This ansible role install and configure rsyslog with fluentd.
Rsyslog transfer the log data to fluentd which makes the data more readable.

**Role Variables**

.. zuul:rolevar:: rsyslog_service_name
   :default: rsyslog

Name from the Rsyslog service to deal with it.

.. zuul:rolevar:: rsyslog_package_name
   :default: rsyslog

Package name from Rsyslog.

.. zuul:rolevar:: rsyslog_fluentd
   :default: true

Enable fluentd export.

.. zuul:rolevar:: rsyslog_fluentd_port
   :default: 5140

Fluentd server port.

.. zuul:rolevar:: rsyslog_fluentd_host
   :default: 127.0.0.1

Fluentd server IP.

.. zuul:rolevar:: fluentd_port
   :default: rsyslog_fluentd_port

Look at rsyslog_fluentd_port.

.. zuul:rolevar:: fluentd_host
   :default: rsyslog_fluentd_host

Look at rsyslog_fluentd_host.
