from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_lldpd_package_installed(host):
    lldpd_package_name = get_variable(host, "lldpd_package_name")
    lldpd_package = host.package(lldpd_package_name)
    assert (
        lldpd_package.is_installed
    ), f"Package {lldpd_package_name} should be installed"


def test_lldpd_service_running_and_enabled(host):
    lldpd_service_name = get_variable(host, "lldpd_service_name")
    lldpd_service = host.service(lldpd_service_name)
    assert lldpd_service.is_running, f"Service {lldpd_service_name} should be running"
    assert lldpd_service.is_enabled, f"Service {lldpd_service_name} should be enabled"
