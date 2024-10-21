from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_teleport_package(host):
    package_name = get_variable(host, "wazuh_agent_package_name")
    package = host.package(package_name)

    assert package.is_installed
