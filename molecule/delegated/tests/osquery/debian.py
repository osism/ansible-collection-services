import pytest
from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()

def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_apt_transport_https_package_installed(host):
    check_ansible_os_family(host)
    osquery_configure_repository = get_variable(host, "osquery_configure_repository")
    if osquery_configure_repository:
        apt_transport_https_package = host.package("apt-transport-https")
        assert apt_transport_https_package.is_installed


def test_osquery_gpgkey(host):
    check_ansible_os_family(host)
    osquery_configure_repository = get_variable(host, "osquery_configure_repository")

    if not osquery_configure_repository:
        pytest.skip("osquery_configure_repository is not true")

    url = get_variable(host, "osquery_debian_repository_key")
    key_content = get_from_url(url)

    # cut first 4 lines of key_content because of unpredictable changes of comment and version in it
    key_content_modified = "\n".join(key_content.split("\n")[4:])

    gpg_key_file = host.file("/etc/apt/trusted.gpg.d/osquery.asc")

    assert gpg_key_file.exists
    assert not gpg_key_file.is_directory
    assert gpg_key_file.mode == 0o644
    assert gpg_key_file.user == "root"
    assert gpg_key_file.group == "root"
    assert key_content_modified in gpg_key_file.content_string
