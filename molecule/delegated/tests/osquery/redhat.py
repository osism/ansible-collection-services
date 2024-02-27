import pytest
from ..util.util import get_ansible, get_variable, get_from_url, get_centos_repo_key

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_osquery_gpgkey(host):
    check_ansible_os_family(host)

    osquery_configure_repository = get_variable(host, "osquery_configure_repository")

    if not osquery_configure_repository:
        pytest.skip("osquery_configure_repository is not true")

    # Fetch the GPG key content from the osquery URL defined in Ansible variables
    url = get_variable(host, "osquery_redhat_repository_key")
    key_content = get_from_url(url)

    # Use the get_centos_repo_key function with the appropriate summary for osquery
    installed_key = get_centos_repo_key(
        host, "osquery (osquery) <osquery@fb.com> public key"
    )

    # Verify that the installed key matches the fetched key
    assert installed_key in key_content
