from .util.util import get_ansible

testinfra_runner, testinfra_hosts = get_ansible()


def test_sshd_service_running_and_enabled(host):
    service = host.service("sshd")
    assert service.is_running, "Service sshd should be running"
    assert service.is_enabled, "Service sshd should be enabled"
