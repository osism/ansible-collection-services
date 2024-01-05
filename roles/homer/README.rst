This ansible role install and configure Homer.
Homer is a dashboard for that collects various managing tools.

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

.. zuul:rolevar:: docker_registry_homer
   :default: quay.io

Path to the registry that stores the Docker container images for Homer.

.. zuul:rolevar:: homer_configuration_directory
   :default: /opt/homer/configuration

In this directory the configuration files will be stored.

.. zuul:rolevar:: homer_docker_compose_directory
   :default: /opt/homer

Path to the directory where the docker-compose-files from Homer will be stored.

.. zuul:rolevar:: homer_host
   :default: 127.0.0.1

The host where Homer will be reachable.

.. zuul:rolevar:: homer_port
   :default: 8080

Port which Homer will be used for connections from outside.

.. zuul:rolevar:: homer_tag
   :default: 22.02.2

Version from Homer in form of a tag which should be used.

.. zuul:rolevar:: homer_image
   :default: {{ docker_registry_homer }}/osism/homer:{{ homer_tag }}

The container image to use.

.. zuul:rolevar:: homer_container_name
   :default: homer

Name of the container in which Homer will run.

.. zuul:rolevar:: homer_network
   :default: 172.31.100.208/28

The subnet for Homer in the docker-compose file.

.. zuul:rolevar:: homer_service_name
   :default: docker-compose@homer

Name from the Homer service to deal with it.


**Urls for the services**

The following Variables define the urls to the webservices that OSISM provides:

.. zuul:rolevar:: homer_url_ara
   :default: http://{{ ara_server_host | default(ansible_default_ipv4.address) }}:{{ ara_server_port | default(8120) }}

.. zuul:rolevar:: homer_url_ceph
   :default: http://{{ kolla_internal_vip_address }}:8140

.. zuul:rolevar:: homer_url_flower
   :default: http://{{ flower_host | default(ansible_default_ipv4.address) }}:{{ flower_port | default(5555) }}

.. zuul:rolevar:: homer_url_grafana
   :default: http://{{ kolla_internal_vip_address }}:3000

.. zuul:rolevar:: homer_url_horizon
   :default: http://{{ kolla_internal_vip_address }}

.. zuul:rolevar:: homer_url_keycloak
   :default: http://{{ keycloak_host | default(ansible_default_ipv4.address) }}:{{ keycloak_port | default(8170) }}

.. zuul:rolevar:: homer_url_opensearch_dashboards
   :default: http://{{ kolla_internal_vip_address }}:5601

.. zuul:rolevar:: homer_url_netbox
   :default: http://{{ netbox_host | default(ansible_default_ipv4.address) }}:{{ netbox_port | default(8121) }}

.. zuul:rolevar:: homer_url_netdata
   :default: http://{{ netdata_host | default(ansible_default_ipv4.address) }}:{{ netdata_port | default(19999) }}

.. zuul:rolevar:: homer_url_phpmyadmin
   :default: http://{{ phpmyadmin_host | default(ansible_default_ipv4.address) }}:{{ phpmyadmin_port | default(8110) }}

.. zuul:rolevar:: homer_url_prometheus
   :default: http://{{ kolla_internal_vip_address }}:9090

.. zuul:rolevar:: homer_url_rabbitmq
   :default: http://{{ kolla_internal_vip_address }}:15672

.. zuul:rolevar:: homer_url_vault
   :default: http://{{ vault_host | default(ansible_default_ipv4.address) }}:{{ vault_port | default(8200) }}


**Traefik Variables**

.. zuul:rolevar:: homer_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of the Docker network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
