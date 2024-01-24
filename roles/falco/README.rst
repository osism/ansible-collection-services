This ansible role installs Falco.

**Role Variables**

.. zuul:rolevar:: falco_configuration_files
   :default: netdata.conf

Configuration file for falco.

.. zuul:rolevar:: falco_service_name
   :default: falco

Service name for Falco.

.. zuul:rolevar:: falco_package_name
   :default: falco

The name of the package for Falco.

.. zuul:rolevar:: falco_configure_repository
   :default: false

Configure the system for installing Falco. Install dependencies, add
the repository key and the repository itselfs. As default it is disabled.


.. zuul:rolevar:: falco_debian_repository_key
   :default: https://falco.org/repo/falcosecurity-3672BA8F.asc

The url from which you will get the repository-key.

.. zuul:rolevar:: falco_debian_repository
   :default: deb
             https://dl.bintray.com/falcosecurity/deb stable main

Name from the required package for the Falco installation.
