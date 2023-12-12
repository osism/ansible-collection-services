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


def test_traefik_docker_compose_file(host):
    traefik_docker_compose_directory = get_variable(
        host, "traefik_docker_compose_directory"
    )
    docker_compose_file = host.file(
        f"{traefik_docker_compose_directory}/docker-compose.yml"
    )

    assert docker_compose_file.exists, "docker-compose.yml for traefik should exist"
    assert docker_compose_file.is_file, "docker-compose.yml should be a file"
    assert docker_compose_file.user == get_variable(
        host, "operator_user"
    ), "docker-compose.yml should be owned by the operator user"
    assert docker_compose_file.group == get_variable(
        host, "operator_group"
    ), "docker-compose.yml should be in the operator group"
    assert (
        docker_compose_file.mode == 0o640
    ), "docker-compose.yml should have 0640 permissions"


def test_traefik_configuration_files(host):
    traefik_configuration_directory = get_variable(
        host, "traefik_configuration_directory"
    )
    config_files = ["traefik.yml", "traefik.env", "certificates.yml"]

    for f in config_files:
        file_path = host.file(f"{traefik_configuration_directory}/{f}")
        assert file_path.exists, f"Configuration file {f} should exist"
        assert file_path.is_file, f"{f} should be a file"
        assert file_path.user == get_variable(
            host, "operator_user"
        ), f"{f} should be owned by the operator user"
        assert file_path.group == get_variable(
            host, "operator_group"
        ), f"{f} should be in the operator group"
        assert file_path.mode == 0o644, f"{f} should have 0644 permissions"


def test_certificate_files(host):
    traefik_certificates_directory = get_variable(
        host, "traefik_certificates_directory"
    )
    traefik_certificates = get_variable(host, "traefik_certificates")

    for key, value in traefik_certificates.items():
        for suffix in ["cert", "key"]:
            f = host.file(f"{traefik_certificates_directory}/{key}.{suffix}")
            assert f.exists, f"Certificate file {key}.{suffix} should exist"
            assert f.is_file, f"{key}.{suffix} should be a file"
            assert f.user == get_variable(
                host, "operator_user"
            ), f"{key}.{suffix} should be owned by the operator user"
            assert f.group == get_variable(
                host, "operator_group"
            ), f"{key}.{suffix} should be in the operator group"
            assert f.mode == 0o644, f"{key}.{suffix} should have 0644 permissions"


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
