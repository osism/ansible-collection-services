from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package_name = get_variable(host, "bird_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_conffile(host):
    with host.sudo("bird"):
        f = host.file("/etc/bird/bird.conf")
        assert f.exists
        assert not f.is_directory
        assert f.user == "bird"
        assert f.group == "bird"
        assert f.mode == 0o640

        bird_cidr = get_variable(host, "bird_cidr")
        assert f"if net ~ [ {bird_cidr}+ ] then " in f.content_string


def test_sysctl(host):
    bird_sysctl = get_variable(host, "bird_sysctl")

    assert type(bird_sysctl) is list

    for element in bird_sysctl:
        assert host.sysctl(f"{element['name']}") == element["value"]


def test_srv(host):
    service = host.service(get_variable(host, "bird_service_name"))

    assert service.is_running
    assert service.is_enabled
