import pytest

from ..util.util import get_ansible, get_variable, get_from_url

testinfra_runner, testinfra_hosts = get_ansible()


def check_ansible_os_family(host):
    if get_variable(host, "ansible_os_family", True) != "Debian":
        pytest.skip("ansible_os_family mismatch")


def test_gpgkey(host):
    check_ansible_os_family(host)

    falco_configure_repository = get_variable(host, "falco_configure_repository")

    if not falco_configure_repository:
        pytest.skip("falco_configure_repository is not true")

    url = get_variable(host, "falco_repository_key")
    key_content = get_from_url(url)

    f = host.file("/etc/apt/trusted.gpg.d/falco.asc")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f.content_string == key_content


def test_pkg(host):
    check_ansible_os_family(host)

    package_name = get_variable(host, "falco_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_kernelmodfile(host):
    check_ansible_os_family(host)

    f = host.file("/etc/modules-load.d/falco.conf")
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o644
    assert f.user == "root"
    assert f.group == "root"
    assert f.content_string == "falco"


def test_kernelmod(host):
    check_ansible_os_family(host)

    with host.sudo():
        loaded_modules = host.check_output("lsmod").splitlines()

    assert any("falco" in line for line in loaded_modules)


def test_srv(host):
    check_ansible_os_family(host)

    service = host.service(get_variable(host, "falco_service_name"))

    assert service.is_running
    assert service.is_enabled
