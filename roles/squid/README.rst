This ansible role installs squid proxy.
Allow other services to access only allowed addresses.

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_squid
   :default: index.docker.io

Path to the registry that stores the Docker container images for Squid.

.. zuul:rolevar:: squid_configuration_directory
   :default: /opt/squid/configuration

In this directory the configuration files will be stored.

.. zuul:rolevar:: squid_docker_compose_directory
   :default: /opt/squid

Path to the directory where the docker-compose-files from Squid will be stored.

.. zuul:rolevar:: squid_host
   :default: 127.0.0.1

The host where Squid will be reachable.

.. zuul:rolevar:: squid_port
   :default: 3128

Port which Squid will be used for connections from outside.

.. zuul:rolevar:: squid_tag
   :default: 5.7-23.04_beta

Version from Squid in form of a tag which should be used.

.. zuul:rolevar:: squid_image
   :default: {{ docker_registry_squid }}/ubuntu/squid:{{ squid_tag }}

The container image to use.

.. zuul:rolevar:: squid_container_name
   :default: squid

Name of the container in which Squid will run.

.. zuul:rolevar:: squid_network
   :default: 172.31.101.144/28

The subnet for Squid in the docker-compose file.

.. zuul:rolevar:: squid_service_name
   :default: docker-compose@squid

Name from the Squid service to deal with it.


**Urls for the services**

The following Variables define the urls to the webservices that OSISM provides:

.. zuul:rolevar:: homer_url_ara
   :default: http://{{ ara_server_host | default(ansible_default_ipv4.address) }}:{{ ara_server_port | default(8120) }}
