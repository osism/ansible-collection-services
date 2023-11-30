import pytest

from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def check_cephclient_install_type(host):
    if get_variable(host, "cephclient_install_type") != "package":
        pytest.skip("cephclient_install_type mismatch")


def test_gpg_key(host):
    check_cephclient_install_type(host)

    cephclient_configure_repository = get_variable(
        host, "cephclient_configure_repository"
    )

    if not cephclient_configure_repository:
        pytest.skip("cephclient_configure_repository not configured")

    cephclient_repository_key_url = get_variable(
        host, "cephclient_debian_repository_key"
    )

    # Fetch the GPG key content from the URL
    key_content = get_from_url(cephclient_repository_key_url)

    # Validate the permissions and ownership of the GPG key file
    key_file = host.file("/etc/apt/trusted.gpg.d/cephclient.asc")
    assert key_file.exists
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content


def test_pkg(host):
    check_cephclient_install_type(host)

    cephclient_debian_packages = get_variable(host, "cephclient_debian_packages")
    assert type(cephclient_debian_packages) is list

    for package_name in cephclient_debian_packages:
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
