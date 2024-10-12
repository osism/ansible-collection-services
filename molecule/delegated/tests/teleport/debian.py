import pytest
from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_teleport_apt_transport_https_package_installed(host):
    check_ansible_os_family(host)

    teleport_configure_repository = get_variable(host, "teleport_configure_repository")
    if teleport_configure_repository:
        apt_transport_https_package = host.package("apt-transport-https")
        assert apt_transport_https_package.is_installed
