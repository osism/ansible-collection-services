from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_sshd_service_running_and_enabled(host):
    service = host.service("sshd")
    assert service.is_running, "Service sshd should be running"
    assert service.is_enabled, "Service sshd should be enabled"


def test_sshd_access_config(host):
    f = host.file("/etc/ssh/sshd_config.d/99-osism.conf")
    assert f.exists
    assert not f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644

    sshd_deny_users = get_variable(host, "sshd_deny_users")
    sshd_allow_users = get_variable(host, "sshd_allow_users")
    assert f"DenyUsers {' '.join(sshd_deny_users)}" in f.content_string
    assert f"AllowUsers {' '.join(sshd_allow_users)}" in f.content_string


def test_sshd_effective_config(host):
    with host.sudo():
        result = host.run("/usr/sbin/sshd -T")
        assert result.rc == 0

    lines = result.stdout.splitlines()
    for pattern in get_variable(host, "sshd_deny_users"):
        assert f"denyusers {pattern}" in lines
    for pattern in get_variable(host, "sshd_allow_users"):
        assert f"allowusers {pattern}" in lines
