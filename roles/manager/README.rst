This ansible role install and configure the OSISM Manager Server and all its
required comopnents.

**Docker Variables**

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

The Docker registry which stores container files which are needed for the manager.

.. zuul:rolevar:: docker_registry_ansible
   :default: quay.io

Container registry which stores container files which are needed for the manager.

.. zuul:rolevar:: docker_registry_service
   :default: docker_registry

Look at docker_registry.

The following Variables declares for which service, which registry is to use:

.. zuul:rolevar:: docker_registry_ara_server
   :default: docker_registry_ansible

.. zuul:rolevar:: docker_registry_inventory_reconciler
   :default: docker_registry_ansible

.. zuul:rolevar:: docker_registry_mariadb
   :default: docker_registry_service

.. zuul:rolevar:: docker_registry_osism
   :default: docker_registry_ansible

.. zuul:rolevar:: docker_registry_osism_netbox
   :default: docker_registry_ansible

.. zuul:rolevar:: docker_registry_receptor
   :default: docker_registry_ansible

.. zuul:rolevar:: docker_registry_redis
   :default: docker_registry_service

.. zuul:rolevar:: docker_registry_vault
   :default: docker_registry_service

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.


**Generic Variables**

.. zuul:rolevar:: manager_network
   :default: 172.31.101.0/27

The subnet for the Manager in the docker-compose file.

.. zuul:rolevar:: manager_service_name
   :default: docker-compose@manager

Name from the Manager service to deal with it.

.. zuul:rolevar:: manager_service_restart
   :default: true

Controls the behavior of the restart handler. If set to false the manager service
will not restart even if the handler was triggered.


**Directory Variables**

.. zuul:rolevar:: ansible_directory
   :default: /opt/ansible

Directory for the Ansible configuration file.

.. zuul:rolevar:: archive_directory
   :default: /opt/archive

# Fix me

.. zuul:rolevar:: cache_directory
   :default: /opt/ansible/cache

Path to the cache which Ansible should use.

.. zuul:rolevar:: configuration_directory
   :default: /opt/configuration

Directory where the configuration files for OSISM are stored.

.. zuul:rolevar:: logs_directory
   :default: /opt/ansible/logs

Location of the logfiles from the installation.

.. zuul:rolevar:: secrets_directory
   :default: /opt/ansible/secrets

Directory which contains the secret files.

.. zuul:rolevar:: state_directory
   :default: /opt/state

In this directory the state files will be stored.

.. zuul:rolevar:: manager_docker_compose_directory
   :default: /opt/manager

Path to the directory where the docker-compose-files from the Manager
will be stored.

.. zuul:rolevar:: manager_configuration_directory
   :default: /opt/manager/configuration

This directory will contain the configuration files for the Manager.


**Operator user Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and
handles with Docker.


**Private keys**

.. zuul:rolevar:: deploy_private_key

.. code-block:: yaml

   -----BEGIN RSA PRIVATE KEY-----
   ...
   -----END RSA PRIVATE KEY-----

.. zuul:rolevar:: operator_private_key

.. code-block:: yaml

   -----BEGIN RSA PRIVATE KEY-----
   ...
   -----END RSA PRIVATE KEY-----

.. zuul:rolevar:: private_keys

These are the private keys in for ``deploy`` and ``operator``.


**Packages**

.. zuul:rolevar:: required_packages_manager
   :default: python3-virtualenv

Required packages for the Manager installation.


**Netbox Integration Variables**

.. zuul:rolevar:: enable_netbox
   :default: netbox_enable

Look at netbox_enable.

.. zuul:rolevar:: netbox_enable
   :default: false

Disables Netbox integration for deployment.

.. zuul:rolevar:: netbox_api_url
   :default: ""

Url to reach the Netbox API.

.. zuul:rolevar:: netbox_api_token
   :default: ""

Access token for Netbox API.


**OpenSearch Integration**

.. zuul:rolevar:: manager_opensearch_enable
   :default: true

Enable or disable OpenSearch integration

.. zuul:rolevar:: manager_opensearch_address
   :default: 127.0.0.1

OpenSearch address.

.. zuul:rolevar:: manager_opensearch_port
   :default: 9200

OpenSearch port.

.. zuul:rolevar:: manager_opensearch_protocol
   :default: https

OpenSearch protocol.


**Inventory-reconciler Variables**

.. zuul:rolevar:: inventory_reconciler_tag
   :default: latest

Version from the Inventory-reconciler in form of a tag which should be used.

.. zuul:rolevar:: inventory_reconciler_image
   :default: {{ docker_registry_inventory_reconciler }}
                  /osism/inventory-reconciler:{{ inventory_reconciler_tag }}

The container image to use.


**Ansible services Variables**

Note: The osism-ansible service is always enabled and cannot be disabled.

.. zuul:rolevar:: ansible_services_defaults

.. code-block:: yaml

   - name: ceph-ansible
     container_name: "{{ ceph_ansible_container_name }}"
     tag: "{{ ceph_ansible_tag }}"
     image: "{{ ceph_ansible_image }}"
     enable: "{{ enable_ceph_ansible }}"
   - name: kolla-ansible
     container_name: "{{ kolla_ansible_container_name }}"
     tag: "{{ kolla_ansible_tag }}"
     image: "{{ kolla_ansible_image }}"
     enable: "{{ enable_kolla_ansible }}"

Required services for OSISM.

.. zuul:rolevar:: ansible_services_extra
   :default: []

Here you can define extra services besides ceph-ansible and kolla-ansible.

.. zuul:rolevar:: ansible_services
   :default: ansible_services_defaults + ansible_services_extra

A compose of ansible_services_defaults and ansible_services_extra.


**osism-ansible Variables**

.. zuul:rolevar:: osism_ansible_container_name
   :default: osism-ansible

Name of the container in which osism-ansible will run.

.. zuul:rolevar:: osism_ansible_tag
   :default: latest

Version from osism-ansible in form of a tag which should be used.

.. zuul:rolevar:: osism_ansible_image
   :default: {{ docker_registry_ansible }}/osism/osism-ansible:{{ osism_ansible_tag }}

The container image to use.


**ceph-ansible Variables**

.. zuul:rolevar:: enable_ceph_ansible
   :default: ceph_ansible_enable

Have a look at ceph_ansible_enable.

.. zuul:rolevar:: ceph_ansible_enable
   :default: true

Enables ceph-ansible integration for deployment.

.. zuul:rolevar:: ceph_ansible_container_name
   :default: ceph-ansible

Name of the container in which ceph-ansible will run.

.. zuul:rolevar:: ceph_ansible_tag
   :default: pacific

Version in form of a tag which should be used.

.. zuul:rolevar:: ceph_ansible_image
   :default: {{ docker_registry_ansible }}/osism/ceph-ansible:{{ ceph_ansible_tag }}

The container image to use.


**kolla-ansible Variables**

.. zuul:rolevar:: enable_kolla_ansible
   :default: kolla_ansible_enable

Look at kolla_ansible_enable.

.. zuul:rolevar:: kolla_ansible_enable
   :default: true

Enables kolla-ansible integration for deployment.

.. zuul:rolevar:: kolla_ansible_container_name
   :default: kolla-ansible

Name of the container in which kolla-ansible will run.

.. zuul:rolevar:: kolla_ansible_tag
   :default: xena

Version in form of a tag which should be used.

.. zuul:rolevar:: kolla_ansible_image
   :default: {{ docker_registry_ansible }}/osism/kolla-ansible:{{ kolla_ansible_tag }}

The container image to use.


**Redis Variables**

.. zuul:rolevar:: manager_redis_tag
   :default: 7.0.0-alpine

Version in form of a tag which should be used.

.. zuul:rolevar:: manager_redis_image
   :default: {{ docker_registry_redis }}/library/redis:{{ manager_redis_tag }}

The container image to use.


**Ara Variables**

.. zuul:rolevar:: enable_ara
   :default: ara_enable

Look at ara_enable.

.. zuul:rolevar:: ara_enable
   :default: true

Enables Ara integration for deployment.

.. zuul:rolevar:: ara_username
   :default: ara

Defines the ara user.

.. zuul:rolevar:: ara_password
   :default: password

The password for ara.

.. zuul:rolevar:: ara_server_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: ara_server_host
   :default: ansible_default_ipv4.address

Hostname for the Ara server.

.. zuul:rolevar:: ara_server_port
   :default: 8120

Port for the Ara server.

.. zuul:rolevar:: ara_worker_connections
   :default: 1000

Number of ara-server worker connections.

.. zuul:rolevar:: ara_workers
   :default: 5

Number of ara-server workers.

.. zuul:rolevar:: ara_worker_class
   :default: gevent

Worker class for the ara-server service.

.. zuul:rolevar:: ara_threads
   :default: 1

Number of ara-server threads.

.. zuul:rolevar:: ara_server_tag
   :default: 1.5.8

Version which should be used.

.. zuul:rolevar:: ara_server_image
   :default: {{ docker_registry_ara_server }}/osism/ara-server:{{ ara_server_tag }}

The container image to use.

.. zuul:rolevar:: ara_server_database_type
   :default: mysql

Select the database backend for Ara.

.. zuul:rolevar:: ara_server_mariadb_host
   :default: ansible_default_ipv4.address

Address of the MariaDB database for Ara.

.. zuul:rolevar:: ara_server_mariadb_port
   :default: 3306

Port from the MariaDB database.

.. zuul:rolevar:: ara_server_mariadb_username
   :default: ara

Database username for Aras MariaDB.

.. zuul:rolevar:: ara_server_mariadb_password
   :default: password

Password for the database.

.. zuul:rolevar:: ara_server_mariadb_databasename
   :default: ara_server_mariadb_username

Name for the database Ara should use.

.. zuul:rolevar:: ara_server_mariadb_tag
   :default: 10.8.3

The Version which should be used.

.. zuul:rolevar:: ara_server_mariadb_image
   :default: {{ docker_registry_mariadb }}/library/mariadb:{{ ara_server_mariadb_tag }}

The container image to use.


**Celery Variables**

.. zuul:rolevar:: enable_celery
   :default: celery_enable

Have a look at celery_enable.

.. zuul:rolevar:: celery_enable
   :default: true

Disables Celery integration for deployment.

.. zuul:rolevar:: osism_tag
   :default: latest

The Version which should used.

.. zuul:rolevar:: osism_image
   :default: {{ docker_registry_osism }}/osism/osism:{{ osism_tag }}

The container image which should used.

.. zuul:rolevar:: osism_netbox_tag
   :default: latest

Version which should be used.

.. zuul:rolevar:: osism_netbox_image
   :default: {{ docker_registry_osism_netbox }}/osism/osism-netbox:{{ osism_netbox_tag }}

The container image which should used.

.. zuul:rolevar:: flower_host
   :default: ansible_default_ipv4.address

Address of the Flower server for Celery queue.

.. zuul:rolevar:: flower_port
   :default: 5555

Port which Flower will use for connections from outside.

.. zuul:rolevar:: flower_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: osism_api_host
   :default: ansible_default_ipv4.address

Address of the OSISM API.

.. zuul:rolevar:: osism_api_port
   :default: 8000

Port for the OSISM API.


**Vault Variables**

.. zuul:rolevar:: vault_container_name
   :default: vault

Name of the container in which Vault will run.

.. zuul:rolevar:: enable_vault
   :default: false

Enables Vault integration for deployment.

.. zuul:rolevar:: vault_host
   :default: ansible_default_ipv4.address

Address of the HashiCorp Vault server.

.. zuul:rolevar:: vault_port
   :default: 8200

Port which Vault will use for connections from outside.

.. zuul:rolevar:: vault_tag
   :default: 1.10.3

The Version which should used.

.. zuul:rolevar:: vault_image
   :default: {{ docker_registry_vault }}/hashicorp/vault:{{ vault_tag }}

The container image to use.

.. zuul:rolevar:: vault_output_key_shares
   :default: false

Disables the output of the Vault unlock keys.

.. zuul:rolevar:: vault_write_key_shares
   :default: false

Disables the writing Vault unlock keys to a file.

.. zuul:rolevar:: vault_key_shares_path
   :default: {{ manager_secrets_directory }}/vault_key_shares.yml

Location of the file which contains the Vault unlock keys.


**Enviroment Variables**

.. zuul:rolevar:: manager_environment_extra
   :default: {}

Enviroments variables that will be added at the ansible container start.


**Listener Variables**

.. zuul:rolevar:: enable_listener
   :default: false

Enable listener service.

.. zuul:rolevar:: manager_listener_broker_uri
   :default: amqp://openstack:password@127.0.0.1:5672/

OpenStack broker URI.


**OpenStack Variables**

.. zuul:rolevar:: manager_openstack_os_project_domain_name
   :default: Default

.. zuul:rolevar:: manager_openstack_os_user_domain_name
   :default: Default

.. zuul:rolevar:: manager_openstack_os_project_name
   :default: admin

.. zuul:rolevar:: manager_openstack_os_username
   :default: admin

.. zuul:rolevar:: manager_openstack_os_password
   :default: password

.. zuul:rolevar:: manager_openstack_os_auth_url
   :default: http://localhost:5000/v3

Enviroment variables for the OSISM container.
These are the credentials to access the OpenStack installation.


**Traefik Variables**

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of the Manager network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.


**Replicas**

.. zuul:rolevar:: manager_netbox_replicas
   :default: 1

Define how many replicas from Netbox will be installed.

**Service integrations**

.. zuul:rolevar:: manager_enable_bifrost
   :default: false

Enable bifrost integration.

.. zuul:rolevar:: manager_enable_ironic
   :default: true

Enable ironic integration.


**Other services**

.. zuul:rolevar:: beat_enable
   :default: true

Enable beat service.

.. zuul:rolevar:: flower_enable
   :default: false

Enable flower service.
