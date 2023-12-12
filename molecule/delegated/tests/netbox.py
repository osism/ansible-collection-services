import pytest
from .util.util import get_ansible, get_variable
from pathlib import Path

testinfra_runner, testinfra_hosts = get_ansible()


def test_config_dirs(host):
    directories = [
        get_variable(host, "netbox_docker_compose_directory"),
        get_variable(host, "netbox_configuration_directory"),
        get_variable(host, "netbox_secrets_directory"),
    ]

    for d in directories:
        d = host.file(d)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")


def test_postgres_config(host):
    config_dir = get_variable(host, "netbox_configuration_directory")

    postgres_env = host.file(f"{config_dir}/postgres.env")
    assert postgres_env.exists
    assert not postgres_env.is_directory
    assert postgres_env.mode == 0o640
    assert postgres_env.user == get_variable(host, "operator_user")
    assert postgres_env.group == get_variable(host, "operator_group")
    assert (
        "POSTGRES_PASSWORD_FILE=/run/secrets/POSTGRES_PASSWORD"
        in postgres_env.content_string
    )

    secrets_dir = get_variable(host, "netbox_secrets_directory")
    postgres_pw = host.file(f"{secrets_dir}/POSTGRES_PASSWORD")
    assert postgres_pw.exists
    assert not postgres_pw.is_directory
    assert postgres_pw.mode == 0o644
    assert postgres_pw.user == get_variable(host, "operator_user")
    assert postgres_pw.group == get_variable(host, "operator_group")
    assert (
        f'{get_variable(host, "netbox_postgres_password")}'
        in postgres_pw.content_string
    )

    entrypoint = host.file(f"{config_dir}/docker-entrypoint-initdb.d")
    assert entrypoint.exists
    assert entrypoint.is_directory
    assert entrypoint.mode == 0o755
    assert entrypoint.user == get_variable(host, "operator_user")
    assert entrypoint.group == get_variable(host, "operator_group")

    if host.file(get_variable(host, "netbox_postgres_init_sql")).exists:
        init_sql = host.file(f"{config_dir}/docker-entrypoint-initdb.d/init.sql.osism")
        assert init_sql.exists
        assert not init_sql.is_directory
        assert init_sql.mode == 0o644

    db_script = host.file(
        f"{config_dir}/docker-entrypoint-initdb.d/init-netbox-database.sh"
    )
    assert db_script.exists
    assert not db_script.is_directory
    assert db_script.mode == 0o755
    assert db_script.user == get_variable(host, "operator_user")
    assert db_script.group == get_variable(host, "operator_group")
    assert "psql -v ON_ERROR_STOP=1 --username" in db_script.content_string


def test_netbox_config(host):
    config_dir = get_variable(host, "netbox_configuration_directory")
    directories = [
        f"{config_dir}/initializers",
        f"{config_dir}/startup-scripts",
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o755
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")

    netbox_env = host.file(f"{config_dir}/netbox.env")
    assert netbox_env.exists
    assert not netbox_env.is_directory
    assert netbox_env.mode == 0o640
    assert netbox_env.user == get_variable(host, "operator_user")
    assert netbox_env.group == get_variable(host, "operator_group")
    assert "CORS_ORIGIN_ALLOW_ALL=True" in netbox_env.content_string

    config_py = host.file(f"{config_dir}/configuration.py")
    assert config_py.exists
    assert not config_py.is_directory
    assert config_py.mode == 0o644
    assert config_py.user == get_variable(host, "operator_user")
    assert config_py.group == get_variable(host, "operator_group")
    assert (
        "SCRIPTS_ROOT = os.environ.get('SCRIPTS_ROOT', '/etc/netbox/scripts')"
        in config_py.content_string
    )

    nginx_unit = host.file(f"{config_dir}/nginx-unit.json")
    assert nginx_unit.exists
    assert not nginx_unit.is_directory
    assert nginx_unit.mode == 0o644
    assert nginx_unit.user == get_variable(host, "operator_user")
    assert nginx_unit.group == get_variable(host, "operator_group")
    assert '  "access_log": "/dev/stdout"' in nginx_unit.content_string

    netbox_init = get_variable(host, "netbox_init")
    if netbox_init:
        initializers = get_variable(host, "netbox_initializers")
        for init in initializers:
            f = host.file(f"{config_dir}/initializers/{init.rstrip()}.yml")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o644
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")

    script_dir = Path(f"{config_dir}/startup-scripts/")
    startup_scripts = list(script_dir.glob("*.py"))
    for script in startup_scripts:
        s = host.file(str(script))
        assert s.exists
        assert not s.is_directory
        assert s.mode == 0o644
        assert s.user == get_variable(host, "operator_user")
        assert s.group == get_variable(host, "operator_group")


def test_netbox_secrets(host):
    secrets_dir = get_variable(host, "netbox_secrets_directory")
    files = [
        f"{secrets_dir}/NETBOX_POSTGRES_PASSWORD",
        f"{secrets_dir}/NETBOX_SECRET_KEY",
        f"{secrets_dir}/NETBOX_TOKEN",
    ]

    for d in files:
        f = host.file(d)
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o644
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert (
            (f'{get_variable(host, "netbox_postgres_password")}' in f.content_string)
            or (f'{get_variable(host, "netbox_secret_key")}' in f.content_string)
            or (f'{get_variable(host, "netbox_user_api_token")}' in f.content_string)
        )


def test_dockernetwork(host):
    netbox_traefik = get_variable(host, "netbox_traefik")
    if not netbox_traefik:
        pytest.skip("netbox_traefik not configured")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert get_variable(host, "traefik_external_network_name") in stdout


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'netbox_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")


def test_netbox_service(host):
    service = host.service(get_variable(host, "netbox_service_name"))
    assert service.is_running
    assert service.is_enabled
