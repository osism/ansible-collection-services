import pytest

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dockernetwork(host):
    phpmyadmin_traefik = get_variable(host, "phpmyadmin_traefik")
    if not phpmyadmin_traefik:
        pytest.skip("phpmyadmin_traefik not configured")

    traefik_external_network_name = get_variable(host, "traefik_external_network_name")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert traefik_external_network_name in stdout


def test_dirs(host):
    directory = get_variable(host, "phpmyadmin_docker_compose_directory")
    d = host.file(directory)

    assert d.exists
    assert d.is_directory
    assert d.mode == 0o755
    assert d.user == get_variable(host, "operator_user")
    assert d.group == get_variable(host, "operator_group")


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'phpmyadmin_docker_compose_directory')}/docker-compose.yml"
    )

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    with host.sudo(get_variable(host, "operator_user")):
        assert "container_name: phpmyadmin" in f.content_string


def test_srv(host):
    s = host.service(get_variable(host, "phpmyadmin_service_name"))

    assert s.is_running
    assert s.is_enabled
