Ansible role for installation and configuration of FRRouting.

**Role Variables**

.. zuul:rolevar:: frr_package_name
   :default: frr

The package name for FRRouting.

.. zuul:rolevar:: frr_service_name
   :default: frr

Service name for FRRouting.

.. zuul:rolevar:: frr_sysctl_defaults
   :default: - name: net.ipv4.ip_forward
               value: 1
             - name: net.ipv4.conf.all.send_redirects
               value: 0
             - name: net.ipv4.conf.all.accept_redirects
               value: 0
             - name: net.ipv4.fib_multipath_hash_policy
               value: 1
             - name: net.ipv4.conf.default.ignore_routes_with_linkdown
               value: 1
             - name: net.ipv4.conf.all.rp_filter
               value: 2

Have a look at frr_sysctl.

.. zuul:rolevar:: frr_sysctl_extra
   :default: []

Have a look at frr_sysctl.

.. zuul:rolevar:: frr_sysctl
   :default: frr_sysctl_defaults + frr_sysctl_extra

A list with kernel parameters for FRRouting.

.. zuul:rolevar:: frr_dummy_interface

.. zuul:rolevar:: frr_interfaces

.. zuul:rolevar:: frr_local_as

.. zuul:rolevar:: frr_remote_as
