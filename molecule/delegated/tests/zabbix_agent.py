from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_zabbix_agent_service(host):
    service = host.service(get_variable(host, "zabbix_agent_service_name"))

    assert service.is_running
    assert service.is_enabled
