import pytest
from ..util.util import get_ansible, get_variable
from packaging.version import Version

testinfra_runner, testinfra_hosts = get_ansible()


def check_openstackclient_install_type(host):
    if get_variable(host, "openstackclient_install_type") != "package":
        pytest.skip("openstackclient_install_type mismatch")


def test_repository_key_installed(host):
    check_openstackclient_install_type(host)
    debian_version = host.system_info.release
    if Version(debian_version) < Version("22.04"):
        key = get_variable(host, "openstackclient_debian_repository_key")
        assert host.run(f"apt-key list | grep {key}").rc == 0
    else:
        package = host.package("ubuntu-cloud-keyring")
        assert package.is_installed


def test_repository_added(host):
    check_openstackclient_install_type(host)

    if get_variable(host, "openstackclient_configure_repository"):
        repo = get_variable(host, "openstackclient_debian_repository")
        assert host.run(f"apt-cache policy | grep {repo.split(' ')[1]}").rc == 0


def test_openstackclient_packages_installed(host):
    check_openstackclient_install_type(host)

    packages = get_variable(host, "openstackclient_debian_packages")
    for package in packages:
        pkg = host.package(package)
        assert pkg.is_installed
