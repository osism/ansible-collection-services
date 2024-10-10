from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


# testing config.yml task
def test_thanos_sidecar_config(host):
    directories = [
        get_variable(host, "thanos_sidecar_docker_compose_directory"),
        get_variable(host, "thanos_sidecar_configuration_directory"),
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")


# testing service.yml tasks
def test_docker_compose(host):
    f = host.file(
        f"{get_variable(host, 'thanos_sidecar_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert "thanos_sidecar:" in f.content_string

    container_name = get_variable(host, "thanos_sidecar_container_name")
    with host.sudo(get_variable(host, "operator_user")):
        assert container_name in f.content_string


def test_thanos_sidecar_service(host):
    service = host.service(get_variable(host, "thanos_sidecar_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_function(host):
    service_host = get_variable(host, "thanos_sidecar_host")
    service_port = get_variable(host, "thanos_sidecar_http_port")

    url = f"http://{service_host}:{service_port}/metrics"

    result = host.run(f"curl -s -o /dev/null -w '%{{http_code}}' {url}")
    assert result.rc == 0
    assert result.stdout.strip() == "200"
