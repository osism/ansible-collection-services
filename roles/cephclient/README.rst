Ansible Role for installation and configuration from the Cephclient.
You can choose between container installation and package installation.

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_cephclient
   :default: quay.io

Path to the registry that stores the Docker container images for Cephclient.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and
handles with Docker.


**Cephclient Variables**

.. zuul:rolevar:: cephclient_install_type
   :default: container

Which type for instalation you prefer to use.
The values that can be used are ``package`` or ``container``.

.. zuul:rolevar:: cephclient_version
   :default: pacific

Version of the Cephclient which will be used.

.. zuul:rolevar:: cephclient_mons

The monitoring systems to which the Cephclient will be connected.

.. zuul:rolevar:: cephclient_keyring

Certificate which the Cephclient will need to use for connections.

.. zuul:rolevar:: cephclient_keyring_name
   :default: client.admin

Name for the certificate to store in a directory.


**Container Variables**

.. zuul:rolevar:: cephclient_configuration_directory
   :default: /opt/cephclient/configuration

The directory where the configuration for the Cephclient will be stored.

.. zuul:rolevar:: cephclient_data_directory
   :default: /opt/cephclient/data

Data from the Cephclient will be stored there.

.. zuul:rolevar:: cephclient_docker_compose_directory
   :default: /opt/cephclient

Path to where the docker-compose-files from Cephclient will be stored.

.. zuul:rolevar:: cephclient_tag
   :default: cephclient_version

The version from Cephclient in form of a tag which should be used.

.. zuul:rolevar:: cephclient_image
   :default: {{ docker_registry_cephclient }}/osism/cephclient:{{ cephclient_tag }}

The container image to use.

.. zuul:rolevar:: cephclient_container_name
   :default: cephclient

Container name for the Cephclient.

.. zuul:rolevar:: cephclient_network
   :default: 172.31.100.0/28

The subnet for Cephclient in the docker-compose file. 

.. zuul:rolevar:: cephclient_service_name
   :default: docker-compose@cephclient

Name from the Cephclient service to deal with it.


**Package Variables**

.. zuul:rolevar:: cephclient_configure_repository
   :default: true

configures if the repository should be added or not.

.. zuul:rolevar:: cephclient_debian_repository_key
   :default: https://download.ceph.com/keys/release.asc

The url from which you will get the repository-key.

.. zuul:rolevar:: cephclient_debian_repository
   :default: "deb [ arch={{ cephclient_debian_repository_arch }} ] https://download.ceph.com/debian-{{ cephclient_version }} {{ ansible_distribution_release }} main"

Name of the Cephclient debian repository.

.. zuul:rolevar:: cephclient_debian_packages
   :default: ceph

Name from the required package for the Cephclient installation.
