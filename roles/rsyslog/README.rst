Role to install and configure rsyslog.

**Role Variables**

.. zuul:rolevar:: rsyslog_service_name
   :default: rsyslog

Name of the rsyslog service.

.. zuul:rolevar:: rsyslog_package_name
   :default: rsyslog

Name of the rsyslog package.

.. zuul:rolevar:: rsyslog_fluentd
   :default: true

Enable redirection to fluentd service.

.. zuul:rolevar:: rsyslog_fluentd_host
   :default: 127.0.0.1

Address of fluentd service.

.. zuul:rolevar:: rsyslog_fluentd_port
   :default: 5140

Port of fluentd service.

.. zuul:rolevar:: rsyslog_additional_host
   :default:

Address of external rsyslog service.

.. zuul:rolevar:: rsyslog_additional_port
   :default: 5140

Port of external rsyslog service.

.. zuul:rolevar:: rsyslog_additional_protocol
   :default: udp

Protocol of external rsyslog service.
