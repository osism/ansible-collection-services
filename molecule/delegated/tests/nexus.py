from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_directories(host):
    docker_dir = host.file(get_variable(host, "nexus_docker_compose_directory"))
    assert docker_dir.exists
    assert docker_dir.is_directory
    assert docker_dir.user == get_variable(host, "operator_user")
    assert docker_dir.group == get_variable(host, "operator_group")
    assert docker_dir.mode == 0o755

    config_dir = host.file(get_variable(host, "nexus_configuration_directory"))
    assert config_dir.exists
    assert config_dir.is_directory
    assert config_dir.uid == 200
    assert config_dir.gid == 200
    assert config_dir.mode == 0o755


def test_configuration_files(host):
    files = [
        {
            "path": "nexus_configuration_directory",
            "file": "nexus.properties",
        },
        {
            "path": "nexus_configuration_directory",
            "file": "nexus.env",
        },
    ]
    for item in files:
        file_path = f"{get_variable(host, item['path'])}/{item['file']}"
        file = host.file(file_path)
        assert file.exists
        assert not file.is_directory
        assert file.uid == 200
        assert file.gid == 200
        assert file.mode == 0o644


def test_dockernetwork(host):
    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert "nexus_default" in stdout


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'nexus_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    nexus_container_name = get_variable(host, "nexus_container_name")

    with host.sudo(get_variable(host, "operator_user")):
        assert f'container_name: "{nexus_container_name}"' in f.content_string


def test_nexus_service(host):
    service = host.service(get_variable(host, "nexus_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_nexus_urls(host):
    nexus_host = get_variable(host, "nexus_host")
    nexus_port = get_variable(host, "nexus_port")
    get_http_code = 'curl -o /dev/null -s -w "%{http_code}"'

    # testing nexus http url
    nexus_url = f"http://{nexus_host}:{nexus_port}/service/rest/v1/status"
    response = host.run(f"{get_http_code} {nexus_url}")

    assert response.stdout == "200"
