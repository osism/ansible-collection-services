import pytest

from ..util.util import (
    get_ansible,
    get_centos_repo_key,
    get_family_role_variable,
    get_variable,
    get_from_url,
    jinja_replacement,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_repo(host):
    check_ansible_os_family(host)

    docker_configure_repository = get_variable(host, "docker_configure_repository")

    if not docker_configure_repository:
        pytest.skip("docker_configure_repository is not true")

    key_content = get_from_url("https://download.docker.com/linux/centos/gpg")
    installed_key = get_centos_repo_key(
        host, "Docker Release (CE rpm) <docker@docker.com> public key"
    )
    assert installed_key in key_content

    repo_file = host.file("/etc/yum.repos.d/docker-ce.repo")
    assert repo_file.exists
    assert not repo_file.is_directory
    assert repo_file.contains("download.docker.com/linux")


def test_pkg(host):
    check_ansible_os_family(host)

    docker_package_name = get_variable(host, "docker_package_name")
    docker_cli_package_name = get_variable(host, "docker_cli_package_name")
    docker_cli_package_name = jinja_replacement(
        docker_cli_package_name, {"docker_package_name": docker_package_name}
    )

    docker_version = get_family_role_variable(host, "docker_version")
    docker_cli_version = docker_version

    with host.sudo("root"):
        f = host.file("/etc/dnf/plugins/versionlock.list")
        assert f.exists
        assert not f.is_directory
        assert docker_package_name in f.content_string
        assert docker_cli_package_name in f.content_string
        assert docker_version in f.content_string
        assert docker_cli_version in f.content_string

    if ":" in docker_cli_version:
        docker_cli_version = docker_cli_version.split(":")[1]

    package = host.package(docker_cli_package_name)
    assert package.is_installed
    assert docker_cli_version in package.version

    if ":" in docker_version:
        docker_version = docker_version.split(":")[1]

    package = host.package(docker_package_name)
    assert package.is_installed
    assert docker_version in package.version
