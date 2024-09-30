from .util.util import get_ansible, get_variable, assert_service_running_and_enabled

testinfra_runner, testinfra_hosts = get_ansible()


def test_metering_directories_created(host):
    directories = [
        get_variable(host, "metering_configuration_directory"),
        get_variable(host, "metering_data_directory"),
        get_variable(host, "metering_docker_compose_directory"),
    ]
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == operator_user
        assert dir.group == operator_group
        assert dir.mode == 0o750


def test_metering_docker_compose_file(host):
    metering_docker_compose_directory = get_variable(
        host, "metering_docker_compose_directory"
    )
    docker_compose_file = host.file(
        f"{metering_docker_compose_directory}/docker-compose.yml"
    )

    assert docker_compose_file.exists, "docker-compose.yml for metering should exist"
    assert docker_compose_file.is_file, "docker-compose.yml should be a file"
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_metering_container_running(host):
    metering_container_name = get_variable(host, "metering_container_name")
    with host.sudo("root"):
        result = host.run(f"docker ps --filter name={metering_container_name}")
        assert metering_container_name in result.stdout


def test_metering_service_running(host):
    assert_service_running_and_enabled(
        host, get_variable(host, "metering_service_name")
    )
