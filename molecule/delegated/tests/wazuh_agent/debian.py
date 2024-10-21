import pytest
from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_wazuh_agent_repository(host):
    check_ansible_os_family(host)

    wazuh_agent_configure_repository = get_variable(
        host, "wazuh_agent_configure_repository"
    )

    if not wazuh_agent_configure_repository:
        pytest.skip("wazuh_agent_configure_repository is not true")

    package = host.package("apt-transport-https")
    assert package.is_installed

    key_file = host.file("/etc/apt/trusted.gpg.d/wazuh_agent.asc")
    key_content = get_from_url(get_variable(host, "wazuh_agent_debian_repository_key"))

    assert key_file.exists
    assert not key_file.is_directory
    assert key_file.user == "root"
    assert key_file.group == "root"
    assert key_file.mode == 0o644
    assert key_file.content_string == key_content
