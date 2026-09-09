import pytest
import re
import yaml
from .util.util import get_ansible, get_variable, get_role_variable
from packaging.version import Version

testinfra_runner, testinfra_hosts = get_ansible()

MANAGER_DEFAULTS = "../../roles/manager/defaults/main.yml"
MANAGER_FIXTURE = "../../molecule/delegated/vars/manager.yml"
ALL_ENV_TEMPLATE = "../../roles/manager/templates/env/all.env.j2"

PROXY_VARIABLES = [
    "HTTP_PROXY",
    "http_proxy",
    "HTTPS_PROXY",
    "https_proxy",
    "NO_PROXY",
    "no_proxy",
]


def render_all_env(host, **variables):
    """Render env/all.env.j2 of the manager role with the given variables.

    The role defaults and the molecule fixture are passed to Ansible as extra
    vars, so the templated defaults, above all manager_proxy_no_proxy, are
    evaluated by Ansible in the same way as in the role. The given variables
    take precedence over both. Returns the rendered file as a dictionary.
    """
    variables = {
        **host.ansible("include_vars", MANAGER_DEFAULTS)["ansible_facts"],
        **host.ansible("include_vars", MANAGER_FIXTURE)["ansible_facts"],
        **variables,
    }
    path = host.ansible("tempfile", "suffix=.env", check=False)["path"]
    try:
        host.ansible(
            "template",
            f"src={ALL_ENV_TEMPLATE} dest={path}",
            check=False,
            extra_vars=variables,
        )
        content = host.file(path).content_string
    finally:
        host.ansible("file", f"path={path} state=absent", check=False)

    return dict(line.split("=", 1) for line in content.splitlines() if line)


# testing config.yml tasks
def test_manager_config(host):
    config_dir = get_variable(host, "manager_configuration_directory")
    manager_dir = get_variable(host, "manager_secrets_directory")
    secrets_dir = get_variable(host, "secrets_directory")
    directories = [
        get_variable(host, "ansible_directory"),
        get_variable(host, "archive_directory"),
        config_dir,
        get_variable(host, "manager_docker_compose_directory"),
        manager_dir,
        secrets_dir,
        get_variable(host, "state_directory"),
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")

    client_env = host.file(f"{config_dir}/client.env")
    assert client_env.exists
    assert not client_env.is_directory
    assert client_env.mode == 0o640
    assert client_env.user == get_variable(host, "operator_user")
    assert client_env.group == get_variable(host, "operator_group")
    assert "OPENSEARCH_ADDRESS=" in client_env.content_string

    all_env = host.file(f"{config_dir}/all.env")
    assert all_env.exists
    assert not all_env.is_directory
    assert all_env.mode == 0o640
    assert all_env.user == get_variable(host, "operator_user")
    assert all_env.group == get_variable(host, "operator_group")
    assert "INVENTORY_RECONCILER_SCHEDULE=" in all_env.content_string

    # NOTE: The molecule fixture keeps the proxy disabled, this is the
    #       disabled branch of all.env.j2. The enabled branch is covered by
    #       test_manager_proxy_environment on a rendering of the template.
    for variable in PROXY_VARIABLES:
        assert f"{variable}=" not in all_env.content_string

    # config-ara
    if host.file(get_variable(host, "enable_ara")) == "true":
        ara_files = [
            host.file(f"{config_dir}/ara.env"),
            host.file(f"{config_dir}/ara-server.env"),
        ]
        for file in ara_files:
            f = host.file(file)
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o640
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")
            assert (
                "ARA_API_CLIENT=http" or "ARA_ALLOWED_HOSTS=['*']" in f.content_string
            )

        if host.file(get_variable(host, "ara_server_database_type")) == "mysql":
            f = host.file(f"{config_dir}/mariadb.env")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o640
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")
            assert "MYSQL_DATABASE=" in f.content_string

    # config-vault
    if host.file(get_variable(host, "enable_vault")) == "true":
        vault_files = [
            host.file(f"{config_dir}/vault.env"),
            host.file(f"{config_dir}/vault.hcl"),
        ]
        assert vault_files[0].mode == 0o640
        assert vault_files[1].mode == 0o644

        for file in vault_files:
            f = host.file(file)
            assert f.exists
            assert not f.is_directory
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")
            assert (
                "VAULT_API_ADDR=http://" in f.content_string
                or 'listener "tcp" {' in f.content_string
            )

    # config-ansible
    ssh_keys = get_variable(host, "private_keys")
    for key, value in ssh_keys.items():
        f = host.file(f"{secrets_dir}/id_rsa.{key}")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o600
        assert f.user == get_variable(host, "operator_user")
        assert "-----BEGIN RSA PRIVATE KEY-----" in f.content_string

    ansible_env = host.file(f"{config_dir}/ansible.env")
    assert ansible_env.exists
    assert not ansible_env.is_directory
    assert ansible_env.mode == 0o640
    assert ansible_env.user == get_variable(host, "operator_user")
    assert ansible_env.group == get_variable(host, "operator_group")

    # config-netbox
    if host.file(get_variable(host, "enable_netbox")) == "true":
        netbox_secrets = [
            {"filename": "NETBOX_TOKEN", "secret": "{{ netbox_api_token }}"},
        ]
        for netbox_secret in netbox_secrets:
            f = host.file(f"{manager_dir}/{netbox_secret}['filename']")
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o644
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")

        netbox_env = host.file(f"{config_dir}/netbox.env")
        assert netbox_env.exists
        assert not netbox_env.is_directory
        assert netbox_env.mode == 0o640
        assert netbox_env.user == get_variable(host, "operator_user")
        assert netbox_env.group == get_variable(host, "operator_group")
        assert "NETBOX_API=" in netbox_env.content_string

    # config-celery
    if host.file(get_variable(host, "enable_celery")) == "true":
        celery_files = [
            host.file(f"{config_dir}/conductor.env"),
            host.file(f"{config_dir}/openstack.env"),
            host.file(f"{config_dir}/environments/manager/files/conductor.yml"),
        ]
        if host.file(get_variable(host, "enable_listener")) == "true":
            celery_files.append(host.file(f"{config_dir}/listener.env"))

        for file in celery_files:
            f = host.file(file)
            assert f.exists
            assert not f.is_directory
            assert f.mode == 0o644
            assert f.user == get_variable(host, "operator_user")
            assert f.group == get_variable(host, "operator_group")

    # config-wrapper
    wrapper_scripts = get_role_variable(host, "manager_wrapper_scripts", "wrapper.yml")

    for script in wrapper_scripts:
        f = host.file(f"/usr/local/bin/{script}")
        assert f.exists
        assert not f.is_directory
        assert f.mode == 0o755
        assert f.user == get_variable(host, "operator_user")
        assert f.group == get_variable(host, "operator_group")
        assert "#!/usr/bin/env bash" in f.content_string


def test_manager_proxy_environment(host):
    # NOTE: The enabled branch is rendered separately from the converge.
    #       Enabling the proxy in the molecule fixture would send the
    #       outbound traffic of every manager service to an unreachable
    #       proxy for the rest of the scenario.
    proxy = "http://proxy.molecule.test:3128"
    no_proxy_extra = ["192.168.16.0/20", "api-int.molecule.test"]
    manager_network = get_variable(host, "manager_network")
    manager_network_ipv6 = get_variable(host, "manager_network_ipv6")

    environment = render_all_env(
        host,
        manager_configure_proxy=True,
        manager_proxy_http=proxy,
        manager_proxy_no_proxy_extra=no_proxy_extra,
        manager_network_enable_ipv6=False,
    )
    assert environment["HTTP_PROXY"] == proxy
    assert environment["http_proxy"] == proxy
    # manager_proxy_https follows manager_proxy_http by default
    assert environment["HTTPS_PROXY"] == proxy
    assert environment["https_proxy"] == proxy
    assert environment["no_proxy"] == environment["NO_PROXY"]

    no_proxy = environment["NO_PROXY"].split(",")
    assert manager_network in no_proxy
    assert manager_network_ipv6 not in no_proxy
    # from manager_proxy_no_proxy_default and from ansible_services
    for name in [
        "localhost",
        "api",
        "netbox",
        "openstack",
        "osism-ansible",
        "kolla-ansible",
    ]:
        assert name in no_proxy, f"Service '{name}' is not excluded from the proxy"
    for entry in no_proxy_extra:
        assert entry in no_proxy, f"Entry '{entry}' is not excluded from the proxy"

    environment = render_all_env(
        host,
        manager_configure_proxy=True,
        manager_network_enable_ipv6=True,
    )
    assert manager_network_ipv6 in environment["NO_PROXY"].split(",")


def test_max_user_watches_and_instances(host):
    sysctl_max_user_watches = host.sysctl("fs.inotify.max_user_watches")
    assert sysctl_max_user_watches == 32768

    sysctl_max_user_instances = host.sysctl("fs.inotify.max_user_instances")
    assert sysctl_max_user_instances == 256


# testing service.yml tasks
def test_docker_network(host):
    ara_server_traefik = get_variable(host, "ara_server_traefik")
    if not ara_server_traefik:
        pytest.skip("ara_server_traefik not configured")

    traefik_external_network_name = get_variable(host, "traefik_external_network_name")

    with host.sudo("root"):
        stdout = host.check_output("docker network ls")
        assert traefik_external_network_name in stdout


def test_mariadb_health(host):
    ara_server_database_type = get_variable(host, "ara_server_database_type")

    if ara_server_database_type == "mysql":
        ara_server_mariadb_tag = get_variable(host, "ara_server_mariadb_tag")
        mysql_user = get_variable(host, "ara_server_mariadb_username")
        mysql_password = get_variable(host, "ara_server_mariadb_password")
        db_healthcheck = ""

        if ara_server_mariadb_tag:
            version = Version(ara_server_mariadb_tag)
            if version < Version("11.0.0"):
                with host.sudo("root"):
                    db_healthcheck = host.run(
                        f"docker exec manager-mariadb-1 mysqladmin status -h "
                        f"localhost -u {mysql_user} -p{mysql_password}"
                    )
            elif version >= Version("11.0.0"):
                with host.sudo("root"):
                    db_healthcheck = host.run(
                        "docker exec manager-mariadb-1 healthcheck.sh --connect --innodb_initialized"
                    )

        if db_healthcheck:
            assert db_healthcheck.rc == 0
        else:
            pytest.skip(
                "Skipping test as ara_server_mariadb_tag is not set or does not match any condition."
            )
    else:
        pytest.skip("Skipping test as ara_server_database_type is not set to mysql.")


def test_docker_compose(host):
    f = host.file(
        f"{get_variable(host, 'manager_docker_compose_directory')}/docker-compose.yml"
    )
    assert f.exists
    assert not f.is_directory
    assert f.mode == 0o640
    assert f.user == get_variable(host, "operator_user")
    assert f.group == get_variable(host, "operator_group")

    container_names = [
        get_variable(host, "osism_ansible_container_name"),
        get_variable(host, "ceph_ansible_container_name"),
        get_variable(host, "kolla_ansible_container_name"),
    ]
    if host.file(get_variable(host, "enable_vault")) == "true":
        container_names.append(get_variable(host, "vault_container_name"))

    for container in container_names:
        with host.sudo(get_variable(host, "operator_user")):
            assert re.search(
                rf'container_name: "{container}"', f.content_string
            ), f"Container name '{container}' not found in docker-compose.yml"

    # NOTE: all.env carries the proxy configuration, every service of the
    #       manager has to read it, also without the netbox integration.
    all_env = f"{get_variable(host, 'manager_configuration_directory')}/all.env"
    services = yaml.safe_load(f.content_string)["services"]
    for name in [
        "api",
        "beat",
        "conductor",
        "flower",
        "inventory_reconciler",
        "listener",
        "netbox",
        "openstack",
        "osism-ansible",
        "osismclient",
        "watchdog",
    ]:
        if name not in services:
            continue
        assert all_env in services[name].get(
            "env_file", []
        ), f"Service '{name}' does not read all.env"


def test_manager_service(host):
    service = host.service(get_variable(host, "manager_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_function(host):
    result = host.run("osism get versions manager")
    assert result.rc == 0
    assert "osism-ansible" in result.stdout


# Note: initialize.yml tasks were not tested.
