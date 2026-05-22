#!/usr/bin/env bash
set -euo pipefail

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

run_role() {
    echo "=== molecule: $1 (driver: $MOLECULE_DRIVER) ==="
    ANSIBLE_ROLE="$1" "$VENV/bin/python" -m molecule test -s local --driver-name "$MOLECULE_DRIVER"
}

if [ "$ROLE" = "all" ]; then
    PASS=()
    FAIL=()
    for role_dir in roles/*/; do
        role="$(basename "$role_dir")"
        if run_role "$role"; then
            PASS+=("$role")
        else
            FAIL+=("$role")
        fi
    done
    echo ""
    echo "=== Results: ${#PASS[@]} passed, ${#FAIL[@]} failed ==="
    [ ${#PASS[@]} -gt 0 ] && printf "  PASS: %s\n" "${PASS[@]}"
    [ ${#FAIL[@]} -gt 0 ] && printf "  FAIL: %s\n" "${FAIL[@]}"
    [ ${#FAIL[@]} -eq 0 ]
else
    run_role "$ROLE"
fi
