from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_dirs(host):
    config_dir = get_variable(host, "openldap_configuration_directory")
    directories = [
        config_dir,
        f"{config_dir}/umc/gateway",
        f"{config_dir}/umc/web",
        f"{config_dir}/umc/server",
        get_variable(host, "openldap_secrets_directory"),
        get_variable(host, "openldap_docker_compose_directory"),
    ]

    for d in directories:
        f = host.file(d)
        assert f.exists
        assert f.is_directory
        assert f.mode == 0o750
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")


def test_env_and_ucr_files(host):
    config_dir = get_variable(host, "openldap_configuration_directory")
    files = [
        f"{config_dir}/openldap.env",
        f"{config_dir}/udm-rest.env",
        f"{config_dir}/umc-web.env",
        f"{config_dir}/umc-gateway.env",
        f"{config_dir}/umc-server.env",
        f"{config_dir}/umc/server/ucr",
        f"{config_dir}/umc/gateway/ucr",
        f"{config_dir}/umc/web/ucr",
    ]

    for f in files:
        f = host.file(f)
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o640
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert "openldap_domain_name" or "openldap_ldap_port" in f.content_string


def test_secret_files(host):
    sec_dir = get_variable(host, "openldap_secrets_directory")
    files = [
        f"{sec_dir}/CAcert.pem",
        f"{sec_dir}/cert.pem",
        f"{sec_dir}/private.key",
        f"{sec_dir}/dh_2048.pem",
    ]

    for f in files:
        f = host.file(f)
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o644
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert (
            "-----BEGIN CERTIFICATE-----"
            or "-----BEGIN RSA PRIVATE KEY-----"
            or "-----BEGIN DH PARAMETERS-----" in f.content_string
        )


def test_dockercompose(host):
    f = host.file(
        f"{get_variable(host, 'openldap_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    openldap_container_name = get_variable(host, "openldap_container_name")

    with host.sudo(get_variable(host, "operator_user")):
        assert f'container_name: "{openldap_container_name}' in f.content_string


def test_openldap_service(host):
    service = host.service(get_variable(host, "openldap_service_name"))
    assert service.is_running
    assert service.is_enabled
