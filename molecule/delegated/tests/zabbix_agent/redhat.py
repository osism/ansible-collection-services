import pytest
from ..util.util import get_ansible, get_variable, get_from_url, get_centos_repo_key

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_zabbix_agent_repository(host):
    check_ansible_os_family(host)

    zabbix_agent_configure_repository = get_variable(
        host, "zabbix_agent_configure_repository"
    )

    if not zabbix_agent_configure_repository:
        pytest.skip("zabbix_agent_configure_repository is not true")

    key_content = get_from_url(get_variable(host, "zabbix_agent_redhat_repository_key"))
    installed_key = get_centos_repo_key(
        host, "Zabbix LLC (Jul 2022) <packager@zabbix.com> public key"
    )
    assert installed_key in key_content

    zabbix_agent_version = get_variable(host, "zabbix_agent_version")
    ansible_distribution = get_variable(host, "ansible_distribution", True)
    distribution_version = get_variable(
        host, "ansible_distribution_major_version", True
    )
    repository_arch = get_variable(host, "zabbix_agent_redhat_repository_arch")

    repo_file = host.file(
        f"/etc/yum.repos.d/repo.zabbix.com_zabbix_{zabbix_agent_version}_{ansible_distribution.lower()}_"
        f"{distribution_version}_{repository_arch}.repo"
    )
    assert repo_file.exists
    assert not repo_file.is_directory
    assert repo_file.contains("baseurl=https://repo.zabbix.com/zabbix/")
