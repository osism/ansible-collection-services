Ansible role for the deployment of the Thanos sidecar.

Thanos sidecar is a component that gets deployed along with a Prometheus instance and
allow Thanos queriers to query Prometheus data.

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry_thanos_sidecar
   :default: quay.io

The registry for the Thanos sidecar container image.


**Thanos sidecar Variables**

.. zuul:rolevar:: thanos_sidecar_container_name
   :default: thanos_sidecar

Name of the container in which Thanos sidecar will run.

.. zuul:rolevar:: thanos_sidecar_configuration_directory
   :default: /opt/thanos_sidecar/configuration

In this directory the configuration files for Thanos sidecar will be stored.

.. zuul:rolevar:: thanos_sidecar_docker_compose_directory
   :default: /opt/thanos_sidecar

Path to the directory where the Docker Compose file from Thanos sidecar will
be stored.

.. zuul:rolevar:: thanos_sidecar_network
   :default: 172.31.101.192/28

The network to use for the Thanos sidecar container.

.. zuul:rolevar:: thanos_sidecar_service_name
   :default: docker-compose@thanos_sidecar

Name from the Thanos sidecar service to deal with it.

.. zuul:rolevar:: thanos_sidecar_prometheus_url
   :default: http://localhost:9090

The URL where Thanos sidecar will reach Prometheus's API.

.. zuul:rolevar:: thanos_sidecar_prometheus_http_client_config
   :default: {}

The Prometheus client configuration.

.. zuul:rolevar:: thanos_sidecar_host
   :default: 127.0.0.1

The host where Thanos sidecar will be reachable.

.. zuul:rolevar:: thanos_sidecar_grpc_port
   :default: 10901

Port where Thanos sidecar gRPC endpoint will be reachable from outside.

.. zuul:rolevar:: thanos_sidecar_http_port
   :default: 10902

Port where Thanos sidecar HTTP endpoint will be reachable from outside.

.. zuul:rolevar:: thanos_sidecar_tag
   :default: v0.32.5

Version from the Thanos sidecar which should be installed.

.. zuul:rolevar:: thanos_sidecar_image
   :default: {{ docker_registry_thanos_sidecar }}/thanos/thanos:{{ thanos_sidecar_tag }}

The container image to use.
