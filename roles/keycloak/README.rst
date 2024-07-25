Ansible role for installation and configuration keycloak and all its
components. Keycloak is an Identity and Access Management (IAM) tool. 

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.

**Keycloak Variables**

.. zuul:rolevar:: container_registry_keycloak
   :default: registry.scs.community

Path to the registry that stores the container images for Keycloak.

.. zuul:rolevar:: keycloak_image
   :default: {{ container_registry_keycloak }}/scs-container-images/scs-keycloak

The container image to use.

.. zuul:rolevar:: keycloak_image_tag
   :default: 23.0.6

Version from Keycloak in form of a tag which should be used.

.. zuul:rolevar:: keycloak_configuration_directory
   :default: /tmp/keycloak/configuration

Work directory inside the osism-ansible container.

.. zuul:rolevar:: keycloak_tls_certificates_directory
   :default: /opt/configuration/environments/infrastructure/files/keycloak

This directory will be used to pass the TLS certiciates used for external access.
The custom certificates need to be readable from within the osism-ansible container.

.. zuul:rolevar:: keycloak_tls_key
   :default: "{{ keycloak_tls_certificates_directory }}/private_key.pem"

The private TLS key, should be vault protected.
See osism/testbed/contrib/ownca/README.md

.. zuul:rolevar:: keycloak_tls_certchain
   :default: "{{ keycloak_tls_certificates_directory }}/cert.crt"

The public TLS certificate chain.
See osism/testbed/contrib/ownca/README.md

.. zuul:rolevar:: keycloak_host
   :default: 127.0.0.1

The host where Keycloak will be reachable.

.. zuul:rolevar:: keycloak_port
   :default: 8170

Port which Keycloak will use for connections from outside.

.. zuul:rolevar:: keycloak_username
   :default: admin

Default login user name for the first login.
You should change it for more security.

.. zuul:rolevar:: keycloak_password
   :default: password

Password for the first login.
For more security you should change it after the first login.


**Postgres Variables**

The container image to use.

.. zuul:rolevar:: keycloak_postgres_password
   :default: password

Password for the first login.
For more security you should change it after the first login.

.. zuul:rolevar:: keycloak_postgres_username
   :default: keycloak

Default login user name for the first login.
You should change it for more security.

.. zuul:rolevar:: keycloak_postgres_databasename
   :default: keycloak

The name for the Postgres database from Keycloak.

**k3s/metallb Variables**

.. zuul:rolevar:: metallb_keycloak_external_IP
   :default: 192.168.16.100

Public IP for Keycloak.

## Importing custom CA\'s into Keycloak

To import your custom CA\'s into Keycloak the operator should copy the CA file into the next directory

`{{ keycloak_tls_certificates_directory }}/certs`

This will be loaded into Keycloak during the deployment.
