Ansible role for installation and configuration keycloak and all its
components. Keycloak is an Identity and Access Management (IAM) tool. 

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and
handles with Docker.


**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker dose not check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_keycloak
   :default: quay.io

Path to the registry that stores the Docker container images for Keycloak.

.. zuul:rolevar:: docker_registry_postgres
   :default: index.docker.io

The registry for the Postgres Docker container.


**Keycloak Variables**

.. zuul:rolevar:: keycloak_configuration_directory
   :default: /opt/keycloak/configuration

In this directory the configuration files for Keycloak will be stored.

.. zuul:rolevar:: keycloak_secrets_directory
   :default: /opt/keycloak/secrets

This directory will store the secrets file.

.. zuul:rolevar:: keycloak_docker_compose_directory
   :default: /opt/keycloak

Path to the directory where the docker-compose-files from Keycloak will
be stored.

.. zuul:rolevar:: keycloak_network
   :default: 172.31.100.144/28

The subnet for Keycloak in the docker-compose file.

.. zuul:rolevar:: keycloak_container_name
   :default: keycloak

Name of the container in which Keycloak will run.

.. zuul:rolevar:: keycloak_service_name
   :default: docker-compose@keycloak

Name from the Keycloak service to deal with it.

.. zuul:rolevar:: keycloak_host
   :default: 127.0.0.1

The host where Keycloak will be reachable.

.. zuul:rolevar:: keycloak_port
   :default: 8170

Port which Keycloak will use for connections from outside.

.. zuul:rolevar:: keycloak_tag
   :default: legacy

Version from Keycloak in form of a tag which should be used.

.. zuul:rolevar:: keycloak_image
   :default: {{ docker_registry_keycloak }}/keycloak/keycloak:{{ keycloak_tag }}

The container image to use.

.. zuul:rolevar:: keycloak_username
   :default: admin

Default login user name for the first login.
You should change it for more security.

.. zuul:rolevar:: keycloak_password
   :default: password

Password for the first login.
For more security you should change it after the first login.


**Postgres Variables**

.. zuul:rolevar:: postgres_tag
   :default: 14-alpine

Version from Postgres in form of a tag which should be used.

.. zuul:rolevar:: postgres_image
   :default: {{ docker_registry_postgres }}/library/postgres:{{ postgres_tag }}

The container image to use.

.. zuul:rolevar:: keycloak_postgres_password
   :default: password

Password for the first login.
For more security you should change it after the first login.

.. zuul:rolevar:: keycloak_postgres_username
   :default: keycloak

Default login user name for the first login.
You should change it for more security.

.. zuul:rolevar:: keycloak_postgres_databasename
   :default: keycloak

The name for the Postgres database from Keycloak.


**MariaDB Variables**

.. zuul:rolevar:: keycloak_galera_backend_enable
   :default: false

Disable the Galera database.
Galera provides high availability for mariadb or mysql databases.

.. zuul:rolevar:: keycloak_use_preconfigured_databases
   :default: false

The database provided with Keycloak will be disabled. 


**Traefik Variables**

.. zuul:rolevar:: keycloak_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of the Docker network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
