from ..util.util import get_ansible, get_variable, jinja_replacement

testinfra_runner, testinfra_hosts = get_ansible()


def test_function(host):
    status = host.run("ceph --version")
    assert status.rc == 0
    # cephclient_version now defaults to "{{ ceph_version }}"; include_vars loads
    # it unrendered, so resolve it against ceph_version like other templated vars.
    cephclient_version = jinja_replacement(
        get_variable(host, "cephclient_version"),
        {"ceph_version": get_variable(host, "ceph_version")},
    )
    assert cephclient_version.lower() in status.stdout.lower()
