import pytest


def test_osquery_package(host):
    p = host.package("osquery")
    assert p.is_installed


def test_osqueryd_service(host):
    f = host.service("osqueryd")
    assert f.is_running
    assert f.is_enabled
