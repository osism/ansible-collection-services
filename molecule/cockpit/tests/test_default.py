import pytest


def test_cockpit_client_packages(host):
    p = host.package("cockpit-storaged")
    assert p.is_installed
