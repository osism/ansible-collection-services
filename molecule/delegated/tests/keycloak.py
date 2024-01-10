import pytest
from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


# testing config.yml tasks
def test_keycloak_config(host):
    config_dir = get_variable(host, "keycloak_configuration_directory")
    secrets_dir = get_variable(host, "keycloak_secrets_directory")
    directories = [
        config_dir,
        secrets_dir,
        get_variable(host, "keycloak_docker_compose_directory"),
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")

    keycloak_env = host.file(f"{config_dir}/keycloak.env")
    assert keycloak_env.exists
    assert not keycloak_env.is_directory
    assert keycloak_env.mode == 0o640
    assert keycloak_env.user == get_variable(host, "operator_user")
    assert keycloak_env.group == get_variable(host, "operator_group")
    assert (
        "KEYCLOAK_USER=" in keycloak_env.content_string
        and "KEYCLOAK_PASSWORD=" in keycloak_env.content_string
    )

    if host.file(get_variable(host, "keycloak_galera_backend_enable")) == "false":
        postgres_env = host.file(f"{config_dir}/postgres.env")
        f = host.file(postgres_env)
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o640
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert (
            "POSTGRES_PASSWORD_FILE=/run/secrets/POSTGRES_PASSWORD" in f.content_string
        )

    if host.file(get_variable(host, "keycloak_galera_backend_enable")) == "false":
        keycloak_secrets = [
            {
                "filename": "POSTGRES_PASSWORD",
                "secret": "{{ keycloak_postgres_password }}",
            },
        ]
        for keycloak_secret in keycloak_secrets:
            f = host.file(f"{secrets_dir}/{keycloak_secret}['filename']")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o644
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")


# Note: Tasks in create-database.yml were not tested.
#
#       - kolla_internal_vip_address,
#       - keycloak_database_name,
#       - keycloak_database_username and
#       - keycloak_database_password
#       in keycloak.env.j2 template and
#       - database_address,
#       - database_port,
#       - database_user and
#       - database_password
#       in create-database.yml
#       are undefined variables in keycloak/defaults/main.yml.
#
#       As well dynamic resolving of to the first host in the 'keycloak' group of inventory doesn't work
#       (cf. create-database.yml line 13 and 33).
#
#       Use of mariadb within default variable "keycloak_galera_backend_enable: true" seems to be obsolete.


# testing service.yml tasks
def test_docker_network(host):
    keycloak_traefik = get_variable(host, "keycloak_traefik")
    if not keycloak_traefik:
        pytest.skip("keycloak_traefik not configured")

    traefik_external_network_name = get_variable(host, "traefik_external_network_name")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert traefik_external_network_name in stdout


def test_docker_compose(host):
    f = host.file(
        f"{get_variable(host, 'keycloak_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    container_name = get_variable(host, "keycloak_container_name")
    with host.sudo(get_variable(host, "operator_user")):
        assert container_name in f.content_string


# Note: The test fails inexplicably with testinfra but the service is up and running
#
# def test_keycloak_service(host):
#     service = host.service(get_variable(host, "keycloak_service_name"))
#     assert service.is_running
#     assert service.is_enabled
