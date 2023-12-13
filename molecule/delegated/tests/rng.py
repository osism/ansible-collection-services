from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_rng_package_installed(host):
    os_family = get_variable(host, "ansible_os_family", fact=True)
    rng_package_name = "rng-tools5" if os_family == "Debian" else "rng-tools"

    rng_package = host.package(rng_package_name)
    assert rng_package.is_installed, f"Package {rng_package_name} should be installed"


def test_haveged_package_removed(host):
    haveged_package = host.package("haveged")
    assert not haveged_package.is_installed, "Package haveged should be removed"


def test_rng_service_running_and_enabled(host):
    rng_service = host.service("rngd")
    assert rng_service.is_running, "Service rngd should be running"
    assert rng_service.is_enabled, "Service rngd should be enabled"
