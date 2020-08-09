import pytest


def test_rsyslog_package(host):
    p = host.package("rsyslog")
    assert p.is_installed


def test_rsyslog_service(host):
    f = host.service("rsyslog")
    assert f.is_running
    assert f.is_enabled
