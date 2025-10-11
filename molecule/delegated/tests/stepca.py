from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_directories(host):
    docker_dir = host.file(get_variable(host, "stepca_docker_compose_directory"))
    assert docker_dir.exists
    assert docker_dir.is_directory
    assert docker_dir.user == get_variable(host, "operator_user")
    assert docker_dir.group == get_variable(host, "operator_group")
    assert docker_dir.mode == 0o755

    config_dir = host.file(get_variable(host, "stepca_configuration_directory"))
    assert config_dir.exists
    assert config_dir.is_directory
    assert config_dir.user == get_variable(host, "operator_user")
    assert config_dir.group == get_variable(host, "operator_group")
    assert config_dir.mode == 0o750


def test_docker_compose_file(host):
    compose_file = host.file(
        f"{get_variable(host, 'stepca_docker_compose_directory')}/docker-compose.yml"
    )
    assert compose_file.exists
    assert not compose_file.is_directory
    assert compose_file.mode == 0o640
    assert compose_file.user == get_variable(host, "operator_user")
    assert compose_file.group == get_variable(host, "operator_group")

    # Verify critical content
    assert "smallstep/step-ca" in compose_file.content_string
    assert "/home/step" in compose_file.content_string
    assert "9000:9000" in compose_file.content_string


def test_docker_network(host):
    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert "stepca_default" in stdout


def test_systemd_service(host):
    service = host.service(get_variable(host, "stepca_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_stepca_api_health(host):
    stepca_port = get_variable(host, "stepca_port")

    # Test health endpoint
    health_url = f"https://localhost:{stepca_port}/health"
    result = host.run(f"curl -k -s -o /dev/null -w '%{{http_code}}' {health_url}")
    assert result.rc == 0
    assert result.stdout.strip() == "200"

    # Verify health response contains "ok"
    result = host.run(f"curl -k -s {health_url}")
    assert result.rc == 0
    assert "ok" in result.stdout.lower()
