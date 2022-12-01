Ansible Role for installation and configuration Auditd.
Auditd is used for collecting Package security messages and forwarding
them to a central server.

**Role Variables**

.. zuul:rolevar:: auditd_backup
   :default: false

Sets the backup to false. If true the role will make a backup from the
rule files. 

.. zuul:rolevar:: auditd_syslog
   :default: false

This varaible disables write to rsyslog for auditd.


**Variable for Configuration**

.. zuul:rolevar:: auditd_config

.. code-block:: yaml

   - parameter: active
     value: "{{ 'yes' if auditd_syslog|bool else 'no' }}"
     config: /etc/audisp/plugins.d/syslog.conf

Configuration for Auditd.


**Variables for Rules**

.. zuul:rolevar:: auditd_rules_path
   :default: /etc/audit/rules.d

Path to where the rules from Auditd should be stored.

.. zuul:rolevar:: auditd_rules_files_defaults
   :default: 20-neo23x0.rules

Look at: auditd_rules_files.

.. zuul:rolevar:: auditd_rules_files_extra

Look at: auditd_rules_files.

.. zuul:rolevar:: auditd_rules_files
   :default: auditd_rules_files_defaults + auditd_rules_files_extra

The configuration files for the rules of Auditd composed from the Variables
auditd_rules_files_defaults and auditd_rules_files_extra.


**Variables for Packages**

.. zuul:rolevar:: auditd_package_name
   :default: auditd

The required package for Auditd.

.. zuul:rolevar:: audispd_plugins_package_name
   :default: audispd-plugins

Plugins for Auditd.


**Variable for Services**

.. zuul:rolevar:: auditd_service_name
   :default: auditd

Service name to deal with the Auditd service.
