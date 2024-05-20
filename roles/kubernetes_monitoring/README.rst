Ansible role for installation and configuration of the Kubernetes monitoring.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.

**Kubernetes monitoring Variables**

.. zuul:rolevar:: kubernetes_monitoring_chart_version
   :default: 3.5.0

Version of Kubernetes monitoring helm chart version which should be used.

.. zuul:rolevar:: kubernetes_monitoring_work_directory
   :default: /tmp/kubernetes_monitoring/configuration

Work directory inside the osism-ansible container.

.. zuul:rolevar:: kubernetes_monitoring_template_directory
   :default: .

Template directory containing `kubernetes_monitoring.yml`, e.g. OSISM configuration directory.

.. zuul:rolevar:: kubernetes_monitoring_namespace
   :default: kubernetes-monitoring

Kubernetes namespace in which the monitoring should be installed.
