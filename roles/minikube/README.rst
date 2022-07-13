This ansible role installs Minikube.
Minikube is a tool to let a single node Kubernetes cluster run on your system.

**Role Variables**

.. zuul:rolevar:: minikube_service_user
   :default: {{ operator_user | default('dragon') }}

User for the Minicube service.

.. zuul:rolevar:: minikube_service_group
   :default: {{ operator_group | default('dragon') }}

Group for the user of the Minicube service.

.. zuul:rolevar:: minikube_driver
   :default: docker

Run driver for Minikube installation.

.. zuul:rolevar:: minikube_service_name
   :default: minikube

Name from the Minicube service to deal with it.

.. zuul:rolevar:: minikube_version
   :default: 1.18.1

Version from Minicube which should be used.

.. zuul:rolevar:: minikube_package_url
   :default: https://github.com/kubernetes/minikube/releases/download/
             v{{ minikube_version }}/minikube_{{ minikube_version }}-0_amd64.deb

The url from which you will get the package for Minicube.
