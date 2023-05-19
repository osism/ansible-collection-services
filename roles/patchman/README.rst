This ansible role install and configure Patchman and required components.
Patchman is a maleware and vulnerability tool for websites. It will patch
automaticly if it find something.

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

.. zuul:rolevar:: docker_registry_patchman
   :default: quay.io

The registry for the Patchman Docker container.

.. zuul:rolevar:: docker_registry_postgres
   :default: index.docker.io

Registry for the Postgres Docker container files.

.. zuul:rolevar:: docker_registry_memcached
   :default: index.docker.io

The registry for the Memcached container files.


**Patchman Variables**

.. zuul:rolevar:: patchman_configuration_directory
   :default: /opt/patchman/configuration

In this directory the configuration files for Patchman will be stored.

.. zuul:rolevar:: patchman_docker_compose_directory
   :default: /opt/patchman

Path to the directory where the docker-compose-files from Patchman will
be stored.

.. zuul:rolevar:: patchman_host
   :default: 127.0.0.1

The host where Patchman will be reachable.

.. zuul:rolevar:: patchman_port
   :default: 8150

Port which Patchman will use for connections from outside.

.. zuul:rolevar:: patchman_server_url
   :default: http://{{ patchman_host }}:{{ patchman_port }}

The url under which Patchman is reachable.

.. zuul:rolevar:: patchman_tag
   :default: 2.0.3

Version from the Patchman which should be installed.

.. zuul:rolevar:: patchman_image
   :default: {{ docker_registry_patchman }}/osism/patchman:{{ patchman_tag }}

The container image to use.

.. zuul:rolevar:: patchman_container_name
   :default: patchman

Name of the container in which Patchman will run.

.. zuul:rolevar:: patchman_network
   :default: 172.31.100.80/28

The network to use for the Patchman container.

.. zuul:rolevar:: patchman_service_name
   :default: docker-compose@patchman

Name from the Patchman service to deal with it.

.. zuul:rolevar:: patchman_username
   :default: patchman

Username for Patchman login.

.. zuul:rolevar:: patchman_password
   :default: password

Password for Patchman login.

.. zuul:rolevar:: patchman_secret_key
   :default: aiGe7eedievootee3ook3aeshok2sa4p

The secret key for patchman.

.. zuul:rolevar:: patchman_cron_day
   :default: *

Day-parameter for the Patchman cronjob.

.. zuul:rolevar:: patchman_cron_hour
   :default: 1

Hour-parameter for the Patchman cronjob.

.. zuul:rolevar:: patchman_cron_minute
   :default: 3

Minute-parameter for the Patchman cronjob.

.. zuul:rolevar:: patchman_cron_user
   :default: {{ operator_user | default('dragon') }}

User that should hold the cronjobs for Patchman.

.. zuul:rolevar:: patchman_debug
   :default: False

Disable debugging messages.

.. zuul:rolevar:: patchman_update_statfile
   :default: /tmp/patchman.stat

File to safe the last execution time of Patchman.

.. zuul:rolevar:: patchman_update
   :default: true

Enables the update funktion from Patchman.

.. zuul:rolevar:: patchman_update_force
   :default: false

Forces the update run to be executed.

.. zuul:rolevar:: patchman_update_valid_time
   :default: 86400

Defines the intervall for how long an update is considerd as valid.


**Postgres Variables**

.. zuul:rolevar:: postgres_tag
   :default: 14.2-alpine

Version of Postgres which should be used.

.. zuul:rolevar:: postgres_image
   :default: {{ docker_registry_postgres }}/library/postgres:{{ postgres_tag }}

The container image to use.

.. zuul:rolevar:: patchman_postgres_username
   :default: patchman

Username for the Patchman-Postgres database.

.. zuul:rolevar:: patchman_postgres_password
   :default: password

Password for the Patchman-Postgres database.

.. zuul:rolevar:: patchman_postgres_databasename
   :default: patchman_postgres_username

Password for the Patchman-Postgres database.


**Memcached Variables**

.. zuul:rolevar:: patchman_memcached_tag
   :default: 1.6.14-alpine

Version from Memcached which should used.

.. zuul:rolevar:: patchman_memcached_image
   :default: {{ docker_registry_memcached }}/library/memcached:{{ patchman_memcached_tag }}

The container image to use.


**Traefik Variables**

.. zuul:rolevar:: patchman_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of Patchman network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
