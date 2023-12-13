import pytest

from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_cephclient_install_type(host):
    if get_variable(host, "cephclient_install_type") != "container":
        pytest.skip("cephclient_install_type mismatch")


def test_dirs(host):
    check_cephclient_install_type(host)

    directories = [
        get_variable(host, "cephclient_configuration_directory"),
        get_variable(host, "cephclient_data_directory"),
        get_variable(host, "cephclient_docker_compose_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o750
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_configfile(host):
    check_cephclient_install_type(host)

    f = host.file(
        f"{get_variable(host, 'cephclient_configuration_directory')}/ceph.conf"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    with host.sudo(get_variable(host, "operator_user")):
        assert "[global]" in f.content_string


def test_keyringfile(host):
    check_cephclient_install_type(host)

    cephclient_keyring_name = get_variable(host, "cephclient_keyring_name")

    f = host.file(
        f"{get_variable(host, 'cephclient_configuration_directory')}/ceph.{cephclient_keyring_name}.keyring"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    cephclient_keyring = get_variable(host, "cephclient_keyring")
    with host.sudo(get_variable(host, "operator_user")):
        assert cephclient_keyring in f.content_string


def test_dockercompose(host):
    check_cephclient_install_type(host)

    f = host.file(
        f"{get_variable(host, 'cephclient_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    cephclient_container_name = get_variable(host, "cephclient_container_name")
    with host.sudo(get_variable(host, "operator_user")):
        assert f'container_name: "{cephclient_container_name}' in f.content_string


def test_srv(host):
    check_cephclient_install_type(host)

    cephclient_service_name = get_variable(host, "cephclient_service_name")
    service = host.service(cephclient_service_name)
    assert service.is_enabled
    assert service.is_running


def test_wrapper(host):
    check_cephclient_install_type(host)

    items = ["ceph", "ceph-authtool", "crushtool", "rados", "radosgw-admin", "rbd"]

    for item in items:
        f = host.file(f"/usr/local/bin/{item}")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o755
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert "docker exec" in f.content_string
