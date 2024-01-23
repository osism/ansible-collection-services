This role installs containerd.

**Role Variables**

.. zuul:rolevar:: containerd_service_name
   :default: containerd

Service name for containerd.

.. zuul:rolevar:: containerd_package_name
   :default: containerd

The name of the package for containerd.

.. zuul:rolevar:: containerd_configure_repository
   :default: true

Prepare the system for installing containerd. Add the repository key
and the repository itself.

.. zuul:rolevar:: docker_debian_repository_key
  :default: https://download.docker.com/linux/ubuntu/gpg

URL that points to the docker repository key.

.. zuul:rolevar:: docker_debian_repository
   :default: "deb
             https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }}
             stable"

URL that points to the docker repository.

.. zuul:rolevar:: containerd_grpc_gid
   :default: 42463

The group ID for GRPC.
