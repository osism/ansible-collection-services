This ansible role install and configure Netdata.
Netdata is a tool for collecting system metrics and transform these in
visualize these metrics in real-time.

**Role Variables**

.. zuul:rolevar:: netdata_configuration_files
   :default: - netdata.conf
             - stream.conf

Files for the Netdata configuration.

.. zuul:rolevar:: netdata_service_name
   :default: netdata

Service name for Netdata to deal with it.

.. zuul:rolevar:: netdata_package_name
   :default: netdata

Package for the installation of Netdata.

.. zuul:rolevar:: netdata_configure_repository
   :default: false

Configure the system for installing Netdata.

.. zuul:rolevar:: netdata_debian_repository_arch
   :default: amd64

Architecture from the target system.

.. zuul:rolevar:: netdata_debian_repository_key
   :default: https://packagecloud.io/netdata/netdata-edge/gpgkey
.. zuul:rolevar:: netdata_debian_repository
   :default: deb [ arch={{ netdata_debian_repository_arch }} ]
             https://packagecloud.io/netdata/netdata-edge/ubuntu/
             {{ ansible_distribution_release }} main

The url from which you will get the package.

.. zuul:rolevar:: netdata_host_type
   :default: client

The type of the host. Possible values: [client, server]

.. zuul:rolevar:: netdata_api_host
   :default: 127.0.0.1

IP address of the Netdata API.

.. zuul:rolevar:: netdata_api_port
   :default: 19999

Port for the Netdata API.

.. zuul:rolevar:: netdata_hostname
   :default: inventory_hostname_short

The short hostname provided from the ansible inventory.

.. zuul:rolevar:: netdata_update_every
   :default: 5

Intervall in seconds how often netdata should update the data

.. zuul:rolevar:: netdata_default_history
   :default: 3600

Default history size of past values

.. zuul:rolevar:: netdata_enable_cloud
   :default: false

Connect netdata daemons to the netdata cloud.

.. zuul:rolevar:: netdata_memory_mode
   :default: map

Mode in which the metrics are stored. Possible values:
dbengine, ram, save, map, none, alloc

.. zuul:rolevar:: netdata_sys_vm_max_map_count
   :default: 262120

NOTE: The more nodes streaming to the server the higher this value must
be set.

