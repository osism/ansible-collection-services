#!/usr/bin/env bash
set -euo pipefail

# Roles that cannot pass in the local container scenario and are always skipped
# in 'all' mode. To force execution of a skipped role, run it by name directly.
declare -A SKIP_REASONS=(
    [auditd]="kernel audit subsystem (CAP_AUDIT_CONTROL)"
    [cephclient]="docker cp remount-ro blocked by fuse-overlayfs in container"
    [chrony]="CAP_SYS_TIME unavailable in container"
    [docker]="zram storage device not present in container"
    [falco]="package not available in Debian repos"
    [frr]="sysctl not accessible (CAP_SYS_ADMIN)"
    [hddtemp]="CAP_SYS_MODULE ineffective in rootless Podman user namespace"
    [kepler]="missing prepare file"
    [manager]="sysctl fs.inotify.max_user_watches (CAP_SYS_ADMIN)"
    [openstackclient]="docker cp remount-ro blocked by fuse-overlayfs in container"
    [rng]="rng-tools5 has no software fallback; /dev/hwrng inaccessible in rootless container"
    [wireguard]="kernel module required"
    [zuul]="SSH keypair + ZooKeeper TLS pre-configuration required"
)

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
RESET='\033[0m'

usage() {
    echo "Usage: $0 <role-name>"
    echo "       $0 all"
    echo ""
    echo "Available roles:"
    for role_dir in roles/*/; do basename "$role_dir"; done
}

case "${1:-}" in
    -h|--help) usage; exit 0 ;;
    "")        usage; exit 1 ;;
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
    PASS_COUNT=0
    FAIL_COUNT=0
    SKIP_COUNT=0

    COL_WIDTH=0
    for role_dir in roles/*/; do
        name="$(basename "$role_dir")"
        (( ${#name} > COL_WIDTH )) && COL_WIDTH=${#name}
    done
    (( COL_WIDTH += 2 ))

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
        if run_role "$role"; then
            RESULT["$role"]="PASS"
            PASS_COUNT=$(( PASS_COUNT + 1 ))
        else
            RESULT["$role"]="FAIL"
            FAIL_COUNT=$(( FAIL_COUNT + 1 ))
        fi
    done

    echo ""
    echo "=== Results: $PASS_COUNT passed, $SKIP_COUNT skipped, $FAIL_COUNT failed ==="
    echo ""
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        printf "  %-${COL_WIDTH}s" "$role"
        case "${RESULT[$role]:-}" in
            PASS) printf "${GREEN}pass${RESET}\n" ;;
            FAIL) printf "${RED}FAIL${RESET}\n" ;;
            SKIP) printf "${YELLOW}skip${RESET}  %s\n" "${SKIP_REASONS[$role]}" ;;
        esac
    done
    echo ""

    [ "$FAIL_COUNT" -eq 0 ]
else
    run_role "$ROLE"
fi
