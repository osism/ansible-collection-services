from ..util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_function(host):
    result = host.run("openstack --version")
    assert result.rc == 0
    assert "openstack" in result.stdout
