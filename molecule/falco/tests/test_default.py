import pytest


def test_falco_package(host):
    p = host.package("falco")
    assert p.is_installed


def test_falco_service(host):
    f = host.service("falco")
    assert f.is_running
    assert f.is_enabled


def test_falco_kernel_module(host):
    c = host.run("lsmod | grep -i falco")
    assert "falco" in c.stdout
    assert c.succeeded
