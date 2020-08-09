import pytest


def test_sysdig_package(host):
    p = host.package("sysdig")
    assert p.is_installed


def test_sysdig_probe_kernel_module(host):
    c = host.run("lsmod | grep -i sysdig_probe")
    assert "sysdig_probe" in c.stdout
    assert c.succeeded
