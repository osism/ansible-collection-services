import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_srv(host):
    """Check if the systemd-timesyncd service is disabled."""

    check_ansible_os_family(host)

    service = host.service("systemd-timesyncd")
    cmd = host.run(
        f'systemctl list-units --all | grep -q "^[[:space:]]*{service.name}"'
    )

    if cmd.rc == 0:
        assert not service.is_enabled, f"{service.name} should not be enabled"
        assert not service.is_running, f"{service.name} should not be running"
    else:
        pytest.skip("The systemd-timesyncd service does not exist")
