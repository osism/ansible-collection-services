from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_metering_dirs(host):
    directories = [
        get_variable(host, "metering_configuration_directory"),
        get_variable(host, "metering_data_directory"),
        get_variable(host, "metering_docker_compose_directory"),
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")


def test_settings_config(host):
    config_dir = get_variable(host, "metering_configuration_directory")
    config = host.file(f"{config_dir}/settings.conf")
    assert config.exists
    assert not config.is_directory
    assert config.mode == 0o640
    assert config.user == get_variable(host, "operator_user")
    assert config.group == get_variable(host, "operator_group")
    assert "file = pushed_billing_data" in config.content_string


def test_docker_compose(host):
    f = host.file(
        f"{get_variable(host, 'metering_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    container_name = get_variable(host, "metering_container_name")
    with host.sudo(get_variable(host, "operator_user")):
        assert container_name in f.content_string


def test_metering_service(host):
    service = host.service(get_variable(host, "metering_service_name"))
    assert service.is_running
    assert service.is_enabled
