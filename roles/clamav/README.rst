Clamav is a free virusscanner for Linux based distributions.
This role will install and configure Clamav.

**Role Variables**

.. zuul:rolevar:: clamav_configuration_defaults

.. code-block:: yaml

    - regexp: '^.*Example$'
      state: absent
    - regexp: '^.*LocalSocket .*$'
      line: 'LocalSocket {{ clamav_localsocket }}'

Have a look at clamav_configuration.

.. zuul:rolevar:: clamav_configuration_extra
   :default: []

Have a look at clamav_configuration.

.. zuul:rolevar:: clamav_configuration
   :default: clamav_configuration_defaults + clamav_configuration_extra

Here you can specify which things you want to change in the Clamav configuration.

.. zuul:rolevar:: clamav_package_names

Required packages for Clamav.

.. zuul:rolevar:: clamav_localsocket

The directory where the socket will be stored in.

.. zuul:rolevar:: clamav_configuration_path

Path to the configuration files.

.. zuul:rolevar:: clamav_daemon_service_name

Service name for handling the Clamav service.

.. zuul:rolevar:: clamav_freshclam_service_name

Freshclam is required for automaticly update the database from Clamav.
