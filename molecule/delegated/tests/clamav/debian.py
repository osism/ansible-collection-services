import pytest

from ..util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_clamav_packages(host):
    check_ansible_os_family(host)

    package_names = get_family_role_variable(host, "clamav_package_names")
    assert type(package_names) is list

    for package_name in package_names:
        package = host.package(package_name)
        assert package.is_installed
