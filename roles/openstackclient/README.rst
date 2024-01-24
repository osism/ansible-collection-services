This ansbile role install the OpenStackClient.
OpenStackClient is a command-line client for OpenStack that brings the
command set for Compute, Identity, Image, Object Storage and Block Storage APIs
together in a single shell with a uniform command structure.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry_openstackclient
   :default: quay.io

The registry for the OpenStackClient Docker container.

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Openstackclient Variables**

.. zuul:rolevar:: openstackclient_install_type
   :default: container

Which type for instalation you prefer to use.
The values that can be used are ``package`` or ``container``.

.. zuul:rolevar:: openstackclient_version
   :default: xena

The Version from the OpenStackClient which should used.


**Container Variables**

.. zuul:rolevar:: openstackclient_configuration_directory
   :default: /opt/openstackclient/configuration

In this directory the configuration files for OpenStackClient will be stored.

.. zuul:rolevar:: openstackclient_data_directory
   :default: /opt/openstackclient/data

Directory where the data for the OpenStackClient will be stored.

.. zuul:rolevar:: openstackclient_docker_compose_directory
   :default: /opt/openstackclient

Path to the directory where the docker-compose-files from OpenStackClient
will be stored.

.. zuul:rolevar:: openstackclient_tag
   :default: {{ openstackclient_version }}

Version from the OpenStackClient which should be installed.

.. zuul:rolevar:: openstackclient_image
   :default: {{ docker_registry_openstackclient }}/osism/openstackclient:{{ openstackclient_tag }}

The container image to use.

.. zuul:rolevar:: openstackclient_container_name
   :default: openstackclient

Name of the container in which OpenStackClient will run.

.. zuul:rolevar:: openstackclient_network
   :default: 172.31.100.16/28

The network to use for the OpenStackClient container.

.. zuul:rolevar:: openstackclient_service_name
   :default: docker-compose@openstackclient

The network to use for the OpenStackClient container.


**Package Variables**

.. zuul:rolevar:: openstackclient_configure_repository
   :default: true

Configure the system for installing OpenStackClient. Install dependencies,
add the repository key and the repository itselfs.

.. zuul:rolevar:: openstackclient_debian_repository_key
   :default: 391A9AA2147192839E9DB0315EDB1B62EC4926EA

The url from which you will get the package.

.. zuul:rolevar:: openstackclient_debian_repository
   :default: deb
             http://ubuntu-cloud.archive.canonical.com/ubuntu
             {{ ansible_distribution_release }}-updates/
             {{ openstackclient_version }} main

Name of the OpenStackClient debian repository.

.. zuul:rolevar:: openstackclient_debian_packages
   :default: - python3-openstackclient
             - python3-heatclient
             - python3-magnumclient

Required packages for installing OpenStackClient.
