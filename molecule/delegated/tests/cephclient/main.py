from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_function(host):
    status = host.run("ceph --version")
    assert status.rc == 0
    assert get_variable(host, "cephclient_version").lower() in status.stdout.lower()
