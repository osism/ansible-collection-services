import pytest

from ..util.util import get_ansible, get_variable, get_from_url, get_dist_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_repo(host):
    check_ansible_os_family(host)
    containerd_configure_repository = get_variable(
        host, "containerd_configure_repository"
    )

    if not containerd_configure_repository:
        pytest.skip("containerd_configure_repository is not true")

    key_content = get_from_url(get_dist_role_variable(host, "__docker_repository_key"))

    f = host.file("/etc/apt/trusted.gpg.d/docker.asc")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f.content_string == key_content
