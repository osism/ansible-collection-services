import pytest

from .util.util import get_ansible, get_variable, get_os_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package_names = get_os_role_variable(host, "clamav_package_names")
    assert type(package_names) is list

    for package_name in package_names:
        package = host.package(package_name)
        assert package.is_installed


def test_srv(host):
    service = host.service(get_os_role_variable(host, "clamav_freshclam_service_name"))

    assert service.is_running
    assert service.is_enabled

    service = host.service(get_os_role_variable(host, "clamav_daemon_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_configfile(host):
    try:
        file_path = get_variable(host, "clamav_configuration_path")
    except Exception:
        try:
            file_path = get_os_role_variable(host, "clamav_configuration_path")
        except Exception:
            pytest.skip("clamav_configuration_path not defined")

    f = host.file(file_path)

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
