import pytest

from ..util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_clamav_service(host):
    service = host.service(
        get_family_role_variable(host, "clamav_freshclam_service_name")
    )

    assert service.is_running
    assert service.is_enabled

    service = host.service(get_family_role_variable(host, "clamav_daemon_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_clamav_configuration_file(host):
    try:
        file_path = get_variable(host, "clamav_configuration_path")
    except Exception:
        try:
            file_path = get_family_role_variable(host, "clamav_configuration_path")
        except Exception:
            pytest.skip("clamav_configuration_path not defined")

    f = host.file(file_path)

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644


def test_function(host):
    with host.sudo():
        result = host.run("clamscan -v -r --stdout /etc")
        assert "SCAN SUMMARY" in result.stdout
        assert "Scanned files: 0" not in result.stdout
        assert result.rc == 0
