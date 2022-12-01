Ansible role for installing Virtualbmc.
Virtualbmc is a bare metall controller for virtual machines.

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

.. zuul:rolevar:: docker_registry_virtualbmc
   :default: quay.io

The registry for the Virtualbmc Docker container.


**Virtualbmc Variables**

.. zuul:rolevar:: virtualbmc_container_name
   :default: virtualbmc

Name of the container in which Virtualbmc will run.

.. zuul:rolevar:: virtualbmc_configuration_directory
   :default: /opt/virtualbmc/configuration

In this directory the configuration files for Virtualbmc will be stored.

.. zuul:rolevar:: virtualbmc_docker_compose_directory
   :default: /opt/virtualbmc

Path to the directory where the docker-compose-files from Virtualbmc will
be stored.

.. zuul:rolevar:: virtualbmc_network
   :default: 172.31.101.128/28

The network to use for the Virtualbmc container.

.. zuul:rolevar:: virtualbmc_service_name
   :default: docker-compose@virtualbmc

Name from the Virtualbmc service to deal with it.

.. zuul:rolevar:: virtualbmc_host
   :default: 127.0.0.1

The host where Virtualbmc will be reachable.

.. zuul:rolevar:: virtualbmc_port
   :default: 6230-6239

Port which Virtualbmc will use for connections from outside.

.. zuul:rolevar:: virtualbmc_tag
   :default: 2.2.1

Version from the Virtualbmc which should be installed.

.. zuul:rolevar:: virtualbmc_image
   :default: {{ docker_registry_virtualbmc }}/osism/virtualbmc:{{ virtualbmc_tag }}

The container image to use.
