Ansible role for installation and configuration of the Kubernetes monitoring.

**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.

**Kubernetes monitoring Variables**

.. zuul:rolevar:: kubernetes_monitoring_chart_source
   :default: dnationcloud/dnation-kubernetes-monitoring-stack

Kubernetes monitoring helm chart package which should be used.

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

**Openstack Exporter Variables**

.. zuul:rolevar:: enable_openstack_exporter
   :default: false

Sets the openstack exporter deployment to false. If true the openstack exporter be
configured and deployed.

.. zuul:rolevar:: openstack_exporter_chart_source
   :default: oci://registry.scs.community/openstack-exporter/prometheus-openstack-exporter

Openstack exporter helm chart package which should be used.

.. zuul:rolevar:: openstack_exporter_chart_version
   :default: 0.4.5

Version of Openstack exporter helm chart version which should be used.

.. zuul:rolevar:: openstack_internal_vip_address
   :default: 127.0.0.1

Openstack internal VIP address to be used in host aliases setting.

.. zuul:rolevar:: openstack_external_vip_address
   :default: openstack_internal_vip_address

Openstack external VIP address to be used in host aliases setting.

.. zuul:rolevar:: openstack_internal_fqdn
   :default: localhost

Openstack internal FQDN to be used in host aliases setting.

.. zuul:rolevar:: openstack_external_fqdn
   :default: openstack_internal_fqdn

Openstack external FQDN to be used in host aliases setting.

.. zuul:rolevar:: openstack_ca_certificate_path
   :default: ""

Openstack custom CA certificate path to use.

.. zuul:rolevar:: openstack_exporter_clouds_yml_cloud
   :default: openstack

Openstack project (cloud) in the clouds.yml to use.

.. zuul:rolevar:: openstack_exporter_clouds_yml_path
   :default: /etc/openstack/clouds.yml

Path to the clouds.yml.

.. zuul:rolevar:: openstack_exporter_secure_yml_path
   :default: /etc/openstack/secure.yml

Credentials for the clouds.yml configured in the secure.yml.

.. zuul:rolevar:: openstack_exporter_work_directory
   :default: kubernetes_monitoring_work_directory

Work directory inside the osism-ansible container.

.. zuul:rolevar:: openstack_exporter_template_directory
   :default: kubernetes_monitoring_template_directory

Template directory containing `openstack_exporter.yml`, e.g. OSISM configuration directory.

.. zuul:rolevar:: openstack_exporter_namespace
   :default: kubernetes_monitoring_namespace

Kubernetes namespace in which the exporter should be installed.

.. zuul:rolevar:: openstack_exporter_service_monitor_scrape_interval
   :default: 90s

Interval at which prometheus will scrape the openstack exporter metrics endpoint.

.. zuul:rolevar:: openstack_exporter_service_monitor_scrape_timeout
   :default: 60s

Timeout duration that prometheus will wait when scraping the openstack exporter metrics endpoint.
