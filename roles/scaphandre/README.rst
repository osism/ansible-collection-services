Ansible role for the deployment of the Scaphandre exporter.

Scaphandre is a metrology agent dedicated to electrical power consumption metrics.

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

.. zuul:rolevar:: docker_registry_scaphandre
   :default: index.docker.io

The registry for the Scaphandre container image.


**Scaphandre Variables**

.. zuul:rolevar:: scaphandre_container_name
   :default: scaphandre

Name of the container in which Scaphandre will run.

.. zuul:rolevar:: scaphandre_configuration_directory
   :default: /opt/scaphandre/configuration

In this directory the configuration files for Scaphandre will be stored.

.. zuul:rolevar:: scaphandre_docker_compose_directory
   :default: /opt/scaphandre

Path to the directory where the Docker Compose file from Scaphandre will
be stored.

.. zuul:rolevar:: scaphandre_network
   :default: 172.31.101.160/28

The network to use for the Scaphandre container.

.. zuul:rolevar:: scaphandre_service_name
   :default: docker-compose@scaphandre

Name from the Scaphandre service to deal with it.

.. zuul:rolevar:: scaphandre_host
   :default: 127.0.0.1

The host where Scaphandre will be reachable.

.. zuul:rolevar:: scaphandre_port
   :default: 9155

Port which Scaphandre will use for connections from outside.

.. zuul:rolevar:: scaphandre_tag
   :default: 0.5.0

Version from the Scaphandre which should be installed.

.. zuul:rolevar:: scaphandre_image
   :default: {{ docker_registry_scaphandre }}/hubblo/scaphandre:{{ scaphandre_tag }}

The container image to use.

.. zuul:rolevar:: scaphandre_exporter
   :default: prometheus

Exporter to launch.

.. zuul:rolevar:: scaphandre_flags_extra
   :default: []

Extra flags.

.. zuul:rolevar:: scaphandre_flags_defaults

.. code-block:: yaml

   - "--qemu"

Default flags.

.. zuul:rolevar:: scaphandre_flags
   :default: "{{ scaphandre_flags_defaults + scaphandre_flags_extra }}"

Merged flags (default + extra)
