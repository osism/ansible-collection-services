import pytest
from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def check_openstackclient_install_type(host):
    if get_variable(host, "openstackclient_install_type") != "package":
        pytest.skip("openstackclient_install_type mismatch")


def test_repository_key_installed(host):
    check_ansible_os_family(host)
    check_openstackclient_install_type(host)

    if get_variable(host, "ansible_distribution", True) != "Ubuntu":
        pytest.skip("ansible_distribution is not Ubuntu")

    package = host.package("ubuntu-cloud-keyring")
    assert package.is_installed


def test_repository_added(host):
    check_ansible_os_family(host)
    check_openstackclient_install_type(host)

    if get_variable(host, "ansible_distribution", True) != "Ubuntu":
        pytest.skip("ansible_distribution is not Ubuntu")

    if get_variable(host, "openstackclient_configure_repository"):
        repo = get_variable(host, "openstackclient_ubuntu_repository")
        assert host.run(f"apt-cache policy | grep {repo.split(' ')[1]}").rc == 0


def test_openstackclient_packages_installed(host):
    check_ansible_os_family(host)
    check_openstackclient_install_type(host)

    packages = get_variable(host, "openstackclient_debian_packages")
    for package in packages:
        pkg = host.package(package)
        assert pkg.is_installed
