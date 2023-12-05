from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_smartmontools_package_installed(host):
    smartd_package_name = get_variable(host, "smartd_package_name")
    smartd_package = host.package(smartd_package_name)
    assert (
        smartd_package.is_installed
    ), f"Package {smartd_package_name} should be installed"


def test_smartd_service_running_and_enabled(host):
    smartd_service_name = get_variable(host, "smartd_service_name")
    smartd_service = host.service(smartd_service_name)
    assert smartd_service.is_running, f"Service {smartd_service_name} should be running"
    assert smartd_service.is_enabled, f"Service {smartd_service_name} should be enabled"


def test_smartd_service_logs(host):
    smartd_service_name = get_variable(host, "smartd_service_name")
    command = f'journalctl -u {smartd_service_name} --no-pager --since "1 minute ago"'
    result = host.run(command)

    assert result.rc == 0, "Failed to run journalctl for smartd service"
    assert "error" not in result.stdout.lower(), "Error found in smartd service logs"


def test_smartd_log_directory_exists(host):
    log_directory = host.file("/var/log/smartd")
    assert log_directory.exists, "/var/log/smartd directory should exist"
    assert log_directory.is_directory, "/var/log/smartd should be a directory"
    assert (
        log_directory.user == "root"
    ), "/var/log/smartd directory should be owned by root"
    assert (
        log_directory.group == "root"
    ), "/var/log/smartd directory should be in the root group"
    assert (
        log_directory.mode == 0o755
    ), "/var/log/smartd directory should have 755 permissions"


def test_smartmontools_config_file(host):
    config_file = host.file("/etc/default/smartmontools")
    assert config_file.exists, "smartmontools configuration file should exist"
    assert config_file.is_file, "smartmontools configuration should be a file"
    assert (
        config_file.user == "root"
    ), "smartmontools configuration file should be owned by root"
    assert (
        config_file.group == "root"
    ), "smartmontools configuration file should be in the root group"
    assert (
        config_file.mode == 0o644
    ), "smartmontools configuration file should have 644 permissions"
