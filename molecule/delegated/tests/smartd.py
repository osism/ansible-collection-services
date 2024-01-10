from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_smartmontools_installation(host):
    smartd_package = host.package(get_variable(host, "smartd_package_name"))
    assert smartd_package.is_installed


def test_smartd_directory(host):
    log_directory = host.file("/var/log/smartd")
    assert log_directory.exists
    assert log_directory.is_directory
    assert log_directory.user == "root"
    assert log_directory.group == "root"
    assert log_directory.mode == 0o755


def test_smartmontools_config(host):
    config_file = host.file("/etc/default/smartmontools")
    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == "root"
    assert config_file.group == "root"
    assert config_file.mode == 0o644
    assert (
        "# Defaults for smartmontools initscript (/etc/init.d/smartmontools)"
        in config_file.content_string
    )


"""
The ConditionVirtualization is a systemd condition that checks whether the system is
running in a virtualized environment. It can be used as part of the systemd service
unit configuration to control whether a service should start based on whether the
system is virtualized or not.

The smartd service has a condition set: ConditionVirtualization=no. Hence the smartd
service will only start if the system is not virtualized and the following test will fail.
"""
# def test_smartd_service(host):
#    service = host.service(get_variable(host, "smartd_service_name"))
#    assert service.is_running
#    assert service.is_enabled
