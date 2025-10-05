from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_substation_directories(host):
    directories = [
        get_variable(host, "substation_configuration_directory"),
        get_variable(host, "substation_data_directory"),
        get_variable(host, "substation_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_docker_compose_file(host):
    docker_compose_file_path = f"{get_variable(host, 'substation_docker_compose_directory')}/docker-compose.yml"
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_substation_service(host):
    service = host.service(get_variable(host, "substation_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_substation_wrapper_script(host):
    wrapper_script_path = "/usr/local/bin/substation"
    wrapper_script = host.file(wrapper_script_path)
    assert wrapper_script.exists
    assert wrapper_script.user == get_variable(host, "operator_user")
    assert wrapper_script.group == get_variable(host, "operator_group")
    assert wrapper_script.mode == 0o755
