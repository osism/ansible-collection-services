This ansible role install and configure the Openstack-health-monitor.
Openstack-health-monitor is an external programm that monitors
Openstack API endpoints.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry_openstack_health_monitor
   :default: quay.io

The registry for the Openstack-health-monitor Docker container.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Common Variables**

.. zuul:rolevar:: openstack_health_monitor_install_type
   :default: container

Which type for instalation you prefer to use.
The values that can be used are ``package`` or ``container``.

.. zuul:rolevar:: openstack_health_monitor_clouds_yml_path
   :default: /opt/configuration/environments/openstack/clouds.yml

Path to the clouds.yml.

.. zuul:rolevar:: openstack_health_monitor_secure_yml_path
   :default: /opt/configuration/environments/openstack/secure.yml

Credentials for the clouds.yml configured in the secure.yml.


**Configuration Variables**

These are variables for the openstack-health-monitor:

.. zuul:rolevar:: openstack_health_monitor_ADDJHVOLSIZE
   :default: 0
.. zuul:rolevar:: openstack_health_monitor_ADDVMVOLSIZE
   :default: 0
.. zuul:rolevar:: openstack_health_monitor_AZS
   :default: nova
.. zuul:rolevar:: openstack_health_monitor_DATADIR
   :default: /data
.. zuul:rolevar:: openstack_health_monitor_FLAVOR
   :default: 1C-1GB-5GB
.. zuul:rolevar:: openstack_health_monitor_IMG
   :default: Ubuntu 20.04
.. zuul:rolevar:: openstack_health_monitor_JHFLAVOR
   :default: 1C-1GB-5GB
.. zuul:rolevar:: openstack_health_monitor_JHIMG
   :default: Ubuntu 20.04
.. zuul:rolevar:: openstack_health_monitor_OS_CLOUD
   :default: openstack_health_monitor
.. zuul:rolevar:: openstack_health_monitor_arguments
   :default: -O -C -D -N 1 -i 1 -n 2


**Cronjob Variables**

.. zuul:rolevar:: openstack_health_monitor_cronjob
   :default: false

Enable cronjob for healthcheck.

.. zuul:rolevar:: openstack_health_monitor_cronjob_minute
   :default: */10

Interval in minutes for healthcheck in the cronformat.

.. zuul:rolevar:: openstack_health_monitor_cronjob_hour
   :default: *

Interval in hours for healthcheck in the cronformat.


**Container Variables**

.. zuul:rolevar:: openstack_health_monitor_configuration_directory
   :default: /opt/openstack_health_monitor/configuration

In this directory the configuration files for Openstack-health-monitor
will be stored.

.. zuul:rolevar:: openstack_health_monitor_docker_compose_directory
   :default: /opt/openstack_health_monitor

Path to the directory where the docker-compose-files from Openstack-health-monitor
will be stored.

.. zuul:rolevar:: openstack_health_monitor_tag
   :default: v3.0.0

Version from the Openstack-health-monitor which should be installed.

.. zuul:rolevar:: openstack_health_monitor_image
   :default: {{ docker_registry_openstack_health_monitor }}/sovereigncloudstack
             /openstack-health-monitor:{{ openstack_health_monitor_tag }}

The container image to use.

.. zuul:rolevar:: openstack_health_monitor_container_name
   :default: openstack_health_monitor

Name of the container.

.. zuul:rolevar:: openstack_health_monitor_service_name
   :default: docker-compose@openstack_health_monitor

Name of the service.

.. zuul:rolevar:: openstack_health_monitor_network
   :default: 172.31.100.160/28

The network to use for the Openstack-health-monitor container.
