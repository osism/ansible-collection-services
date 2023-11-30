import pytest

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dockernetwork(host):
    homer_traefik = get_variable(host, "homer_traefik")
    if not homer_traefik:
        pytest.skip("homer_traefik not configured")

    traefik_external_network_name = get_variable(host, "traefik_external_network_name")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert traefik_external_network_name in stdout


def test_dirs(host):
    directories = [
        get_variable(host, "homer_docker_compose_directory"),
        get_variable(host, "homer_configuration_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o750
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_configfile(host):
    f = host.file(f"{get_variable(host, 'homer_configuration_directory')}/config.yml")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert 'title: "Operations dashboard"' in f.content_string


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'homer_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    homer_container_name = get_variable(host, "homer_container_name")

    with host.sudo(get_variable(host, "operator_user")):
        assert f'container_name: "{homer_container_name}' in f.content_string


def test_srv(host):
    service = host.service(get_variable(host, "homer_service_name"))

    assert service.is_running
    assert service.is_enabled
