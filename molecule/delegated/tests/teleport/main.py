from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_teleport_package(host):
    package_name = get_variable(host, "teleport_package_name")
    package = host.package(package_name)

    assert package.is_installed


def test_teleport_service(host):
    service_name = get_variable(host, "teleport_service_name")
    service = host.service(service_name)

    assert service.is_running
    assert service.is_enabled


def test_function(host):
    result = host.run("teleport version")
    assert result.rc == 0
    assert get_variable(host, "teleport_version") in result.stdout
