from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dnsmasq_directories(host):
    directories = [
        get_variable(host, "dnsmasq_docker_compose_directory"),
        get_variable(host, "dnsmasq_configuration_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o750
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_dnsmasq_service(host):
    service = host.service(get_variable(host, "dnsmasq_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_dnsmasq_container(host):
    container_name = get_variable(host, "dnsmasq_container_name")
    container = host.docker(container_name)

    assert container.is_running
