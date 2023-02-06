Dnsdist is a loadbalancer with goal to route the traffic to the best server.
This role install and configure Dnsdist

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_dnsdist
   :default: quay.io

Path to the registry that stores the Docker container images for Dnsdist.

.. zuul:rolevar:: dnsdist_configuration_directory
   :default: /opt/dnsdist/configuration

Path to the directory which will contains the configuration files.

.. zuul:rolevar:: dnsdist_docker_compose_directory
   :default: /opt/dnsdist

Directory which contains the docker-compose-files for Dnsdist.

.. zuul:rolevar:: dnsdist_network
   :default: 172.31.101.80/28

The subnet for Dnsdist in the docker-compose file.

.. zuul:rolevar:: dnsdist_service_name
   :default: docker-compose@dnsdist

Name from the Dnsdist service to deal with it.

.. zuul:rolevar:: dnsdist_container_name
   :default: dnsdist

Name from the container in which Dnsdist will run.

.. zuul:rolevar:: dnsdist_host
   :default: 127.0.0.1

The host where Dnsdist will be reachable.

.. zuul:rolevar:: dnsdist_hosts
   :default: - "{{ dnsdist_host }}"

The hosts where Dnsdist will be reachable.

.. zuul:rolevar:: dnsdist_port
   :default: 1053

Port which Dnsdist will be used for connections from outside.

.. zuul:rolevar:: dnsdist_tag
   :default: 1.6.1

The version from Dnsdist in form of a tag which should be used.

.. zuul:rolevar:: dnsdist_image
   :default: {{ docker_registry_dnsdist }}/osism/dnsdist:{{ dnsdist_tag }}

The container image to use.

.. zuul:rolevar:: dnsdist_servers
   :default: - 208.67.222.222
             - 208.67.220.220
             - 208.67.222.220
             - 208.67.220.222

List of DNS servers to loadbalance.
