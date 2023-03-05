With this role you can install and configure hddtmp/lm-sensors.
This tool checks the temperature of a block device.

**Role Variables**

.. zuul:rolevar:: hddtemp_conf_file

Path to configuration file.


**Hddtemp Variables**

.. zuul:rolevar:: RUN_DAEMON
   :default: true

Hddtemp network daemon switch. If set to true, hddtemp will listen
for incoming connections.

.. zuul:rolevar:: DISKS
   :default: /dev/hda

List of devices you want to use with hddtemp. If none specified,
hddtemp will probe standard devices.

.. zuul:rolevar:: DISKS_NOPROBE
   :default: ""

List of devices you want to use with hddtemp, but that would not be
probed for a working sensor.

.. zuul:rolevar:: INTERFACE
   :default: 127.0.0.1

IP address of the interface on which you want hddtemp to be bound
on. If none specified, goes to 127.0.0.1. Use 0.0.0.0 to bind hddtemp
on all interfaces.

.. zuul:rolevar:: PORT
   :default: 7634

Port number on which you want hddtemp to listen on. If none specified,
the port 7634 is used.

.. zuul:rolevar:: DATABASE
   :default: /etc/hddtemp.db

Database file to use. If none specified, /etc/hddtemp.db is used.

.. zuul:rolevar:: SEPARATOR
   :default: |

Separator to use between fields. The default separator is '|'.

.. zuul:rolevar:: RUN_SYSLOG
   :default: 0

Logging period (in seconds) for the temperatures. If set to a value
different than 0, hddtemp will run as a daemon periodically logging
the temperatures through syslog.

.. zuul:rolevar:: OPTIONS

Other options to pass to hddtemp.
