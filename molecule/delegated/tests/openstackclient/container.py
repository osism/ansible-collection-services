import pytest
from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def check_openstackclient_install_type(host):
    if get_variable(host, "openstackclient_install_type") != "container":
        pytest.skip("openstackclient_install_type mismatch")


def test_openstackclient_directories(host):
    check_openstackclient_install_type(host)

    directories = [
        get_variable(host, "openstackclient_configuration_directory"),
        get_variable(host, "openstackclient_data_directory"),
        get_variable(host, "openstackclient_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_docker_compose_file(host):
    check_openstackclient_install_type(host)

    docker_compose_file_path = f"{get_variable(host, 'openstackclient_docker_compose_directory')}/docker-compose.yml"
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_openstackclient_service(host):
    check_openstackclient_install_type(host)

    service = host.service(get_variable(host, "openstackclient_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_openstack_wrapper_script(host):
    check_openstackclient_install_type(host)

    wrapper_script_path = "/usr/local/bin/openstack"
    wrapper_script = host.file(wrapper_script_path)
    assert wrapper_script.exists
    assert wrapper_script.user == get_variable(host, "operator_user")
    assert wrapper_script.group == get_variable(host, "operator_group")
    assert wrapper_script.mode == 0o755


def test_ospurge_script_removed(host):
    check_openstackclient_install_type(host)

    ospurge_script = host.file("/usr/local/bin/ospurge")
    assert not ospurge_script.exists


def test_bash_completion_script(host):
    check_openstackclient_install_type(host)

    bash_completion_script = host.file("/etc/bash_completion.d/openstack")
    assert bash_completion_script.exists
    assert bash_completion_script.user == "root"
    assert bash_completion_script.group == "root"
    assert bash_completion_script.mode == 0o644
