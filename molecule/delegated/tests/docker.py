import pytest

from .util.util import (
    get_ansible,
    get_variable,
    get_from_url,
    jinja_replacement,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_filesystem(host):
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


def test_dirs(host):
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


def test_configfile(host):
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


def test_srv(host):
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


def test_user(host):
    username = get_variable(host, "docker_user")
    if username == "{{ operator_user | default('dragon') }}":
        try:
            username = get_variable(host, "operator_user")
        except Exception:
            username = "dragon"

    user = host.user(username)

    assert user.exists
    assert "docker" in user.groups


def test_fact(host):
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


def test_failpkg(host):
    package_names = get_variable(host, "docker_packages_fail")
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


def test_containerd(host):
    docker_manage_containerd = get_variable(host, "docker_manage_containerd")

    if not docker_manage_containerd:
        pytest.skip("docker_manage_containerd is not true")

    package = host.package(get_variable(host, "containerd_package_name"))
    assert package.is_installed


def test_pkg(host):
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

    package = host.package(docker_cli_package_name)
    assert package.is_installed
    assert get_variable(host, "docker_version") in package.version

    package = host.package(docker_package_name)
    assert package.is_installed
    assert get_variable(host, "docker_version") in package.version


def test_python(host):
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


def test_dockerlogin(host):
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
