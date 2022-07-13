This ansible role will installing and configuring Chrony.

**Role Variables**

.. zuul:rolevar:: chrony_package_name
   :default: chrony

Package name of the required package for the installation of Chrony.

.. zuul:rolevar:: configuration_directory
   :default: /opt/configuration

Path to the directory which will contains the configuration files.

.. zuul:rolevar:: chrony_local_conf_template
   :default: "{{ configuration_directory }}/environments/generic/templates/chrony.conf.j2"

Path to the template-configuration-file.

.. zuul:rolevar:: chrony_servers
   :default: - 0.de.pool.ntp.org
             - 1.de.pool.ntp.org
             - 2.de.pool.ntp.org
             - 3.de.pool.ntp.org

List with NTP server which should be used.

.. zuul:rolevar:: chrony_server_options
   :default: iburst

NTP server options.

.. zuul:rolevar:: chrony_sync_rtc
   :default: false

Configure Chrony to synchronize the hardware clock.

.. zuul:rolevar:: chrony_allowed_subnets
   :default: - 10/8
             - 192.168/16
             - 172.16/12

Chrony limits access to clients that are on certain subnets.  Adjust the
following subnets here to limit client access to chrony servers.

.. zuul:rolevar:: chrony_bind_local_interfaces_only
   :default: true

If set to true, chronyd will never open the server port and will operate
strictly in a client-only mode.

.. zuul:rolevar:: chrony_bindaddresses
   :default: []

Bind Chrony to specific addresses
NOTE: It is only possible to set at most one IPv4 and one IPv6 address.
