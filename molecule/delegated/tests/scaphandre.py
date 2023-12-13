from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_scaphandre_directories_created(host):
    directories = [
        get_variable(host, "scaphandre_docker_compose_directory"),
        get_variable(host, "scaphandre_configuration_directory"),
    ]
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    for directory in directories:
        dir = host.file(directory)
        assert dir.exists, f"Directory {directory} should exist"
        assert dir.is_directory, f"{directory} should be a directory"
        assert dir.user == operator_user
        assert dir.group == operator_group
        assert dir.mode == 0o750, f"Directory {directory} should have 0750 permissions"


def test_scaphandre_docker_compose_file(host):
    scaphandre_docker_compose_directory = get_variable(
        host, "scaphandre_docker_compose_directory"
    )
    docker_compose_file = host.file(
        f"{scaphandre_docker_compose_directory}/docker-compose.yml"
    )

    assert docker_compose_file.exists, "docker-compose.yml for scaphandre should exist"
    assert docker_compose_file.is_file, "docker-compose.yml should be a file"
    assert docker_compose_file.user == get_variable(host, "operator_user"), (
        "docker-compose.yml should be " "owned by the operator user"
    )
    assert docker_compose_file.group == get_variable(host, "operator_group"), (
        "docker-compose.yml should be " "in the operator group"
    )
    assert (
        docker_compose_file.mode == 0o640
    ), "docker-compose.yml should have 0640 permissions"


def test_scaphandre_service_running(host):
    scaphandre_service_name = get_variable(host, "scaphandre_service_name")
    service = host.service(scaphandre_service_name)
    assert service.is_enabled
    assert service.is_running
