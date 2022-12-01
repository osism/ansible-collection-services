This ansible role will install and configure Cgit and Traefik for Cgit.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_cgit
   :default: quay.io

Path to the registry that stores the Docker container images for Cgit.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and handles with Docker.


**Cgit Variables**

.. zuul:rolevar:: cgit_docker_compose_directory
   :default: /opt/cgit

The path where the docker-compose-files for Cgit will be stored.

.. zuul:rolevar:: cgit_configuration_directory
   :default: /opt/cgit/configuration

Directory in which the configuration files for Cgit will be stored.

.. zuul:rolevar:: cgit_host
   :default: 127.0.0.1

The host where Cgit will be reachable.

.. zuul:rolevar:: cgit_port
   :default: 8210

For connections Cgit will use the configured port.

.. zuul:rolevar:: cgit_tag
   :default: 1.2.3

The version from Cgit in form of a tag which should be used.

.. zuul:rolevar:: cgit_image
   :default: {{ docker_registry_cgit }}/osism/cgit:{{ cgit_tag }}

Container image which will be used.

.. zuul:rolevar:: cgit_network
   :default: 172.31.101.112/28

The subnet for Cgit in the docker-compose file.

.. zuul:rolevar:: cgit_service_name
   :default: docker-compose@cgit

Name from the Cgit service to deal with it.

.. zuul:rolevar:: cgit_repositories_defaults

.. code-block:: yaml

    configuration: /opt/configuration/.git
    inventory: /var/lib/docker/volumes/manager_inventory_reconciler/_data/.git
    netbox: /opt/state/netbox/.git

Have a look at: cgit_repositories.

.. zuul:rolevar:: cgit_repositories_extra
   :default: {}

Have a look at: cgit_repositories.

.. zuul:rolevar:: cgit_repositories
   :default: cgit_repositories_defaults|combine(cgit_repositories_extra)

The repositories which are required for the installation of Cgit.


**Traefik Variables**

.. zuul:rolevar:: cgit_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of the Docker network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
