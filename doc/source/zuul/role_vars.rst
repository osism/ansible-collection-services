Ansible Role Variables for the Zuul Role
========================================

Generic Variables
-----------------

.. zuul:rolevar:: zuul_user
      :default: zuul

The Unix user name to be used for the Zuul installation.

.. zuul:rolevar:: zuul_logserver_fqdn
      :default: "logs.example.org"

The FQDN that is to be used for the logserver vhost.

.. zuul:rolevar:: zuul_webserver_fqdn
      :default: "zuul.example.org"

The FQDN that is to be used for the Zuul webserver vhost.

.. zuul:rolevar:: zuul_webserver_admin
      :default: "admin@example.org"

The email address that is to be shown as webserver admin.

.. zuul:rolevar:: zookeeper_fqdn
      :default: "zookeeper01.example.org"

The FQDN that is to be used for the Zookeeper server.

.. zuul:rolevar:: base_conf_dir
      :default: /opt/zuul

The base configuration directory which will contain the docker-compose
configuration and by default all the service-specific configuration
directories.
