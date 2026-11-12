import yaml

from .util.util import get_ansible, get_variable, jinja_replacement

testinfra_runner, testinfra_hosts = get_ansible()


def get_configuration_file(host):
    return jinja_replacement(
        get_variable(host, "ipmi_exporter_configuration_file"),
        {
            "ipmi_exporter_configuration_directory": get_variable(
                host, "ipmi_exporter_configuration_directory"
            )
        },
    )


def test_package_installed(host):
    package_name = get_variable(host, "ipmi_exporter_package_name")
    package = host.package(package_name)
    assert package.is_installed, f"Package {package_name} should be installed"


def test_configuration_directory(host):
    directory = host.file(get_variable(host, "ipmi_exporter_configuration_directory"))
    assert directory.exists
    assert directory.is_directory
    assert directory.user == "root"
    assert directory.group == "root"
    assert directory.mode == 0o755


def test_configuration_file(host):
    file = host.file(get_configuration_file(host))
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644

    module = yaml.safe_load(file.content_string)["modules"]["default"]
    assert module["collectors"] == get_variable(host, "ipmi_exporter_collectors")
    assert module["exclude_sensor_ids"] == get_variable(
        host, "ipmi_exporter_exclude_sensor_ids"
    )
    assert module["sel_events"] == get_variable(host, "ipmi_exporter_sel_events")
    assert module["collector_cmd"] == get_variable(host, "ipmi_exporter_collector_cmd")
    assert module["custom_args"] == get_variable(host, "ipmi_exporter_custom_args")


def test_defaults_file(host):
    file = host.file("/etc/default/prometheus-ipmi-exporter")
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644

    content = file.content_string
    assert content.startswith('ARGS="')
    assert "--web.listen-address=127.0.0.1:9290" in content
    assert f"--config.file={get_configuration_file(host)}" in content
    assert "--freeipmi.path=/usr/bin" in content


def test_sudoers_file(host):
    file = host.file("/etc/sudoers.d/prometheus-ipmi-exporter")
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o440

    with host.sudo():
        result = host.run(f"visudo -cf {file.path}")
        assert result.rc == 0, result.stderr


def test_sudo_permissions(host):
    # The exporter runs the FreeIPMI tools through sudo, so every command in
    # ipmi_exporter_sudo_commands must be allowed without a password.
    ipmi_exporter_user = get_variable(host, "ipmi_exporter_user")
    with host.sudo():
        result = host.run(f"sudo -l -U {ipmi_exporter_user}")
        assert result.rc == 0, result.stderr

    assert "NOPASSWD" in result.stdout
    for command in get_variable(host, "ipmi_exporter_sudo_commands"):
        assert command in result.stdout, f"{command} should be allowed via sudo"


def test_service_running_and_enabled(host):
    service_name = get_variable(host, "ipmi_exporter_service_name")
    service = host.service(service_name)
    assert service.is_running, f"Service {service_name} should be running"
    assert service.is_enabled, f"Service {service_name} should be enabled"


def test_service_listening(host):
    assert host.socket("tcp://127.0.0.1:9290").is_listening


def test_metrics_endpoint(host):
    # The test node has no BMC, so the collectors themselves fail. The exporter
    # still answers the scrape and reports ipmi_up for every collector, which
    # shows that the configuration file was loaded.
    result = host.run("curl -s -w '\\n%{http_code}' http://127.0.0.1:9290/metrics")
    assert result.rc == 0, result.stderr

    body, status_code = result.stdout.rsplit("\n", 1)
    assert status_code == "200"
    assert "ipmi_up" in body
