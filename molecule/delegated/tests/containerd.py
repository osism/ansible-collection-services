import pytest

from .util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def test_configfile(host):
    f = host.file("/etc/containerd/config.toml")

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o660

    containerd_grpc_gid = get_variable(host, "containerd_grpc_gid")
    with host.sudo("root"):
        content = host.check_output("cat /etc/containerd/config.toml")
        assert f"gid = {containerd_grpc_gid}" in content


def test_srv(host):
    service = host.service(get_variable(host, "containerd_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_failpkg(host):
    package_names = get_variable(host, "containerd_packages_fail")
    assert type(package_names) is list

    for package_name in package_names:
        package = host.package(package_name)
        assert not package.is_installed


def test_repo(host):
    docker_configure_repository = get_variable(host, "docker_configure_repository")

    if not docker_configure_repository:
        pytest.skip("docker_configure_repository is not true")

    package = host.package("apt-transport-https")
    assert package.is_installed

    key_content = get_from_url(get_variable(host, "docker_debian_repository_key"))

    f = host.file("/etc/apt/trusted.gpg.d/docker.asc")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f.content_string == key_content


def test_pkg(host):
    package = host.package(get_variable(host, "containerd_package_name"))
    assert package.is_installed
