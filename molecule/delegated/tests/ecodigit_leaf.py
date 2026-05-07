from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_ecodigit_leaf_directories_created(host):
    directories = [
        get_variable(host, "leaf_docker_compose_directory"),
        get_variable(host, "leaf_configuration_directory"),
        get_variable(host, "leaf_kubeconfig_directory"),
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


def test_ecodigit_leaf_docker_compose_file(host):
    leaf_docker_compose_directory = get_variable(host, "leaf_docker_compose_directory")
    docker_compose_file = host.file(
        f"{leaf_docker_compose_directory}/docker-compose.yml"
    )

    assert docker_compose_file.exists, "docker-compose.yml for leaf should exist"
    assert docker_compose_file.is_file, "docker-compose.yml should be a file"
    assert docker_compose_file.user == get_variable(host, "operator_user"), (
        "docker-compose.yml should be owned by the operator user"
    )
    assert docker_compose_file.group == get_variable(host, "operator_group"), (
        "docker-compose.yml should be in the operator group"
    )
    assert (
        docker_compose_file.mode == 0o640
    ), "docker-compose.yml should have 0640 permissions"


def test_ecodigit_leaf_config_file(host):
    leaf_configuration_directory = get_variable(host, "leaf_configuration_directory")
    config_file = host.file(f"{leaf_configuration_directory}/config.yaml")

    assert config_file.exists, "config.yaml for leaf should exist"
    assert config_file.is_file, "config.yaml should be a file"
    assert config_file.user == get_variable(host, "operator_user"), (
        "config.yaml should be owned by the operator user"
    )
    assert config_file.group == get_variable(host, "operator_group"), (
        "config.yaml should be in the operator group"
    )
    assert config_file.mode == 0o640, "config.yaml should have 0640 permissions"


def test_ecodigit_leaf_service_running(host):
    leaf_service_name = get_variable(host, "leaf_service_name")
    service = host.service(leaf_service_name)
    assert service.is_enabled
    assert service.is_running
