from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_tang_packages_installed(host):
    """
    Test that the tang package is installed.
    """
    tang_package_name = get_variable(host, "tang_package_name")

    pkg = host.package(tang_package_name)
    assert pkg.is_installed, f"Package {tang_package_name} should be installed"


def test_tang_service_installed(host):
    """
    Test that the tang service is installed, enabled, and running.
    """
    tang_service_name = get_variable(host, "tang_service_name")
    service = host.service(tang_service_name)

    assert service.is_running, f"Service {tang_service_name} should be running"
    assert service.is_enabled, f"Service {tang_service_name} should be enabled"


def test_tang_service_status(host):
    """
    Test that the tang service is active and listening using systemctl.
    """
    tang_service_name = get_variable(host, "tang_service_name")
    with host.sudo():
        # Run the systemctl status command
        result = host.run(f"systemctl status {tang_service_name}")
        assert (
            "active (listening)" in result.stdout
        ), f"{tang_service_name} should be active and listening"


def test_tang_socket_configuration(host):
    """
    Test that the tang socket configuration file is properly deployed.
    """
    systemd_destination = get_variable(host, "systemd_destination")
    tang_service_name = get_variable(host, "tang_service_name")
    config_file_path = f"{systemd_destination}/{tang_service_name}"
    config_file = host.file(config_file_path)

    assert config_file.exists, f"Configuration file {config_file_path} should exist"
    assert config_file.is_file, f"{config_file_path} should be a file"
    assert config_file.user == "root", f"{config_file_path} should be owned by root"
    assert config_file.group == "root", f"{config_file_path} should be in group root"
    assert config_file.mode == 0o644, f"{config_file_path} should have 0644 permissions"


def test_function(host):
    result = host.run("tang-show-keys")
    assert result.rc == 0
    assert len(result.stdout) > 0
