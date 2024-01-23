Ansible role for installation and configuration of Docker and all required components.

**Role Variables**

.. zuul:rolevar:: docker_debug
   :default: false

Configure if Docker will start in the debug mode.

.. zuul:rolevar:: docker_experimental
   :default: false

Disables Docker experimental features. 

.. zuul:rolevar:: docker_live_restore
   :default: true

This enables that containers won't be shut down if the Daemon is unreachable.

.. zuul:rolevar:: docker_user
   :default: operator_user | default('dragon')

The user which docker will use for actions and which ownes the configuration directory.

.. zuul:rolevar:: docker_group
   :default: operator_group | default('dragon')

Group from the user.

.. zuul:rolevar:: docker_allow_restart
   :default: true

Enables the restart of the Docker daemon after reconfiguration.

.. zuul:rolevar:: docker_enforce_restart
   :default: false

Disables the enforcing the restart if the ``docker_enforce_restart`` value isn't true.

.. zuul:rolevar:: docker_ignore_restart_groupname
   :default: manager

Hosts that are protected from the restart. Can only be overwritten by ``docker_enforce_restart``.

.. zuul:rolevar:: docker_ipv6
   :default: false

Disables Dockers ipv6 capabilities.

.. zuul:rolevar:: docker_disable_default_network
   :default: false

Enables the default network from Docker.

.. zuul:rolevar:: docker_log_driver
   :default: json-file

Here you can configure the log output destination.

.. zuul:rolevar:: docker_log_level
   :default: info

Level of detail from the logs which you want to collect.

.. zuul:rolevar:: docker_log_opts
   :default: max-size: 10m
             max-file: 3

Options for the logging.

.. zuul:rolevar:: docker_hosts_defaults
   :default: "unix:///var/run/docker.sock"

Look at docker_hosts.

.. zuul:rolevar:: docker_hosts_extra
   :default: []

Look at docker_hosts.

.. zuul:rolevar:: docker_hosts
   :default: docker_hosts_defaults + docker_hosts_extra

A list of hosts on which the Docker Engine will be run.

.. zuul:rolevar:: docker_service_name
   :default: docker

Service name for Docker to deal with it.

.. zuul:rolevar:: containerd_service_name
   :default: containerd

For using Docker you will need the Containerd service too.
This declares the services from the Containerd.

.. zuul:rolevar:: docker_package_name
   :default: docker-ce

Package for the installation of Docker.

.. zuul:rolevar:: docker_cli_package_name
   :default: {{ docker_package_name }}-cli

Package name of the docker-cli.

.. zuul:rolevar:: containerd_package_name
   :default: containerd.io

The name of the package for Containerd.

.. note::

   By default this role uses the packages from Docker itself. Therefore the
   packages of Ubuntu must not be installed.
   To use the packages of Ubuntu the following parameters have to be adjusted.
   The repository of Docker should then also not be included
   docker_package_name: docker.io
   containerd_package_name: containerd
   docker_packages_fail: []

.. zuul:rolevar:: docker_packages_fail
   :default: - containerd
             - docker.io

Checks if the packages are installed or not. If them are installed, the
installation run will fail.

.. zuul:rolevar:: docker_python3_package_name
   :default: python3-docker

Required package for Python3-docker.

.. zuul:rolevar:: docker_python_package_name
   :default: python-docker

Package name for python-docker.

.. zuul:rolevar:: docker_python_package_names

This is a compose from the two variables before.

.. zuul:rolevar:: docker_python_install_from_pip
   :default: ansible_distribution_release == 'xenial'

If Xenial is the version of the distribution, Docker will be installed with
pip instead of apt.

.. zuul:rolevar:: docker_pip_package_name
   :default: docker

Package name of Docker for installation with pip.

.. zuul:rolevar:: docker_pip_extra_args

Here you can define extra arguments for pip.

.. zuul:rolevar:: docker_version
   :default: 5:20.10.16

This "5:" must be prepended starting with version 18.09.
Check available version under Ubuntu with apt-cache madison docker-ce.

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

Path to the registry that stores the Docker container images.

.. zuul:rolevar:: docker_insecure_registries
   :default: []

List of allowed insecure registries.

.. zuul:rolevar:: docker_registry_mirrors
   :default: []

The mirrors of registries which can be used.

.. zuul:rolevar:: docker_storage_driver
   :default: overlay2

Overlay2 is the default choice for Docker CE

.. zuul:rolevar:: docker_configure_storage_block_device
   :default: false

Disable the configuration of a storage block device with exclusive usage
for Docker.

.. zuul:rolevar:: docker_storage_block_device
   :default: /dev/sdb

On which device Docker will create the storage block device.

.. zuul:rolevar:: docker_storage_filesystem
   :default: ext4

The filesystem for the storage block device.

.. zuul:rolevar:: docker_storage_force
   :default: false

Disables the enforcement of configuring a filesystem.

.. zuul:rolevar:: docker_configure_proxy
   :default: false

Disables the proxy configuration for Docker.

.. zuul:rolevar:: docker_proxy_http
   :default: http://proxy.tld:8080

Docker proxy address.

.. zuul:rolevar:: docker_proxy_https
   :default: docker_proxy_http

Look at docker_proxy_http.

.. zuul:rolevar:: docker_proxy_no_proxy_default
   :default: - localhost
             - 127.0.0.1

Have a look at docker_proxy_no_proxy.

.. zuul:rolevar:: docker_proxy_no_proxy_extra
   :default: []

Have a look at docker_proxy_no_proxy.

.. zuul:rolevar:: docker_proxy_no_proxy
   :default: docker_proxy_no_proxy_default + docker_proxy_no_proxy_extra

A list of IP addresses which aren't transfered via the proxy.

.. zuul:rolevar:: docker_configure_repository
   :default: true

Configure the system for installing Docker. Install dependencies, add
the repository key and the repository itselfs.

.. zuul:rolevar:: docker_debian_repository_key
   :default: https://download.docker.com/linux/ubuntu/gpg

The url from which you will get the package.

.. zuul:rolevar:: docker_debian_repository
   :default: "deb
              https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }}
              stable"

Name of the Docker debian repository.

.. zuul:rolevar:: docker_default_runtime
   :default: runc

Container-execution-runtime which should be used.

.. zuul:rolevar:: containerd_grpc_gid
   :default: 42463

The group id for Go-lang RPC(Remote Procedure Call).

.. zuul:rolevar:: docker_opts
   :default: {}

Extra options for Docker.

.. zuul:rolevar:: docker_fact_files
   :default: - docker_containers
             - docker_images

Fact files for Docker images and containers.

.. zuul:rolevar:: docker_manage_containerd
   :default: true

Manage the containerd service with this role. Alternatively, osism.service.containerd
can be used for this.

.. zuul:rolevar:: docker_facts
   :default: true

Copy docker fact files.
