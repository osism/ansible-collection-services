This ansible role install and configure Openldap and its components.
Openldap is a tool that allows you to build and manage a LDAP directory.

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

.. zuul:rolevar:: docker_registry_openldap
   :default: quay.io

The registry for the Openldap Docker container.

.. zuul:rolevar:: docker_registry_umc
   :default: quay.io

Registry for the UMC Docker container.


**Openldap Variables**

.. zuul:rolevar:: openldap_configuration_directory
   :default: /opt/openldap/configuration

In this directory the configuration files for Openldap will be stored.

.. zuul:rolevar:: openldap_secrets_directory
   :default: /opt/openldap/secrets

This directory will store the secrets file.

.. zuul:rolevar:: openldap_docker_compose_directory
   :default: /opt/openldap

Path to the directory where the docker-compose-files from Openldap will
be stored.

.. zuul:rolevar:: openldap_network
   :default: 172.31.100.240/28

The network to use for the Openldap container.

.. zuul:rolevar:: openldap_container_name
   :default: openldap

Name of the container in which Openldap will run.

.. zuul:rolevar:: openldap_service_name
   :default: docker-compose@openldap

Name from the Openldap service to deal with it.

.. zuul:rolevar:: openldap_host
   :default: 127.0.0.1

The host where Openldap will be reachable.

.. zuul:rolevar:: openldap_ldap_port
   :default: 389

Port which Openldap will use for connections from outside.

.. zuul:rolevar:: openldap_ldaps_port
   :default: 636

Secure port which Openldap will use for connections.

.. zuul:rolevar:: openldap_tag
   :default: build-25862

Version of Openldap which should be used.

.. zuul:rolevar:: openldap_image
   :default: {{ docker_registry_openldap }}/univention/upx-ldap-server:{{ openldap_tag }}

The container image to use.

.. zuul:rolevar:: openldap_domain_name
   :default: osism.local

Configures the Ldap domain.

.. zuul:rolevar:: openldap_base_dn
   :default: dc=osism,dc=local

Defines the base dn string. 

.. zuul:rolevar:: openldap_password
   :default: password

Password for Openldap.

.. zuul:rolevar:: openldap_cacert_pem

# FIX ME

.. zuul:rolevar:: openldap_cert_pem

# FIX ME

.. zuul:rolevar:: openldap_private_key

# FIX ME

.. zuul:rolevar:: openldap_dh_parameters

# FIX ME


**UDM Variables**

.. zuul:rolevar:: udm_rest_host
   :default: 127.0.0.1

The host where UDM will be reachable.

.. zuul:rolevar:: udm_rest_port
   :default: 9979

Port which UDM will use for connections.

.. zuul:rolevar:: udm_rest_container_name
   :default: udm-rest

Name of the container in which UDM will run.

.. zuul:rolevar:: udm_rest_tag
   :default: build-24328

Version from UDM which should used.

.. zuul:rolevar:: udm_rest_image
   :default: {{ docker_registry_udm_rest }}/univention/upx-udm-rest:{{ udm_rest_tag }}

The container image to use.


**UMC Variables**

.. zuul:rolevar:: umc_web_host
   :default: 127.0.0.1

# FIX ME

.. zuul:rolevar:: umc_web_port
   :default: 8090

Port which UMC-web will use for connections.

.. zuul:rolevar:: umc_web_container_name
   :default: umc-web

Name of the container in which UMC-web will run.

.. zuul:rolevar:: umc_web_tag
   :default: build-24437

Version which should used.

.. zuul:rolevar:: umc_web_image
   :default: {{ docker_registry_umc }}/univention/upx-umc-web:{{ umc_web_tag }}

The container image to use.

.. zuul:rolevar:: umc_gateway_host
   :default: 127.0.0.1

# FIX ME

.. zuul:rolevar:: umc_gateway_http_port
   :default: 8191

HTTP port for UMC.

.. zuul:rolevar:: umc_gateway_https_port
   :default: 8192

HTTPS port for UMC.

.. zuul:rolevar:: umc_gateway_container_name
   :default: umc-gateway

Name of the container in which UMC-gateway will run.

.. zuul:rolevar:: umc_gateway_tag
   :default: build-24437

Version which should used.

.. zuul:rolevar:: umc_gateway_image
   :default: {{ docker_registry_umc }}/univention/upx-umc-gateway:{{ umc_gateway_tag }}

The container image to use.

.. zuul:rolevar:: umc_server_host
   :default: 127.0.0.1

The host where UMC will be reachable.

.. zuul:rolevar:: umc_server_port
   :default: 6670

Port which UMC will use for connections.

.. zuul:rolevar:: umc_server_container_name
   :default: umc-server

Name of the container in which UMC will run.

.. zuul:rolevar:: umc_server_tag
   :default: build-24437

Version of UMC which should used.

.. zuul:rolevar:: umc_server_image
   :default: {{ docker_registry_umc }}/univention/upx-umc-server:{{ umc_server_tag }}

The container image to use.
