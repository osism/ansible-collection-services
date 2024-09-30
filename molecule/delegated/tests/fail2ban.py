from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_fail2ban_service(host):
    service = host.service(get_variable(host, "fail2ban_service_name"))

    assert service.is_running
    assert service.is_enabled


def test_fail2ban_package(host):
    package_name = get_variable(host, "fail2ban_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_function(host):
    with host.sudo():
        result = host.run("fail2ban-client status")
        assert result.rc == 0
        assert "Jail list:" in result.stdout
        assert "sshd" in result.stdout
