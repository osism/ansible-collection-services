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


def test_service(host):
    service = host.service(get_variable(host, "squid_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_proxy_functionality(host):
    squid_host = get_variable(host, "squid_host")
    squid_port = get_variable(host, "squid_port")

    url = f"http://{squid_host}:{squid_port}"

    # Check if Squid is listening on the configured port
    assert host.socket(f"tcp://{squid_host}:{squid_port}").is_listening

    # Test Squid proxy with curl
    result = host.run(f"curl -v -x {squid_host}:{squid_port} https://www.osism.tech")
    assert result.rc == 0

    # Check HTTP status code
    status_code = host.run(
        f"curl -s -o /dev/null -w '%{{http_code}}' -x {squid_host}:{squid_port} https://osism.tech"
    ).stdout
    assert status_code in ["200"]

    # Check for Squid server header
    result = host.run(f"curl -I -s {url} | grep -i 'Server: squid'")
    assert result.rc == 0

    # Verify Squid is listening on its configured port
    result = host.run(f"netstat -tuln | grep :{squid_port}")
    assert result.rc == 0


def test_config_and_status(host):
    operator_user = get_variable(host, "operator_user")
    # Check Squid's status
    with host.sudo(operator_user):
        result = host.run("docker exec squid squid -k check")
        assert result.rc == 0

    # Verify Squid's configuration
    with host.sudo(operator_user):
        result = host.run("docker exec squid squid -k parse")
        assert result.rc == 0
