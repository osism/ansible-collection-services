from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_directory(host):
    path = get_variable(host, "adminer_docker_compose_directory")

    f = host.file(path)
    assert f.exists
    assert f.is_directory
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert f.mode == 0o755


def test_file(host):
    path = get_variable(host, "adminer_docker_compose_directory")

    f = host.file(f"{path}/docker-compose.yml")
    assert f.exists
    assert not f.is_directory
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert f.mode == 0o640

    adminer_database_host = get_variable(host, "adminer_database_host")
    assert f'ADMINER_DEFAULT_SERVER: "{adminer_database_host}"' in f.content_string


def test_srv(host):
    service = host.service(get_variable(host, "adminer_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_function(host):
    service_host = get_variable(host, "adminer_host")
    service_port = get_variable(host, "adminer_port")

    url = f"http://{service_host}:{service_port}"

    result = host.run(f"curl -s -o /dev/null -w '%{{http_code}}' {url}")
    assert result.rc == 0
    assert result.stdout.strip() == "200"

    result = host.run(f"curl -s {url} | grep -i adminer")
    assert result.rc == 0
