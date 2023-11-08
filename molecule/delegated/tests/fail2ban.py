from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_srv(host):
    service = host.service(get_variable(host, "fail2ban_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_pkg(host):
    package_name = get_variable(host, "fail2ban_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed
