With this ansible role you can install and configure Jenkins.

**Role Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Because of Docker don't check the default MTU from the system it is nessecary
to set the MTU for Docker.

.. zuul:rolevar:: docker_registry_jenkins
   :default: registry.airgap.services.osism.tech

Path to the registry that stores the Docker container images for Jenkins.

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: jenkins_configuration_directory
   :default: /opt/jenkins/configuration

In this directory the configuration files will be stored.

.. zuul:rolevar:: jenkins_docker_compose_directory
   :default: /opt/jenkins

Path to the directory where the docker-compose-files from Jenkins will be stored.

.. zuul:rolevar:: jenkins_tag
   :default: 2

Version from Jenkins in form of a tag which should be used.

.. zuul:rolevar:: jenkins_image
   :default: {{ docker_registry_jenkins }}/osism/jenkins:{{ jenkins_tag }}

The container image to use.

.. zuul:rolevar:: jenkins_host
   :default: 127.0.0.1

The host where Jenkins will be reachable.

.. zuul:rolevar:: jenkins_port
   :default: 4441

Port which Jenkins will be used for connections from outside.

.. zuul:rolevar:: jenkins_network
   :default: 172.31.100.224/28

The subnet for Jenkins in the docker-compose file.

.. zuul:rolevar:: jenkins_password
   :default: password

Default password for the first login.

.. zuul:rolevar:: jenkins_username
   :default: jenkins

Username for the first login.

.. zuul:rolevar:: jenkins_disable_jenkins_initialization
   :default: no

The value should be a string. Possible values are ``no`` or ``yes``.
Disables the default configuration options. For more information have a look here:
https://github.com/bitnami/bitnami-docker-jenkins

.. zuul:rolevar:: jenkins_java_opts
   :default: ""

Here you can define java options.

.. zuul:rolevar:: jenkins_service_name
   :default: docker-compose@jenkins

Name from the Jenkins service to deal with it.
