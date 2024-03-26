import pytest
from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def check_openstackclient_install_type(host):
    if get_variable(host, "openstackclient_install_type") != "package":
        pytest.skip("openstackclient_install_type mismatch")


def test_openstackclient_packages_installed(host):
    check_ansible_os_family(host)
    check_openstackclient_install_type(host)

    packages = get_variable(host, "openstackclient_redhat_packages")
    for package in packages:
        pkg = host.package(package)
        assert pkg.is_installed
