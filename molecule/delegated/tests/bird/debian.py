import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_conffile(host):
    check_ansible_os_family(host)

    with host.sudo("bird"):
        f = host.file("/etc/bird/bird.conf")
        assert f.exists
        assert not f.is_directory
        assert f.user == "bird"
        assert f.group == "bird"
        assert f.mode == 0o640

        bird_cidr = get_variable(host, "bird_cidr")
        assert f"if net ~ [ {bird_cidr}+ ] then " in f.content_string
