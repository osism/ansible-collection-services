from ..util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_zabbix_agent_service_and_version(host):
    service = host.service(get_variable(host, "zabbix_agent_service_name"))

    assert service.is_running
    assert service.is_enabled

    with host.sudo("zabbix"):
        cmd = host.run("zabbix_agent2 -V")
    assert cmd.rc == 0
    assert "zabbix_agent2" in cmd.stdout


def test_zabbix_agent_config(host):
    config_file = get_variable(host, "zabbix_agent_configuration_file")
    f = host.file(f"/etc/zabbix/{config_file}")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644

    content = f.content_string
    assert f'ListenPort={get_variable(host, "zabbix_agent_port")}' in content
    assert f'Server={get_variable(host, "zabbix_agent_server")}' in content


def test_zabbix_agent_function(host):
    # Verify zabbix_agent is listening on its configured port
    zabbix_agent_port = get_variable(host, "zabbix_agent_port")
    result = host.run(f"netstat -tuln | grep :{zabbix_agent_port}")
    assert result.rc == 0
