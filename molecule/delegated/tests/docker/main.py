import pytest

from ..util.util import (
    get_ansible,
    get_variable,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_docker_filesystem(host):
    docker_configure_storage_block_device = get_variable(
        host, "docker_configure_storage_block_device"
    )

    if not docker_configure_storage_block_device:
        pytest.skip("docker_configure_storage_block_device is not true")

    mountPoint = host.mount_point("/var/lib/docker")

    assert mountPoint.exists
    assert mountPoint.filesystem == get_variable(host, "docker_storage_filesystem")
    assert mountPoint.device == get_variable(host, "docker_storage_block_device")

    f = host.file("/var/lib/docker")

    assert f.exists
    assert f.is_directory
    assert f.mode == 0o711
    assert f.user == "root"
    assert f.group == "root"


def test_docker_directories(host):
    docker_service_name = get_variable(host, "docker_service_name")
    directories = [
        "/etc/docker/plugins",
        f"/etc/systemd/system/{docker_service_name}.service.d",
        "/etc/ansible/facts.d",
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o755
        assert f.user == "root"
        assert f.group == "root"


def test_docker_configuration_files(host):
    docker_service_name = get_variable(host, "docker_service_name")

    f = host.file(f"/etc/systemd/system/{docker_service_name}.service.d/overlay.conf")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert "ExecStart=/usr/bin/dockerd" in f.content_string

    f = host.file("/etc/security/limits.d/docker.conf")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert "root soft nofile 65536" in f.content_string

    docker_storage_driver = get_variable(host, "docker_storage_driver")
    f = host.file("/etc/docker/daemon.json")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f'"storage-driver": "{docker_storage_driver}",' in f.content_string


def test_docker_service(host):
    service = host.service(get_variable(host, "docker_service_name"))

    assert service.is_running
    assert service.is_enabled

    service = host.service(get_variable(host, "docker_service_name") + ".socket")

    assert service.is_running
    assert service.is_enabled

    docker_manage_containerd = get_variable(host, "docker_manage_containerd")
    if docker_manage_containerd:
        service = host.service(get_variable(host, "containerd_service_name"))

        assert service.is_running
        assert service.is_enabled


def test_docker_user(host):
    username = get_variable(host, "docker_user")
    if username == "{{ operator_user | default('dragon') }}":
        try:
            username = get_variable(host, "operator_user")
        except Exception:
            username = "dragon"

    user = host.user(username)

    assert user.exists
    assert "docker" in user.groups


def test_docker_fact(host):
    docker_fact_files = get_variable(host, "docker_fact_files")
    assert type(docker_fact_files) is list

    for item in docker_fact_files:
        f = host.file(f"/etc/ansible/facts.d/{item}.fact")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o755
        assert f.user == "root"
        assert f.group == "root"
        assert f.content_string != ""


def test_docker_failpkg(host):
    package_names = get_variable(host, "docker_packages_fail")
    assert type(package_names) is list

    for package_name in package_names:
        package = host.package(package_name)
        assert not package.is_installed


def test_docker_containerd(host):
    docker_manage_containerd = get_variable(host, "docker_manage_containerd")

    if not docker_manage_containerd:
        pytest.skip("docker_manage_containerd is not true")

    package = host.package(get_variable(host, "containerd_package_name"))
    assert package.is_installed


def test_docker_python(host):
    docker_python_install_from_pip = (
        get_variable(host, "docker_python_install_from_pip") is True
    )

    docker_python3_package_name = get_variable(host, "docker_python3_package_name")
    docker_python_package_name = get_variable(host, "docker_python_package_name")
    docker_python_package_names = get_variable(host, "docker_python_package_names")
    docker_python_package_names = jinja_list_concat(
        None, [[docker_python3_package_name], [docker_python_package_name]]
    )

    if not docker_python_install_from_pip:
        for item in docker_python_package_names:
            f = host.file(f"/etc/apt/preferences.d/{item}")
            assert not f.exists

        package = host.package(docker_python3_package_name)
        assert package.is_installed
    else:
        for item in docker_python_package_names:
            package = host.package(item)
            assert not package.is_installed

        for item in docker_python_package_names:
            f = host.file(f"/etc/apt/preferences.d/{item}")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o644
            assert "Pin-Priority: -1" in f.content_string

        package = host.package("python3-pip")
        assert package.is_installed


def test_docker_login(host):
    try:
        docker_registry_username = get_variable(host, "docker_registry_username")
        docker_registry_password = get_variable(host, "docker_registry_password")
    except Exception:
        pytest.skip("docker registry credentials not defined")

    if docker_registry_username == "" or docker_registry_password == "":
        pytest.skip("docekr registry credentials empty")

    package = host.package("gnupg2")
    assert package.is_installed

    package = host.package("pass")
    assert package.is_installed


@pytest.mark.parametrize(
    "name,image,expected_output",
    [("docker_test", "docker.io/hello-world:latest", "Hello from Docker!")],
)
def test_docker_usability(host, name, image, expected_output):
    # Check Docker version
    docker_version = host.run("docker --version")
    assert docker_version.rc == 0
    assert "docker version" in docker_version.stdout.lower()

    # Run a test container and check if Docker can list images
    with host.sudo(get_variable(host, "operator_user")):
        container = host.run(f"docker run --name {name} {image}")
        list_images = host.run("docker images")
    assert container.rc == 0
    assert expected_output in container.stdout
    assert list_images.rc == 0
