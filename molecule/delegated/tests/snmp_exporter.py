from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_snmp_exporter_directories_created(host):
    directories = [
        get_variable(host, "snmp_exporter_docker_compose_directory"),
        get_variable(host, "snmp_exporter_configuration_directory"),
    ]
    operator_user = get_variable(host, "operator_user")
    operator_group = get_variable(host, "operator_group")

    for directory in directories:
        dir = host.file(directory)
        assert dir.exists, f"Directory {directory} should exist"
        assert dir.is_directory, f"{directory} should be a directory"
        assert dir.user == operator_user
        assert dir.group == operator_group
        assert dir.mode == 0o750, f"Directory {directory} should have 0750 permissions"


def test_snmp_exporter_docker_compose_file(host):
    snmp_exporter_docker_compose_directory = get_variable(
        host, "snmp_exporter_docker_compose_directory"
    )
    docker_compose_file = host.file(
        f"{snmp_exporter_docker_compose_directory}/docker-compose.yml"
    )

    assert (
        docker_compose_file.exists
    ), "docker-compose.yml for snmp_exporter should exist"
    assert docker_compose_file.is_file, "docker-compose.yml should be a file"
    assert docker_compose_file.user == get_variable(host, "operator_user"), (
        "docker-compose.yml should be " "owned by the operator user"
    )
    assert docker_compose_file.group == get_variable(host, "operator_group"), (
        "docker-compose.yml should be " "in the operator group"
    )
    assert (
        docker_compose_file.mode == 0o640
    ), "docker-compose.yml should have 0640 permissions"


def test_snmp_exporter_service_running(host):
    snmp_exporter_service_name = get_variable(host, "snmp_exporter_service_name")
    service = host.service(snmp_exporter_service_name)
    assert service.is_enabled
    assert service.is_running


def _listen_address(host):
    host_addr = get_variable(host, "snmp_exporter_host")
    port = get_variable(host, "snmp_exporter_port")
    # ipwrap brackets IPv6 literals in the rendered flag, and ss reports them
    # the same way.
    if ":" in host_addr:
        return f"[{host_addr}]:{port}", port
    return f"{host_addr}:{port}", port


def test_snmp_exporter_listen_address_flag(host):
    snmp_exporter_docker_compose_directory = get_variable(
        host, "snmp_exporter_docker_compose_directory"
    )
    expected, _ = _listen_address(host)

    docker_compose_file = host.file(
        f"{snmp_exporter_docker_compose_directory}/docker-compose.yml"
    )
    assert f"--web.listen-address={expected}" in docker_compose_file.content_string


def test_snmp_exporter_listening(host):
    expected, port = _listen_address(host)

    # is_listening against a wildcard bind also succeeds for loopback
    # connections, and snmp_exporter falls back to [::]:9116 (dual-stack)
    # without --web.listen-address, so neither is_listening nor a
    # "not 0.0.0.0" check would notice the flag being ignored. Assert every
    # address actually bound on the port matches snmp_exporter_host exactly.
    local_addrs = [
        line.split()[3]
        for line in host.check_output(f"ss -ltnH 'sport = :{port}'").splitlines()
        if line.strip()
    ]
    assert local_addrs, f"nothing is listening on port {port}"
    for addr in local_addrs:
        assert addr == expected, f"snmp_exporter bound to {addr}, expected {expected}"
