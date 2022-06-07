Ansible role for installing and configuring Rundeck and its components.
Rundeck enables self-service operations. You can give specific users
access to your existing tools, services and scripts.

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

.. zuul:rolevar:: docker_registry_rundeck
   :default: index.docker.io

The registry for the Rundeck Docker container.

.. zuul:rolevar:: docker_registry_postgres
   :default: index.docker.io

Registry for the Postgres Docker container.


**Rundeck Variables**

.. zuul:rolevar:: rundeck_configuration_directory
   :default: /opt/rundeck/configuration

In this directory the configuration files for Rundeck will be stored.

.. zuul:rolevar:: rundeck_secrets_directory
   :default: /opt/rundeck/secrets

Directory which contains the secret files.

.. zuul:rolevar:: rundeck_docker_compose_directory
   :default: /opt/rundeck

Path to the directory where the docker-compose-files from Rundeck will
be stored.

.. zuul:rolevar:: rundeck_network
   :default: 172.31.100.192/28

The network to use for the Rundeck container.

.. zuul:rolevar:: rundeck_service_name
   :default: docker-compose@rundeck

Name from the Rundeck service to deal with it.

.. zuul:rolevar:: rundeck_host
   :default: 127.0.0.1

The host where Rundeck will be reachable.

.. zuul:rolevar:: rundeck_port
   :default: 4440

Port which Rundeck will use for connections from outside.

.. zuul:rolevar:: rundeck_tag
   :default: 3.3.10

Version from the Rundeck which should be installed.

.. zuul:rolevar:: rundeck_image
   :default: {{ docker_registry_rundeck }}/rundeck/rundeck:{{ rundeck_tag }}

The container image to use.


**Postgres Variables**

.. zuul:rolevar:: rundeck_postgres_tag
   :default: 13-alpine

Version of Postgres which should be used.

.. zuul:rolevar:: rundeck_postgres_image
   :default: {{ docker_registry_postgres }}/library/postgres:{{ rundeck_postgres_tag }}

The container image to use.

.. zuul:rolevar:: rundeck_postgres_password
   :default: password

Password for the Rundeck-Postgres database.

.. zuul:rolevar:: rundeck_postgres_username
   :default: rundeck

Username for the Rundeck-Postgres database.

.. zuul:rolevar:: rundeck_postgres_databasename
   :default: rundeck

Name for the Rundeck-Postgres database.
