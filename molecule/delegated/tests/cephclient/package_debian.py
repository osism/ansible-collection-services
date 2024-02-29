import pytest

from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def check_cephclient_install_type(host):
    if get_variable(host, "cephclient_install_type") != "package":
        pytest.skip("cephclient_install_type mismatch")


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_gpg_key(host):
    check_cephclient_install_type(host)
    check_ansible_os_family(host)

    cephclient_configure_repository = get_variable(
        host, "cephclient_configure_repository"
    )

    if not cephclient_configure_repository:
        pytest.skip("cephclient_configure_repository not configured")

    cephclient_repository_key_url = get_variable(host, "cephclient_repository_key")

    # Fetch the GPG key content from the URL
    key_content = get_from_url(cephclient_repository_key_url)

    # Validate the permissions and ownership of the GPG key file
    key_file = host.file("/etc/apt/trusted.gpg.d/cephclient.asc")
    assert key_file.exists
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content
