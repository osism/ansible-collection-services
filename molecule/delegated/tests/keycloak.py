from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


# testing config.yml tasks
def test_keycloak_config(host):
    config_dir = get_variable(host, "keycloak_configuration_directory")
    directories = [
        config_dir,
    ]
    for directory in directories:
        d = host.file(directory)
        assert d.exists
        assert d.is_directory
        assert d.mode == 0o750
        assert d.user == get_variable(host, "operator_user")
        assert d.group == get_variable(host, "operator_group")


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
