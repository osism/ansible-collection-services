from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package = host.package("wireguard-tools")
    assert package.is_installed


def test_srv(host):
    service = host.service("wg-quick@wg0.service")
    assert service.is_running
    assert service.is_enabled


def test_wireguard_config_files(host):
    with host.sudo("root"):
        f = host.file("/etc/wireguard/wg0.conf")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o400
        assert f.user == "root"
        assert f.group == "root"

        assert host.file("/etc/wireguard/server.key").exists
        assert host.file("/etc/wireguard/server.pub").exists
        assert host.file("/etc/wireguard/osism.psk").exists


def test_client_config_files(host):
    wireguard_users = get_variable(host, "wireguard_users")

    for user in wireguard_users:
        config_file_path = f"/home/{user}/wg0-{user}.conf"
        config_file = host.file(config_file_path)

        assert config_file.exists
        assert config_file.user == user
        assert config_file.group == user
        assert config_file.mode == 0o600
        assert "AllowedIPs =" in config_file.content_string
