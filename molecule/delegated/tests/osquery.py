import pytest
from .util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def test_apt_transport_https_package_installed(host):
    osquery_configure_repository = get_variable(host, "osquery_configure_repository")
    if osquery_configure_repository:
        apt_transport_https_package = host.package("apt-transport-https")
        assert apt_transport_https_package.is_installed, "apt-transport-https package should be installed"


def test_osquery_gpgkey(host):
    osquery_configure_repository = get_variable(host, "osquery_configure_repository")

    if not osquery_configure_repository:
        pytest.skip("osquery_configure_repository is not true")

    url = get_variable(host, "osquery_debian_repository_key")
    key_content = get_from_url(url)

    gpg_key_file = host.file("/etc/apt/trusted.gpg.d/osquery.asc")

    assert gpg_key_file.exists, "GPG key file for osquery does not exist"
    assert not gpg_key_file.is_directory
    assert gpg_key_file.mode == 0o644
    assert gpg_key_file.user == "root"
    assert gpg_key_file.group == "root"
    assert gpg_key_file.content_string == key_content


def test_osquery_package_installed(host):
    osquery_package_name = get_variable(host, "osquery_package_name")
    osquery_package = host.package(osquery_package_name)
    assert osquery_package.is_installed, f"Package {osquery_package_name} should be installed"


def test_osquery_service_running_and_enabled(host):
    osquery_service_name = get_variable(host, "osquery_service_name")
    osquery_service = host.service(osquery_service_name)
    assert osquery_service.is_running, f"Service {osquery_service_name} should be running"
    assert osquery_service.is_enabled, f"Service {osquery_service_name} should be enabled"
