Ansible role for installing ang configuring Traefik.
Traefik is a reverse proxy and loadbalancer for managing microservices.

**Docker Variables**

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

The registry for the Traefik Docker container.

.. zuul:rolevar:: docker_registry_traefik
   :default: docker_registry

Look at ``docker_registry``.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Traefik Variables**

.. zuul:rolevar:: traefik_docker_compose_directory
   :default: /opt/traefik

Path to the directory where the docker-compose-files from Traefik will
be stored.

.. zuul:rolevar:: traefik_certificates_directory
   :default: /opt/traefik/certificates

Directory which strores the certificates.

.. zuul:rolevar:: traefik_configuration_directory
   :default: /opt/traefik/configuration

In this directory the configuration files for Traefik will be stored.

.. zuul:rolevar:: traefik_host
   :default: 127.0.0.1

The host where Traefik will be reachable.

.. zuul:rolevar:: traefik_port
   :default: 8122

This port is for the Traefik dashboard.

.. zuul:rolevar:: traefik_port_http
   :default: 80

Port which Traefik will use for connections from outside.

.. zuul:rolevar:: traefik_port_https
   :default: 443

Port which Traefik will use for connections from outside via https.

.. zuul:rolevar:: traefik_certificates
   :default: {}

If you want to add self-signed certificates you can do it here.

Example:

.. code-block:: yaml

   traefik_certificates
     dashboard:
       cert: "-----BEGIN CERTIFICATE-----..."
       key: "-----BEGIN PRIVATE KEY-----..."

.. zuul:rolevar:: traefik_tag
   :default: v2.7.0

Version from the Traefik which should be installed.

.. zuul:rolevar:: traefik_image
   :default: {{ docker_registry_traefik }}/traefik:{{ traefik_tag }}

The container image to use.

.. zuul:rolevar:: traefik_container_name
   :default: traefik

Container name for the Traefik service.

.. zuul:rolevar:: traefik_service_name
   :default: docker-compose@traefik

Name from the Traefik service to deal with it.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Network name of the external network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.

.. zuul:rolevar:: traefik_pilot_dashboard
   :default: false

Disable the Traefik dashboard.

.. zuul:rolevar:: traefik_log_level
   :default: INFO

Level of detail for the log messages.
