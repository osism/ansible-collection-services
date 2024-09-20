import pytest

from ..util.util import get_ansible, get_variable, get_family_role_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_srv(host):
    service_name = get_family_role_variable(host, "chrony_service_name")
    service = host.service(service_name)
    assert service.is_enabled
    assert service.is_running


def test_pkg(host):
    package_name = get_variable(host, "chrony_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_configfile(host):
    try:
        file_path = get_variable(host, "chrony_conf_file")
    except Exception:
        try:
            file_path = get_family_role_variable(host, "chrony_conf_file")
        except Exception:
            pytest.skip("chrony_conf_file not defined")

    f = host.file(file_path)
    if not f.exists:
        pytest.skip("No existing config file")

    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644

    chrony_servers = get_variable(host, "chrony_servers")
    content = f.content_string

    for server in chrony_servers:
        assert f"server {server}" in content


def test_chrony_servers_reachable(host):
    """Check if chrony servers are reachable"""

    chrony_servers = get_variable(host, "chrony_servers")
    assert isinstance(chrony_servers, list)
    assert len(chrony_servers) > 0

    for server in chrony_servers:
        # Resolve the hostname to an IP address
        cmd_resolve = host.run(f"dig +short {server}")
        assert cmd_resolve.rc == 0
        ip_addresses = cmd_resolve.stdout.strip().split("\n")

        assert len(ip_addresses) > 0

        # Check if at least one IP address is reachable
        reachable = False
        for ip in ip_addresses:
            cmd_ping = host.run(f"ping -c 1 -W 2 {ip}")
            if cmd_ping.rc == 0:
                reachable = True
                break

        assert reachable

        # Check if the NTP port is open
        cmd_ntp = host.run(f"nc -zu -w 2 {server} 123")
        assert cmd_ntp.rc == 0


def test_chrony_status(host):
    """Check chrony status and sources."""

    cmd = host.run("chronyc sources")
    assert cmd.rc == 0

    # Check if there are any reachable sources
    assert "^*" in cmd.stdout or "^+" in cmd.stdout

    cmd = host.run("chronyc tracking")
    assert cmd.rc == 0

    # Check if system clock is synchronized
    assert "Leap status     : Not synchronised" not in cmd.stdout
