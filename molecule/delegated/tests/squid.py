import os
import re

from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()

ROLE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "roles", "squid")
)


def render_template(host, template, network_mode, dest):
    """Render a squid role template for the given ``squid_network_mode``.

    The molecule scenario only converges the default bridge configuration, so
    the host-mode templates are rendered out-of-band here. Rendering is
    delegated to ansible (with the role defaults loaded) because the templates
    use the ``ansible.utils.ipwrap`` filter, which a plain Jinja2 environment
    does not provide.
    """
    src = os.path.join(ROLE_DIR, "templates", template)
    defaults = os.path.join(ROLE_DIR, "defaults", "main.yml")
    cmd = host.run(
        "ansible localhost -c local -i localhost, -m template "
        f'-a "src={src} dest={dest}" '
        f"-e @{defaults} -e squid_network_mode={network_mode}"
    )
    assert cmd.rc == 0, cmd.stderr
    return host.file(dest).content_string


def http_port_lines(content):
    return re.findall(r"(?m)^http_port .*$", content)


def test_required_directories(host):
    directories = [
        get_variable(host, "squid_configuration_directory"),
        f"{get_variable(host, 'squid_configuration_directory')}/conf.d",
        get_variable(host, "squid_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_configuration_files(host):
    files = ["osism.conf"]
    for file_name in files:
        file_path = (
            f"{get_variable(host, 'squid_configuration_directory')}/conf.d/{file_name}"
        )
        file = host.file(file_path)
        assert file.exists
        assert not file.is_directory
        assert file.user == get_variable(host, "operator_user")
        assert file.group == get_variable(host, "operator_group")
        assert file.mode == 0o644


def test_base_configuration_file(host):
    # The role owns /etc/squid/squid.conf so it controls the single http_port
    # listener instead of inheriting the image's stock 0.0.0.0:3128 default.
    file_path = f"{get_variable(host, 'squid_configuration_directory')}/squid.conf"
    file = host.file(file_path)
    assert file.exists
    assert not file.is_directory
    assert file.user == get_variable(host, "operator_user")
    assert file.group == get_variable(host, "operator_group")
    assert file.mode == 0o644

    content = file.content_string
    # conf.d is included so drop-in configuration (osism.conf) is still applied.
    assert "include /etc/squid/conf.d/*.conf" in content
    # Exactly one listener, and in bridge mode it stays container-internal.
    assert http_port_lines(content) == ["http_port 3128"]


def test_no_duplicate_http_port(host):
    # The base config owns the sole http_port; the conf.d drop-in must not add a
    # second one (which previously caused EADDRINUSE in host mode).
    file_path = (
        f"{get_variable(host, 'squid_configuration_directory')}/conf.d/osism.conf"
    )
    assert http_port_lines(host.file(file_path).content_string) == []


def test_docker_compose_file(host):
    docker_compose_file_path = (
        f"{get_variable(host, 'squid_docker_compose_directory')}/docker-compose.yml"
    )
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_service(host):
    service = host.service(get_variable(host, "squid_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_proxy_functionality(host):
    squid_host = get_variable(host, "squid_host")
    squid_port = get_variable(host, "squid_port")

    url = f"http://{squid_host}:{squid_port}"

    # Check if Squid is listening on the configured port
    assert host.socket(f"tcp://{squid_host}:{squid_port}").is_listening

    # Test Squid proxy with curl
    result = host.run(f"curl -v -x {squid_host}:{squid_port} https://www.osism.tech")
    assert result.rc == 0

    # Check HTTP status code
    status_code = host.run(
        f"curl -s -o /dev/null -w '%{{http_code}}' -x {squid_host}:{squid_port} https://osism.tech"
    ).stdout
    assert status_code in ["200"]

    # Check for Squid server header
    result = host.run(f"curl -I -s {url} | grep -i 'Server: squid'")
    assert result.rc == 0

    # Verify Squid is listening on its configured port
    result = host.run(f"netstat -tuln | grep :{squid_port}")
    assert result.rc == 0


def test_config_and_status(host):
    operator_user = get_variable(host, "operator_user")
    # Check Squid's status
    with host.sudo(operator_user):
        result = host.run("docker exec squid squid -k check")
        assert result.rc == 0

    # Verify Squid's configuration
    with host.sudo(operator_user):
        result = host.run("docker exec squid squid -k parse")
        assert result.rc == 0


def test_host_mode_docker_compose_render(host):
    content = render_template(
        host,
        "docker-compose.yml.j2",
        "host",
        "/tmp/molecule-squid-host-compose.yml",
    )
    # Host mode joins the host network namespace, so there is no published
    # port mapping and no dedicated bridge network.
    assert "network_mode: host" in content
    assert "ports:" not in content
    assert "networks:" not in content


def test_host_mode_squid_conf_render(host):
    content = render_template(
        host,
        "squid.conf.j2",
        "host",
        "/tmp/molecule-squid-host.conf",
    )
    squid_host = get_variable(host, "squid_host")
    squid_port = get_variable(host, "squid_port")
    # Exactly one listener, bound to the configured address rather than the
    # stock 0.0.0.0:3128 (which would be an open proxy on every interface).
    listeners = http_port_lines(content)
    assert listeners == [f"http_port {squid_host}:{squid_port}"]
    assert not any("0.0.0.0" in listener for listener in listeners)


def test_host_mode_config_parses(host):
    # Rendering the host-mode base config with the default squid_port and
    # parsing it in squid would have caught the duplicate-http_port regression.
    dest = "/tmp/molecule-squid-host.conf"
    render_template(host, "squid.conf.j2", "host", dest)
    operator_user = get_variable(host, "operator_user")
    with host.sudo(operator_user):
        assert host.run(f"docker cp {dest} squid:/tmp/squid-host.conf").rc == 0
        result = host.run("docker exec squid squid -k parse -f /tmp/squid-host.conf")
        assert result.rc == 0, result.stderr
