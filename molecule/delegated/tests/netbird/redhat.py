import pytest
from ..util.util import (
    get_ansible,
    get_variable,
    get_family_role_variable,
    # get_from_url,
    # get_centos_repo_key,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_netbird_repository_key(host):
    check_ansible_os_family(host)

    netbird_configure_repository = get_variable(host, "netbird_configure_repository")

    if not netbird_configure_repository:
        pytest.skip("netbird_configure_repository is not true")

    # key_content = get_from_url(get_variable(host, "netbird_redhat_repository_key"))


def test_netbird_package(host):
    check_ansible_os_family(host)

    package_name = get_family_role_variable(host, "netbird_package_name")
    package = host.package(package_name)
    assert package.is_installed


def test_netbird_service(host):
    check_ansible_os_family(host)

    service_name = get_family_role_variable(host, "netbird_service_name")
    service = host.service(service_name)

    assert service.is_running
    assert service.is_enabled
