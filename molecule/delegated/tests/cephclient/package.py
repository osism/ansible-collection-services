import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_cephclient_install_type(host):
    if get_variable(host, "cephclient_install_type") != "package":
        pytest.skip("cephclient_install_type mismatch")


def test_pkg(host):
    check_cephclient_install_type(host)

    cephclient_packages = get_variable(host, "cephclient_packages")
    assert type(cephclient_packages) is list

    for package_name in cephclient_packages:
        package = host.package(package_name)
        assert package.is_installed


def test_configfile(host):
    check_cephclient_install_type(host)

    f = host.file("/etc/ceph/ceph.conf")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert "[global]" in f.content_string


def test_keyringfile(host):
    check_cephclient_install_type(host)

    cephclient_keyring_name = get_variable(host, "cephclient_keyring_name")

    f = host.file(f"/etc/ceph/ceph.{cephclient_keyring_name}.keyring")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o600
    assert f.user == "root"
    assert f.group == "root"

    cephclient_keyring = get_variable(host, "cephclient_keyring")
    with host.sudo("root"):
        assert cephclient_keyring in f.content_string
