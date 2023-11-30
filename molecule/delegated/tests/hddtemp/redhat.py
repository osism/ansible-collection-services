import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_pkg(host):
    check_ansible_os_family(host)

    package = host.package("epel-release")
    assert package.is_installed

    package = host.package("hddtemp")
    assert package.is_installed


def test_configfile(host):
    check_ansible_os_family(host)

    f = host.file("/etc/sysconfig/hddtemp")
    assert f.exists
    assert not f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    assert (
        "--listen 127.0.0.1 --daemon --port 7634 --syslog=1 /dev/sd[a-z] /dev/sd[a-z][a-z]"
        in f.content_string
    )


def test_srv(host):
    check_ansible_os_family(host)

    service_name = "hddtemp"
    service = host.service(service_name)
    assert service.is_enabled
    assert service.is_running
