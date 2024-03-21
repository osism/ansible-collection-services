from .util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_rsyslog_package_installed(host):
    rsyslog_package_name = get_variable(host, "rsyslog_package_name")
    rsyslog_package = host.package(rsyslog_package_name)
    assert (
        rsyslog_package.is_installed
    ), f"Package {rsyslog_package_name} should be installed"


def test_rsyslog_service_running_and_enabled(host):
    rsyslog_service_name = get_variable(host, "rsyslog_service_name")
    rsyslog_service = host.service(rsyslog_service_name)

    # Check service status using journalctl
    service_status_check = host.run(f"journalctl -xeu {rsyslog_service_name}")

    assert rsyslog_service.is_running, (
        f"Service {rsyslog_service_name} should be running.\n"
        f"Service status check output: {service_status_check.stdout}"
    )

    assert rsyslog_service.is_enabled, f"Service {rsyslog_service_name} should be enabled"



def test_rsyslog_configuration_files(host):
    with host.sudo("root"):
        rsyslog_conf_file = host.file("/etc/rsyslog.conf")

        assert rsyslog_conf_file.exists, "rsyslog.conf should exist"
        assert rsyslog_conf_file.is_file, "rsyslog.conf should be a file"
        assert rsyslog_conf_file.user == "root", "rsyslog.conf should be owned by root"
        assert rsyslog_conf_file.group == "root", "rsyslog.conf should be in the root group"
        assert rsyslog_conf_file.mode == 0o644, "rsyslog.conf should have 0644 permissions"

        os_distribution = get_variable(host, "ansible_distribution", True)
        if os_distribution == "Debian":
            expected_rsyslog_user = "root"
        else:
            expected_rsyslog_user = get_family_role_variable(host, "rsyslog_user")

        rsyslog_file_owner = "$FileOwner {}".format(expected_rsyslog_user)

        assert "MODULES" in rsyslog_conf_file.content_string
        assert rsyslog_file_owner in rsyslog_conf_file.content_string, "rsyslog.conf should contain the correct FileOwner setting"

        # Check Fluentd and additional log server configurations if enabled
        rsyslog_fluentd = get_variable(host, "rsyslog_fluentd")
        rsyslog_additional_host = get_variable(host, "rsyslog_additional_host")

        if rsyslog_fluentd:
            fluentd_conf_file = host.file("/etc/rsyslog.d/70-fluentd.conf")
            assert fluentd_conf_file.exists, "70-fluentd.conf should exist"
            assert fluentd_conf_file.mode == 0o644, "70-fluentd.conf should have 0644 permissions"
            assert fluentd_conf_file.user == "root", "70-fluentd.conf should be owned by root"
            assert fluentd_conf_file.group == "root", "70-fluentd.conf should be in the root group"

        if rsyslog_additional_host:
            additional_log_server_conf_file = host.file("/etc/rsyslog.d/71-additional-log-server.conf")
            assert additional_log_server_conf_file.exists, "71-additional-log-server.conf should exist"
            assert additional_log_server_conf_file.mode == 0o644, "71-additional-log-server.conf should have 0644 permissions"
            assert additional_log_server_conf_file.user == "root", "71-additional-log-server.conf should be owned by root"
            assert additional_log_server_conf_file.group == "root", "71-additional-log-server.conf should be in the root group"
