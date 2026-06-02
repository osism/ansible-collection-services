#!/usr/bin/env bash
set -euo pipefail

# Roles that cannot pass in the local container scenario and are always skipped
# in 'all' mode. To force execution of a skipped role, run it by name directly.
declare -A SKIP_REASONS=(
    [auditd]="kernel audit subsystem (CAP_AUDIT_CONTROL)"
    [cephclient]="docker cp remount-ro blocked by fuse-overlayfs in container"
    [chrony]="CAP_SYS_TIME unavailable in container"
    [docker]="zram storage device not present in container"
    [falco]="kernel module (kmod driver) cannot load in a container; CI runs on real VMs"
    [frr]="sysctl not accessible (CAP_SYS_ADMIN)"
    [hddtemp]="CAP_SYS_MODULE ineffective in rootless Podman user namespace"
    [kepler]="no CI job (role never wired up for testing)"
    [manager]="sysctl fs.inotify.max_user_watches (CAP_SYS_ADMIN)"
    [openstackclient]="docker cp remount-ro blocked by fuse-overlayfs in container"
    [rng]="rng-tools5 has no software fallback; /dev/hwrng inaccessible in rootless container"
    [wireguard]="kernel module required"
    [zuul]="CI job not in check pipeline; requires SSH keypair and TLS certs"
)

# Estimated run times for roles tested in 'all' mode (shown by --help).
declare -A ESTIMATED_TIMES=(
    [adminer]="4:36"
    [cgit]="5:58"
    [clamav]="2:56"
    [containerd]="2:33"
    [dnsdist]="5:18"
    [dnsmasq]="4:25"
    [fail2ban]="1:37"
    [gnmic]="4:58"
    [homer]="5:07"
    [httpd]="4:35"
    [journald]="1:34"
    [lldpd]="1:31"
    [netbird]="2:17"
    [netbox]="17:17"
    [netdata]="3:28"
    [nexus]="7:29"
    [opentelemetry_collector]="6:02"
    [osquery]="2:18"
    [phpmyadmin]="4:48"
    [rsyslog]="2:35"
    [scaphandre]="4:41"
    [smartd]="1:53"
    [squid]="7:12"
    [sshd]="1:27"
    [stepca]="5:24"
    [substation]="5:49"
    [teleport]="2:31"
    [thanos_sidecar]="6:55"
    [traefik]="6:23"
    [tuned]="1:55"
    [wazuh_agent]="2:24"
    [zabbix_agent]="4:37"
)

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
RESET='\033[0m'

format_time() {
    local secs=$1
    if (( secs >= 3600 )); then
        printf "%d:%02d:%02d" $(( secs / 3600 )) $(( (secs % 3600) / 60 )) $(( secs % 60 ))
    else
        printf "%d:%02d" $(( secs / 60 )) $(( secs % 60 ))
    fi
}

usage() {
    local col_width=0
    for role_dir in roles/*/; do
        name="$(basename "$role_dir")"
        (( ${#name} > col_width )) && col_width=${#name}
    done
    (( col_width += 2 ))

    local test_count=0 skip_count=0
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        if [[ -v SKIP_REASONS["$role"] ]]; then
            (( skip_count += 1 ))
        else
            (( test_count += 1 ))
        fi
    done

    local total_est=0
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        est="${ESTIMATED_TIMES[$role]:-?}"
        if [[ ! -v SKIP_REASONS["$role"] ]] && [[ "$est" != "?" ]]; then
            mins="${est%%:*}"
            secs="${est##*:}"
            total_est=$(( total_est + mins * 60 + 10#$secs ))
        fi
    done

    echo "Usage: $0 <role-name>"
    echo "       $0 all"
    echo ""
    echo "=== $test_count to test, $skip_count skipped (estimated total: ~$(format_time $total_est)) ==="
    echo ""
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        printf "  %-${col_width}s" "$role"
        if [[ -v SKIP_REASONS["$role"] ]]; then
            printf "${YELLOW}skip${RESET}  %s\n" "${SKIP_REASONS[$role]}"
        else
            est="${ESTIMATED_TIMES[$role]:-?}"
            printf "test  ~%s\n" "$est"
        fi
    done
}

case "${1:-}" in
    -h|--help)   usage; exit 0 ;;
    "")          usage; exit 1 ;;
esac

ROLE="${ANSIBLE_ROLE:-$1}"

if [ "$ROLE" != "all" ] && [ ! -d "roles/$ROLE" ]; then
    echo "Error: no such role '$ROLE'"
    echo ""
    usage
    exit 1
fi

VENV=".venv"

if command -v uv &>/dev/null; then
    [ -d "$VENV" ] || UV_PYTHON_DOWNLOADS=automatic uv venv --python 3.11 "$VENV"
    uv pip install -q --python "$VENV/bin/python" -r molecule/requirements.txt
else
    python3 -c "
import sys
if sys.version_info >= (3, 14):
    v = sys.version.split()[0]
    print(f'Error: Python {v} is not supported.')
    print('ansible==11.13.0 (ansible-core 2.18.x) requires Python < 3.14.')
    print('Install uv (https://docs.astral.sh/uv/) to have it manage the Python version automatically.')
    sys.exit(1)
" || exit 1
    [ -d "$VENV" ] || python3 -m venv "$VENV"
    "$VENV/bin/pip" install -q --disable-pip-version-check -r molecule/requirements.txt
fi

export PATH="$PWD/$VENV/bin:$PATH"
export MOLECULE_COLLECTIONS_PATH="$PWD/$VENV/.ansible/collections:$HOME/.ansible/collections"
# Molecule detects galaxy.yml and warns that scenarios should move to
# extensions/molecule/. Setting MOLECULE_GLOB explicitly bypasses that
# collection-detection path and keeps the existing molecule/ layout.
export MOLECULE_GLOB="molecule/*/molecule.yml"

if [ -z "${MOLECULE_DRIVER:-}" ]; then
    if command -v podman &>/dev/null; then
        export MOLECULE_DRIVER=podman
    elif command -v docker &>/dev/null; then
        export MOLECULE_DRIVER=docker
    else
        echo "Error: neither podman nor docker found. Install one to run local molecule tests."
        exit 1
    fi
fi
# molecule/local/molecule.yml uses ${DRIVER} for driver.name. Molecule
# keeps all MOLECULE_* variables unexpanded in molecule.yml (MOLECULE_KEEP_STRING),
# so MOLECULE_DRIVER cannot be referenced directly from the YAML.
export DRIVER="$MOLECULE_DRIVER"

run_role() {
    echo "=== molecule: $1 (driver: $MOLECULE_DRIVER) ==="
    ANSIBLE_ROLE="$1" "$VENV/bin/python" -m molecule test -s local
}

if [ "$ROLE" = "all" ]; then
    declare -A RESULT
    declare -A ELAPSED
    PASS_COUNT=0
    FAIL_COUNT=0
    SKIP_COUNT=0

    COL_WIDTH=0
    for role_dir in roles/*/; do
        name="$(basename "$role_dir")"
        (( ${#name} > COL_WIDTH )) && COL_WIDTH=${#name}
    done
    (( COL_WIDTH += 2 ))

    all_start=$(date +%s)

    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        if [[ -v SKIP_REASONS["$role"] ]]; then
            RESULT["$role"]="SKIP"
            SKIP_COUNT=$(( SKIP_COUNT + 1 ))
            continue
        fi
        # Reset state before each run: a crashed container from the previous
        # role can leave created=true in the state file, causing the next
        # role to skip create and converge against a non-existent container.
        ANSIBLE_ROLE="$role" "$VENV/bin/python" -m molecule reset -s local \
            >/dev/null 2>&1 || true
        role_start=$(date +%s)
        if run_role "$role"; then
            RESULT["$role"]="PASS"
            PASS_COUNT=$(( PASS_COUNT + 1 ))
        else
            RESULT["$role"]="FAIL"
            FAIL_COUNT=$(( FAIL_COUNT + 1 ))
        fi
        ELAPSED["$role"]=$(( $(date +%s) - role_start ))
    done

    total_secs=$(( $(date +%s) - all_start ))

    echo ""
    echo "=== Results: $PASS_COUNT passed, $SKIP_COUNT skipped, $FAIL_COUNT failed (total: $(format_time $total_secs)) ==="
    echo ""
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        printf "  %-${COL_WIDTH}s" "$role"
        case "${RESULT[$role]:-}" in
            PASS) printf "${GREEN}pass${RESET}  %s\n" "$(format_time "${ELAPSED[$role]:-0}")" ;;
            FAIL) printf "${RED}FAIL${RESET}  %s\n" "$(format_time "${ELAPSED[$role]:-0}")" ;;
            SKIP) printf "${YELLOW}skip${RESET}  %s\n" "${SKIP_REASONS[$role]}" ;;
        esac
    done
    echo ""

    [ "$FAIL_COUNT" -eq 0 ]
else
    run_role "$ROLE"
fi
