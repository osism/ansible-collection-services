import pytest

from ..util.util import (
    get_ansible,
    get_family_role_variable,
    get_variable,
    get_from_url,
    jinja_replacement,
)

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_repo(host):
    check_ansible_os_family(host)

    docker_configure_repository = get_variable(host, "docker_configure_repository")

    if not docker_configure_repository:
        pytest.skip("docker_configure_repository is not true")

    package = host.package("apt-transport-https")
    assert package.is_installed

    if get_variable(host, "ansible_os_family", True) == "Debian":
        key_content = get_from_url("https://download.docker.com/linux/debian/gpg")
    elif get_variable(host, "ansible_os_family", True) == "Ubuntu":
        key_content = get_from_url("https://download.docker.com/linux/ubuntu/gpg")

    f = host.file("/etc/apt/trusted.gpg.d/docker.asc")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f.content_string == key_content


def test_pkg(host):
    check_ansible_os_family(host)
    f = host.file("/etc/apt/preferences.d/docker")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert "Pin-Priority: 1001" in f.content_string

    f = host.file("/etc/apt/preferences.d/docker-cli")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert "Pin-Priority: 1001" in f.content_string

    docker_package_name = get_variable(host, "docker_package_name")
    docker_cli_package_name = get_variable(host, "docker_cli_package_name")
    docker_cli_package_name = jinja_replacement(
        docker_cli_package_name, {"docker_package_name": docker_package_name}
    )

    docker_cli_version = get_family_role_variable(host, "docker_cli_version")

    package = host.package(docker_cli_package_name)
    assert package.is_installed
    assert docker_cli_version in package.version

    docker_version = get_family_role_variable(host, "docker_version")

    package = host.package(docker_package_name)
    assert package.is_installed
    assert docker_version in package.version
