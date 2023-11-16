from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_traefik_directories_created(host):
    directories = [
        get_variable(host, "traefik_docker_compose_directory"),
        get_variable(host, "traefik_certificates_directory"),
        get_variable(host, "traefik_configuration_directory"),
    ]
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    for directory in directories:
        dir = host.file(directory)
        assert dir.exists, f"Directory {directory} should exist"
        assert dir.is_directory, f"{directory} should be a directory"
        assert (
            dir.user == operator_user
        ), f"Directory {directory} should be owned by {operator_user}"
        assert (
            dir.group == operator_group
        ), f"Directory {directory} should be in group {operator_group}"
        assert dir.mode == 0o755, f"Directory {directory} should have 0755 permissions"


def test_traefik_configuration_files(host):
    traefik_configuration_directory = get_variable(
        host, "traefik_configuration_directory"
    )
    config_files = ["traefik.yml", "traefik.env", "certificates.yml"]

    for file in config_files:
        file_path = host.file(f"{traefik_configuration_directory}/{file}")
        assert file_path.exists, f"Configuration file {file} should exist"
        assert file_path.is_file, f"{file} should be a file"
        assert file_path.user == get_variable(
            host, "operator_user"
        ), f"{file} should be owned by the operator user"
        assert file_path.group == get_variable(
            host, "operator_group"
        ), f"{file} should be in the operator group"
        assert file_path.mode == 0o644, f"{file} should have 0644 permissions"


def test_traefik_service_running(host):
    traefik_service_name = get_variable(host, "traefik_service_name")
    service = host.service(traefik_service_name)
    assert service.is_enabled
    assert service.is_running


def test_traefik_external_network_created(host):
    traefik_external_network_name = get_variable(host, "traefik_external_network_name")
    with host.sudo("root"):
        result = host.run(
            f"docker network ls --filter name={traefik_external_network_name}"
        )
        assert (
            traefik_external_network_name in result.stdout
        ), f"Network {traefik_external_network_name} should be created"
