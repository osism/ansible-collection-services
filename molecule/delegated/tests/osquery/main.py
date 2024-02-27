from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_osquery_package_installed(host):
    osquery_package_name = get_variable(host, "osquery_package_name")
    osquery_package = host.package(osquery_package_name)
    assert osquery_package.is_installed


def test_osquery_service(host):
    service = host.service(get_variable(host, "osquery_service_name"))
    assert service.is_running
    assert service.is_enabled
