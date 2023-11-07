import pytest

from ..util.util import get_ansible, get_variable, get_os_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_srv(host):
    service_name = get_os_role_variable(host, "chrony_service_name")
    service = host.service(service_name)
    assert service.is_enabled
    assert service.is_running


def test_pkg(host):
    package_name = get_variable(host, "chrony_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_configfile(host):
    try:
        file_path = get_variable(host, "chrony_conf_file")
    except Exception:
        try:
            file_path = get_os_role_variable(host, "chrony_conf_file")
        except Exception:
            pytest.skip("chrony_conf_file not defined")

    f = host.file(file_path)
    if not f.exists:
        pytest.skip("No existing config file")

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
