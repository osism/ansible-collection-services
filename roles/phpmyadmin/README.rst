Ansible role to install and configure Phpmyadmin.
Phpmyadmin is a tool to manage MySQL and MariaDB database over the web.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

Have a look at ``docker_registry_phpmyadmin``

.. zuul:rolevar:: docker_registry_phpmyadmin
   :default: docker_registry

The registry for the Phpmyadmin Docker container.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Phpmyadmin Variables**

.. zuul:rolevar:: phpmyadmin_docker_compose_directory
   :default: /opt/phpmyadmin

Path to the directory where the docker-compose-files from Phpmyadmin will
be stored.

.. zuul:rolevar:: phpmyadmin_host
   :default: 127.0.0.1

The host where Phpmyadmin will be reachable.

.. zuul:rolevar:: phpmyadmin_database_host
   :default: 127.0.0.1

Host for the database.

.. zuul:rolevar:: phpmyadmin_port
   :default: 8110

Port which Phpmyadmin will use for connections from outside.

.. zuul:rolevar:: phpmyadmin_tag
   :default: 5.2

Version from the Phpmyadmin which should be installed.

.. zuul:rolevar:: phpmyadmin_image
   :default: {{ docker_registry_phpmyadmin }}
             /phpmyadmin/phpmyadmin:{{ phpmyadmin_tag }}

The container image to use.

.. zuul:rolevar:: phpmyadmin_network
   :default: 172.31.100.32/28

The network to use for the Phpmyadmin container.

.. zuul:rolevar:: phpmyadmin_service_name
   :default: docker-compose@phpmyadmin

Name from the Phpmyadmin service to deal with it.


**Traefik Variables**

.. zuul:rolevar:: phpmyadmin_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of Phpmyadmin network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
