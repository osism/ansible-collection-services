Ansible role for installation and configuration Netbox and all its
components. Netbox is an infrastructure resource modeling (IRM) tool to
empower network automation. 

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry_netbox
   :default: quay.io

Name of the registry for the Netbox container image.

.. zuul:rolevar:: docker_registry_postgres
   :default: index.docker.io

Name of the registry for the Postgres container image.

.. zuul:rolevar:: docker_registry_redis
   :default: index.docker.io

Name of the registry for the Redis container image.

.. zuul:rolevar:: netbox_service_restart
   :default: true

Controls the behavior of the restart handler. If set to false the netbox service
will not restart even if the handler was triggered.


**Variables for Netbox**

.. zuul:rolevar:: netbox_configuration_directory
   :default: /opt/netbox/configuration

The directory where the configuration for the Netbox will be stored.

.. zuul:rolevar:: netbox_secrets_directory
   :default: /opt/netbox/secrets

Directory which contains the secret files.

.. zuul:rolevar:: netbox_docker_compose_directory
   :default: /opt/netbox

Path to the directory where the docker-compose-files from Netbox will be
stored.

.. zuul:rolevar:: netbox_network
   :default: 172.31.100.176/28

The network to use for the Netbox container.

.. zuul:rolevar:: netbox_service_name
   :default: docker-compose@netbox

Name of the docker-compose service for Netbox.

.. zuul:rolevar:: netbox_host
   :default: 127.0.0.1

Hostname for the Netbox server.

.. zuul:rolevar:: netbox_port
   :default: 8121

Port for the Netbox server.

.. zuul:rolevar:: netbox_osism_api_host
   :default: netbox_host

Sets the Osism API host.

.. zuul:rolevar:: netbox_osism_api_port
   :default: 8000

Sets th eOsism API port.

.. zuul:rolevar:: netbox_userid
   :default: 101

Defines the userid for container user inside the netbox container.

.. zuul:rolevar:: netbox_tag
   :default: v3.2.3-ldap

Version of Netbox which should be used.

.. zuul:rolevar:: netbox_image
   :default: {{ docker_registry_netbox }}/osism/netbox:{{ netbox_tag }}

The container image to use.

.. zuul:rolevar:: netbox_secret_key
   :default: 00000000-0000-0000-0000-000000000000

The secret key for Netbox.

.. zuul:rolevar:: netbox_superuser_name
   :default: admin

The name for the superuser.

.. zuul:rolevar:: netbox_superuser_email
   :default: netbox@osism.local

Email Address for the superuser.

.. zuul:rolevar:: netbox_superuser_password
   :default: password

Password for the superuser.

.. zuul:rolevar:: netbox_superuser_api_token
   :default: 0000000000000000000000000000000000000000

Api Token for the superuser.

.. zuul:rolevar:: netbox_user_name
   :default: dragon

User for Netbox.

.. zuul:rolevar:: netbox_user_api_token
   :default: 1111111111111111111111111111111111111111

Api token for the Netbox user.

.. zuul:rolevar:: netbox_ldap_enable
   :default: false

LDAP should not be used for user authentication against netbox.

.. zuul:rolevar:: netbox_ldap_server_uri
   :default: ldap://localhost:389

Address of the LDAP server.

.. zuul:rolevar:: netbox_ldap_bind_dn
   :default: ""

Username used for connecting to the LDAP server.

.. zuul:rolevar:: netbox_ldap_bind_password
   :default: ""

Password used for connecting to the LDAP server.

.. zuul:rolevar:: netbox_ldap_user_dn_template

If required define the LDAP user template here.

.. zuul:rolevar:: netbox_ldap_user_search_attr
   :default: sAMAccountName

Defines which attribute of a user DN is the naming attribute.

.. zuul:rolevar:: netbox_ldap_user_search_basedn
   :default: ""

Defines the users base DN string.

.. zuul:rolevar:: netbox_ldap_group_search_class
   :default: group

Defines the search class for a group (can be user or group)

.. zuul:rolevar:: netbox_ldap_group_search_basedn
   :default: ""

Defines the group base DN string.

.. zuul:rolevar:: netbox_ldap_group_type
   :default: NestedGroupOfNamesType

Sets the type of the LDAP group.

.. zuul:rolevar:: netbox_ldap_require_group_dn

When a group DN string is required, set this

.. zuul:rolevar:: netbox_ldap_is_admin_dn

If a DN is required to login as an admin. You need to define the DN here if required.

.. zuul:rolevar:: netbox_ldap_is_superuser_dn

If a DN is required to get superuser rights. You need to define the DN here if required.

.. zuul:rolevar:: netbox_ldap_start_tls
   :default: false

Configures if START TLS should be used.

.. zuul:rolevar:: netbox_ldap_ignore_cert_errors
   :default: false

Wheater certificate issues should be ignored or not.

.. zuul:rolevar:: netbox_ldap_mirror_groups
   :default: false

Configures if groups from ldap should be mirrored to netbox.

.. zuul:rolevar:: netbox_ldap_find_group_perms
   :default: true

If true, configures the rights from LDAP automatically to matching group names in netbox.

.. zuul:rolevar:: netbox_ldap_cache_timeout
   :default: 3600

Cache time span before an information becomes invalid if there is no connection to the server.

.. zuul:rolevar:: netbox_metrics
   :default: True

Configures, if netbox should offer a metrics endpoint which can be monitored.

.. zuul:rolevar:: netbox_max_db_wait_time
   :default: 90

Time to wait for the database.

.. zuul:rolevar:: netbox_extra
   :default: {}

Additional environment variables for the netbox container.

.. zuul:rolevar:: netbox_plugins_defaults
   :default: - netbox_initializers
             - netbox_plugin_osism

Plugins for Netbox which should be installed at default.

.. zuul:rolevar:: netbox_plugins_extra
   :default: []

Here you can define extra plugins.

.. zuul:rolevar:: netbox_plugins
   :default: netbox_plugins_defaults + netbox_plugins_extra

Compose of netbox_plugins_defaults + netbox_plugins_extra.

.. zuul:rolevar:: netbox_plugins_config_osism

.. code-block:: yaml

   grafana: "http://{{ kolla_internal_vip_address | default('127.0.0.1') }}:3000"
   netdata: "http://{{ netdata_api_host | default('127.0.0.1') }}:19999"

OSISM specific configuration for plugins of netbox. Contains mostly urls to other connected services.

.. zuul:rolevar:: netbox_plugins_config
   :default: netbox_plugin_osism: {{ netbox_plugins_config_osism }}

Configuration for all Plugins of netbox.


**Postgres Variables**

.. zuul:rolevar:: postgres_tag
   :default: 15.3-alpine

Version of Postgres which should be used.

.. zuul:rolevar:: postgres_image
   :default: {{ docker_registry_postgres }}/library/postgres:{{ postgres_tag }}

The container image to use.

.. zuul:rolevar:: netbox_postgres_password
   :default: password

Password for the Netbox-Postgres database.

.. zuul:rolevar:: netbox_postgres_username
   :default: netbox

Username for the Netbox-Postgres database.

.. zuul:rolevar:: netbox_postgres_databasename
   :default: netbox

Name for the Netbox-Postgres database.

.. zuul:rolevar:: netbox_postgres_init_sql
   :default: "{{ configuration_directory }}/environments/infrastructure/files/netbox/init.sql"

Optional init.sql file in the configuration repository that should be used to initialize
the database.

**Redis Variables**

.. zuul:rolevar:: netbox_redis_tag
   :default: 7.0.0-alpine

Version for Redis which should be used.

.. zuul:rolevar:: netbox_redis_image
   :default: {{ docker_registry_redis }}/library/redis:{{ netbox_redis_tag }}

The container image to use.


**Traefik Variables**

.. zuul:rolevar:: netbox_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of Netbox network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.


**Initializers Variables**

.. zuul:rolevar:: netbox_init
   :default: true

Copy and run initialize scripts.

.. zuul:rolevar:: netbox_initializers
   :default: - custom_fields
             - device_roles
             - device_types
             - groups
             - manufacturers
             - object_permissions
             - prefix_vlan_roles
             - sites
             - tags
             - users
             - webhooks

List of files which contain preconfigured settings for netbox data.
(Like device types, custom fields, etc.)

.. zuul:rolevar:: netbox_init_object_permissions

.. code-block:: yaml

   read_write_all:
     enabled: true
     description: 'Read/Write all objects'
     object_types: all
     actions:
       - add
       - change
       - delete
       - view
     groups:
       - netbox-writers
   read_all:
     enabled: true
     description: 'Read all objects'
     object_types: all
     actions:
       - view
     groups:
       - netbox-readers

Part of the initial data to configure netbox. contains permission settings
for read_write_all and read_write permission.

.. zuul:rolevar:: netbox_init_groups

.. code-block:: yaml

   netbox-writers:
     users:
       - "{{ netbox_user_name }}"
   netbox-readers:
     users: []

Sets permissions trough netbox groups by adding users to the respective groups.

.. zuul:rolevar:: netbox_init_users_template
   :default: {'{{ netbox_user_name }}': {'api_token': '{{ netbox_user_api_token }}'}}

String in a specific format that adds users to netbox with name and api token.

.. zuul:rolevar:: netbox_init_users
   :default: netbox_init_users_template

Have a look at netbox_init_users_template.
