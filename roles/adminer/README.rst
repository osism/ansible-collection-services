Ansible role to install and configure Adminer with docker-compose.
Adminer is a tool for database management.

**Role Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

Default name of the registry for container images.

.. zuul:rolevar:: docker_registry_adminer
   :default: docker_registry

Name of the registry for the adminer container image.

.. zuul:rolevar:: operator_user
   :default: dragon

The user that should own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

The group that should own the configuration directory.

.. zuul:rolevar:: adminer_docker_compose_directory
   :default: /opt/adminer

The path where the docker-compose-files from Adminer will be stored.

.. zuul:rolevar:: adminer_host
   :default: 127.0.0.1

The host where Adminer will be reachable.

.. zuul:rolevar:: adminer_database_host
   :default: 127.0.0.1

Default database host that adminer should connect to.

.. zuul:rolevar:: adminer_port
   :default: 8111

Port which Adminer will be used for connections from outside.

.. zuul:rolevar:: adminer_tag
   :default: '4.7'

Tag of the container image that should be used.

.. zuul:rolevar:: adminer_image
   :default: "{{ docker_registry_adminer }}/library/adminer:{{ adminer_tag }}"

The container image to use.

.. zuul:rolevar:: adminer_network
   :default: 172.31.100.64/28

The network to use for the adminer container.

.. zuul:rolevar:: adminer_service_name
   :default: docker-compose@adminer

Name of the docker-compose service for adminer.
