from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_required_directories(host):
    directories = [
        get_variable(host, "wazuh_proxy_docker_compose_directory"),
        get_variable(host, "wazuh_proxy_configuration_directory"),
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")
        assert d.mode == 0o750


def test_nginx_configuration_file(host):
    f = host.file(
        f"{get_variable(host, 'wazuh_proxy_configuration_directory')}/nginx.conf"
    )
    assert f.exists
    assert not f.is_directory
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert f.mode == 0o644

    content = f.content_string
    assert "upstream registration {" in content
    assert "upstream agent_connection {" in content

    registration_port = get_variable(host, "wazuh_proxy_registration_listen_port")
    agent_connection_port = get_variable(
        host, "wazuh_proxy_agent_connection_listen_port"
    )
    assert f"listen 0.0.0.0:{registration_port};" in content
    assert f"listen 0.0.0.0:{agent_connection_port};" in content

    for server in get_variable(host, "wazuh_proxy_registration_upstream_servers"):
        assert f"server {server};" in content
    for server in get_variable(host, "wazuh_proxy_agent_connection_upstream_servers"):
        assert f"server {server};" in content


def test_docker_compose_file(host):
    f = host.file(
        f"{get_variable(host, 'wazuh_proxy_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert f.mode == 0o640

    content = f.content_string
    container_name = get_variable(host, "wazuh_proxy_container_name")
    assert f'container_name: "{container_name}"' in content
    assert "network_mode: host" in content


def test_service(host):
    service = host.service(get_variable(host, "wazuh_proxy_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_listening_ports(host):
    registration_port = get_variable(host, "wazuh_proxy_registration_listen_port")
    agent_connection_port = get_variable(
        host, "wazuh_proxy_agent_connection_listen_port"
    )
    assert host.socket(f"tcp://0.0.0.0:{registration_port}").is_listening
    assert host.socket(f"tcp://0.0.0.0:{agent_connection_port}").is_listening
