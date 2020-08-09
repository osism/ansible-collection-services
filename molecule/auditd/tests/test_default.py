import pytest


def test_auditd_package(host):
    p = host.package("auditd")
    assert p.is_installed


def test_audispd_plugins_package(host):
    p = host.package("audispd-plugins")
    assert p.is_installed


def test_auditd_service(host):
    f = host.service("auditd")
    assert f.is_running
    assert f.is_enabled
