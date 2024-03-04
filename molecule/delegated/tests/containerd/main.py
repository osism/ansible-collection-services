from ..util.util import get_ansible, get_variable

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


def test_pkg(host):
    package = host.package(get_variable(host, "containerd_package_name"))
    assert package.is_installed
