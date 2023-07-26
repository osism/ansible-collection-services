Ansible Role for installation and configuration from the metering.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and
handles with Docker.


**Container Variables**

.. zuul:rolevar:: metering_configuration_directory
   :default: /opt/metering/configuration

The directory where the configuration for the metering will be stored.

.. zuul:rolevar:: metering_data_directory
   :default: /opt/metering/data

Data from the metering will be stored there.

.. zuul:rolevar:: metering_docker_compose_directory
   :default: /opt/metering

Path to where the docker-compose-files from metering will be stored.

.. zuul:rolevar:: metering_tag
   :default: metering_version

The version from metering in form of a tag which should be used.

.. zuul:rolevar:: metering_image
   :default: "metering:{{ metering_tag }}"

The container image to use.

.. zuul:rolevar:: metering_container_name
   :default: metering

Container name for the metering.

.. zuul:rolevar:: metering_network
   :default: 172.31.100.16/28

The subnet for metering in the docker-compose file.

.. zuul:rolevar:: metering_service_name
   :default: docker-compose@metering

Name from the metering service to deal with it.
