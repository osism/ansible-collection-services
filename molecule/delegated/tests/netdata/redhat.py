import pytest
from ..util.util import get_ansible, get_variable, get_from_url, get_centos_repo_key

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_netdata_lib64_directory(host):
    check_ansible_os_family(host)

    lib_dir = host.file("/usr/lib64/netdata/conf.d")

    assert lib_dir.exists
    assert lib_dir.is_directory


def test_osquery_gpgkey(host):
    check_ansible_os_family(host)

    netdata_configure_repository = get_variable(host, "netdata_configure_repository")

    if not netdata_configure_repository:
        pytest.skip("netdata_configure_repository is not true")

    # Fetch the GPG key content from the osquery URL defined in Ansible variables
    url = get_variable(host, "netdata_redhat_repository_key")
    key_content = get_from_url(url)

    # Use the get_centos_repo_key function with the appropriate summary for osquery
    installed_key = get_centos_repo_key(
        host,
        "(https://packagecloud.io/docs#gpg_signing) <support@packagecloud.io> public key",
    )

    # Verify that the installed key matches the fetched key
    assert installed_key in key_content
