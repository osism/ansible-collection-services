import pytest
from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()

def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "RedHat":
        pytest.skip("ansible_os_family mismatch")


def test_repository_configuration(host):
    check_ansible_os_family(host)
    if get_variable(host, "netdata_configure_repository"):
        repo = get_variable(host, "netdata_debian_repository")
        key_file = host.file("/etc/apt/trusted.gpg.d/netdata.asc")
        key_content = get_from_url(get_variable(host, "netdata_debian_repository_key"))
        assert key_file.exists
        assert key_file.content_string == key_content
        assert host.run(f"apt-cache policy | grep {repo.split(' ')[1]}").rc == 0
