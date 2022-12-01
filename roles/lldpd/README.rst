Ansible role for the Lldpd insatllation.
Lldpd is a daemon able to receive and send LLDP frames.

**Role Variables**

.. zuul:rolevar:: lldpd_package_name
   :default: lldpd

The name of the package for Lldpd.

.. zuul:rolevar:: lldpd_service_name
   :default: lldpd

Name from the Lldpd service to deal with it.
