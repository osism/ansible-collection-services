This ansible role installs osquery. osquery uses basic SQL commands
to leverage a relational data-model to describe a device.

**Role Variables**

.. zuul:rolevar:: osquery_service_name
   :default: osqueryd

Service name for osquery.

.. zuul:rolevar:: osquery_package_name
   :default: osquery

The name of the package for osquery.

.. zuul:rolevar:: osquery_configure_repository
   :default: true

Prepare the system for installing osquery. Add the repository key
and the repository itself.


.. zuul:rolevar:: osquery_debian_repository_key
   :default: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x1484120ac4e9f8a1a577aeee97a80c63c9d8b80b

URL that points to the osquery repository key.

.. zuul:rolevar:: osquery_debian_repository
   :default: deb
             https://pkg.osquery.io/deb deb main

URL that points to the osquery repository.
