import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_srv(host):
    """
    Temporary skipping on Ubuntu 24.04 as the service is currently unstable on 24.04
    Also see: https://bugs.launchpad.net/ubuntu/+source/fail2ban/+bug/2055114
    """

    if (
        get_variable(host, "ansible_distribution", True) == "Ubuntu"
        and get_variable(host, "ansible_distribution_version", True) == "24.04"
    ):
        pytest.skip("Skipping this test on Ubuntu 24.04")

    service = host.service(get_variable(host, "fail2ban_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_pkg(host):
    package_name = get_variable(host, "fail2ban_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed
