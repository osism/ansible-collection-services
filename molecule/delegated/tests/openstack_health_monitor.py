from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_directories(host):
    directories = [
        get_variable(host, "openstack_health_monitor_configuration_directory"),
        get_variable(host, "openstack_health_monitor_crontabs_directory"),
        get_variable(host, "openstack_health_monitor_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_configuration_files(host):
    files = [
        {
            "path": "openstack_health_monitor_configuration_directory",
            "file": "openstack_health_monitor.env",
        },
        {
            "path": "openstack_health_monitor_configuration_directory",
            "file": "clouds.yml",
        },
        {
            "path": "openstack_health_monitor_configuration_directory",
            "file": "secure.yml",
        },
    ]
    for item in files:
        file_path = f"{get_variable(host, item['path'])}/{item['file']}"
        file = host.file(file_path)
        assert file.exists
        assert not file.is_directory
        assert file.user == get_variable(host, "operator_user")
        assert file.group == get_variable(host, "operator_group")
        assert file.mode == 0o640


def test_docker_compose_file(host):
    docker_compose_file_path = (
        f"{get_variable(host, 'openstack_health_monitor_docker_compose_directory')}/"
        f"docker-compose.yml"
    )
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_openstack_health_monitor_service(host):
    service = host.service(get_variable(host, "openstack_health_monitor_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_cronjob_setup(host):
    cronjob_enabled = get_variable(host, "openstack_health_monitor_cronjob")
    if cronjob_enabled:
        cron_file_path = (
            f"{get_variable(host, 'openstack_health_monitor_crontabs_directory')}/main"
        )
        cron_file = host.file(cron_file_path)
        assert cron_file.exists
        assert cron_file.user == get_variable(host, "operator_user")
        assert "*/10" in cron_file.content_string
