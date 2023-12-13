import pytest

from .util.util import get_ansible, get_variable, jinja_replacement

testinfra_runner, testinfra_hosts = get_ansible()


def test_dirs(host):
    directories = [
        get_variable(host, "cgit_docker_compose_directory"),
        get_variable(host, "cgit_configuration_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o755
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_configfile(host):
    f = host.file(f"{get_variable(host, 'cgit_configuration_directory')}/cgitrc")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert "cache-scanrc-ttl=1" in f.content_string

    f = host.file(
        f"{get_variable(host, 'cgit_configuration_directory')}/httpd-cgit.conf"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert "# set server name to start httpd from docker" in f.content_string


def test_dockernetwork(host):
    cgit_traefik = get_variable(host, "cgit_traefik")
    if not cgit_traefik:
        pytest.skip("cgit_traefik not configured")

    traefik_external_network_name = get_variable(host, "traefik_external_network_name")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert traefik_external_network_name in stdout


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'cgit_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    cgit_image = get_variable(host, "cgit_image")
    docker_registry_cgit = get_variable(host, "docker_registry_cgit")
    cgit_tag = get_variable(host, "cgit_tag")
    cgit_image = jinja_replacement(
        cgit_image, {"docker_registry_cgit": docker_registry_cgit, "cgit_tag": cgit_tag}
    )

    with host.sudo(get_variable(host, "operator_user")):
        assert f'image: "{cgit_image}' in f.content_string


def test_srv(host):
    service = host.service(get_variable(host, "cgit_service_name"))

    assert service.is_running
    assert service.is_enabled
