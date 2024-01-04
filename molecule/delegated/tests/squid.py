from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_directories(host):
    directories = [
        get_variable(host, "squid_configuration_directory"),
        f"{get_variable(host, 'squid_configuration_directory')}/conf.d",
        get_variable(host, "squid_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_configuration_files(host):
    files = ["osism.conf"]
    for file_name in files:
        file_path = (
            f"{get_variable(host, 'squid_configuration_directory')}/conf.d/{file_name}"
        )
        file = host.file(file_path)
        assert file.exists
        assert not file.is_directory
        assert file.user == get_variable(host, "operator_user")
        assert file.group == get_variable(host, "operator_group")
        assert file.mode == 0o644


def test_docker_compose_file(host):
    docker_compose_file_path = (
        f"{get_variable(host, 'squid_docker_compose_directory')}/docker-compose.yml"
    )
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_srv(host):
    service = host.service(get_variable(host, "squid_service_name"))
    assert service.is_running
    assert service.is_enabled
