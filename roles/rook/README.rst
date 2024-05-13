Ansible role for installation and configuration of the Rook operator.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.

**Rook Variables**

.. zuul:rolevar:: container_registry_rook
   :default: index.docker.io

Path to the registry that stores the container images for the rook operator.

.. zuul:rolevar:: rook_image
   :default: {{ container_registry_rook }}/rook/ceph

The container image to use.

.. zuul:rolevar:: rook_image_tag
   :default: v1.13.5

Version from rook operator in form of a tag which should be used.

.. zuul:rolevar:: rook_work_directory
   :default: /tmp/rook/configuration

Work directory inside the osism-ansible container.

.. zuul:rolevar:: rook_template_directory
   :default: .

Template directory containing `operator.yml`, e.g. OSISM configuration directory.

.. zuul:rolevar:: rook_namespace
   :default: .

Kubernetes namespace in which the operator should be installed. 
Also see https://rook.io/docs/rook/v1.13/Storage-Configuration/Advanced/ceph-configuration/?h=#using-alternate-namespaces
