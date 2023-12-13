import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_srv(host):
    check_ansible_os_family(host)

    service_name = "systemd-timesyncd"
    service = host.service(service_name)
    assert not service.is_enabled
    assert not service.is_running
