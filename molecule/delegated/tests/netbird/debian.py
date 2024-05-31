import pytest
from ..util.util import (
    get_ansible,
    get_variable,
    get_from_url,
    get_family_role_variable,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_netbird_repository_key(host):
    check_ansible_os_family(host)

    if not get_variable(host, "netbird_configure_repository"):
        pytest.skip("netbird_configure_repository is not true")

    key_file = host.file("/etc/apt/trusted.gpg.d/netbird.asc")
    key_content = get_from_url(get_variable(host, "netbird_debian_repository_key"))

    assert key_file.exists
    assert not key_file.is_directory
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content


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
