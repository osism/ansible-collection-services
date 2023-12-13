from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_configfile(host):
    f = host.file("/etc/systemd/journald.conf")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"

    journald_SystemMaxUse = get_variable(host, "journald_SystemMaxUse")
    assert f"SystemMaxUse={journald_SystemMaxUse}" in f.content_string


def test_srv(host):
    service = host.service(get_variable(host, "journald_service_name"))

    assert service.is_running
    assert service.is_enabled
