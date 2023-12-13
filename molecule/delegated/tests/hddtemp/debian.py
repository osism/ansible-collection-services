import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)

    package = host.package("lm-sensors")
    assert package.is_installed

    package = host.package("hddtemp")
    assert not package.is_installed


def test_modulefile(host):
    check_ansible_os_family(host)

    f = host.file("/etc/modules")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert "drivetemp" in f.content_string


def test_module(host):
    check_ansible_os_family(host)

    with host.sudo():
        loaded_modules = host.check_output("lsmod").splitlines()

    assert any("drivetemp" in line for line in loaded_modules)


def test_srv(host):
    check_ansible_os_family(host)

    service_name = "lm-sensors"
    service = host.service(service_name)
    assert service.is_enabled
    assert service.is_running
