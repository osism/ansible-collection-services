import socket

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dirs(host):
    directories = [
        get_variable(host, "dnsdist_docker_compose_directory"),
        get_variable(host, "dnsdist_configuration_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o750
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_configfile(host):
    f = host.file(
        f"{get_variable(host, 'dnsdist_configuration_directory')}/dnsdist.conf"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")
    assert "addLocal('0.0.0.0:53')" in f.content_string


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'dnsdist_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    dnsdist_container_name = get_variable(host, "dnsdist_container_name")

    with host.sudo(get_variable(host, "operator_user")):
        assert f'container_name: "{dnsdist_container_name}' in f.content_string


def test_srv(host):
    service = host.service(get_variable(host, "dnsdist_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_dns_resolution(host):
    service_host = get_variable(host, "dnsdist_host")
    service_port = get_variable(host, "dnsdist_port")

    cmd = host.run(f"dig @{service_host} -p {service_port} osism.tech +short")
    assert cmd.rc == 0
    assert cmd.stdout.strip() != ""


def test_dns_reverse_lookup(host):
    service_host = get_variable(host, "dnsdist_host")
    service_port = get_variable(host, "dnsdist_port")

    ip = socket.gethostbyname("osism.tech")
    cmd = host.run(f"dig @{service_host} -p {service_port} -x {ip} +short")
    assert cmd.rc == 0
    assert cmd.stdout.strip() != ""
