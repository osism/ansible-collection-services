Ansible role for installation and configuration of the Rook operator.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.

**Rook Variables**

.. zuul:rolevar:: container_registry_rook_operator
   :default: index.docker.io

Path to the registry that stores the container images for the rook operator.

.. zuul:rolevar:: rook_operator_image
   :default: {{ container_registry_rook_operator }}/rook/ceph

The container image to use.

.. zuul:rolevar:: rook_operator_image_tag
   :default: v1.13.5

Version from rook operator in form of a tag which should be used.

.. zuul:rolevar:: rook_operator_work_directory
   :default: /tmp/rook_operator/configuration

Work directory inside the osism-ansible container.

.. zuul:rolevar:: rook_operator_template_directory
   :default: .

Template directory containing `operator.yml`, e.g. OSISM configuration directory.

.. zuul:rolevar:: rook_operator_namespace
   :default: .

Kubernetes namespace in which the operator should be installed. 
Also see https://rook.io/docs/rook/v1.13/Storage-Configuration/Advanced/ceph-configuration/?h=#using-alternate-namespaces

.. zuul:rolevar:: rook_operator_enable_discovery_daemon
   :default: true

Enable discovery daemon.
Also see https://rook.io/docs/rook/v1.11/Storage-Configuration/Monitoring/ceph-dashboard/#visualization-of-physical-disks-section-in-the-dashboard

.. zuul:rolevar:: rook_operator_discovery_interval
   :default: "60m"

Configure discovery daemon interval.
Also see https://rook.io/docs/rook/v1.11/Storage-Configuration/Monitoring/ceph-dashboard/#visualization-of-physical-disks-section-in-the-dashboard
