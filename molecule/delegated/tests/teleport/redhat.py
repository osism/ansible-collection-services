import pytest
from ..util.util import get_ansible, get_variable, get_from_url, get_centos_repo_key

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_teleport_repository(host):
    check_ansible_os_family(host)

    teleport_configure_repository = get_variable(host, "teleport_configure_repository")

    if not teleport_configure_repository:
        pytest.skip("teleport_configure_repository is not true")

    key_content = get_from_url(get_variable(host, "teleport_redhat_repository_key"))
    installed_key = get_centos_repo_key(
        host, "Gravitational, Inc <info@gravitational.com> public key"
    )
    assert installed_key in key_content

    repo_file = host.file("/etc/yum.repos.d/teleport.repo")
    assert repo_file.exists
    assert not repo_file.is_directory
    assert repo_file.contains("https://yum.releases.teleport.dev")
