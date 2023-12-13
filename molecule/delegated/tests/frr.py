from .util.util import get_ansible, get_variable, jinja_list_concat

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package_name = get_variable(host, "frr_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_daemonfile(host):
    with host.sudo("frr"):
        f = host.file("/etc/frr/daemons")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o640
        assert f.user == "frr"
        assert f.group == "frr"

        content = host.check_output("cat /etc/frr/daemons")
        assert "This file tells the frr package which daemons to start." in content


def test_configfile(host):
    with host.sudo("frr"):
        f = host.file("/etc/frr/frr.conf")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o640
        assert f.user == "frr"
        assert f.group == "frr"

        content = host.check_output("cat /etc/frr/frr.conf")
        assert "frr defaults traditional" in content


def test_sysctl_settings(host):
    assert host.file("/etc/sysctl.d/50-frr.conf").exists

    frr_sysctl_defaults = get_variable(host, "frr_sysctl_defaults")
    frr_sysctl_extra = get_variable(host, "frr_sysctl_extra")
    frr_sysctl = get_variable(host, "frr_sysctl")

    frr_sysctl = jinja_list_concat(frr_sysctl, [frr_sysctl_defaults, frr_sysctl_extra])

    for item in frr_sysctl:
        sysctl_name = item["name"]
        expected_value = str(item["value"])

        sysctl_path = f"/proc/sys/{sysctl_name.replace('.', '/')}"

        if host.file(sysctl_path).exists:
            actual_value = host.file(sysctl_path).content_string.strip()
            assert actual_value == expected_value


def test_srv(host):
    service = host.service(get_variable(host, "frr_service_name"))

    assert service.is_running
    assert service.is_enabled
