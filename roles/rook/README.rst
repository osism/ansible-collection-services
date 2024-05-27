Ansible role for installation and configuration of Rook Cluster CRDs.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory and handles with Docker.

.. zuul:rolevar:: operator_group
   :default: {{ operator_user }}

Group from the user which will own the configuration directory.

.. zuul:rolevar:: configuration_directory
   :default: /opt/configuration

Path to the directory which will contains the configuration files.

**k3s/metallb Variables**

.. zuul:rolevar:: metallb_rook_external_IP
   :default: 192.168.16.101

Public IP for rook ceph dashboard.

**Rook Variables**

.. zuul:rolevar:: container_registry_rook
   :default: quay.io

Path to the registry that stores the container images for the rook operator.

.. zuul:rolevar:: rook_ceph_image
   :default: {{ container_registry_rook }}/rook/ceph

The container image to use.

.. zuul:rolevar:: rook_ceph_image_tag
   :default: v1.13.5

Version from rook operator in form of a tag which should be used.

.. zuul:rolevar:: rook_template_directory
   :default: {{ role_path }}/templates

Template directory containing rook CRD `*.yml.j2` files, e.g. OSISM configuration directory. Overwrite this to completely customize every aspect of the CRDs.

.. zuul:rolevar:: rook_namespace
   :default: rook-ceph

The Kubernetes namespace that will be created for the Rook cluster. The services, pods, and other resources created by the operator will be added to this namespace. The common scenario is to create a single Rook cluster. If multiple clusters are created, they must not have conflicting devices or host paths.

Also see https://rook.io/docs/rook/v1.13/Storage-Configuration/Advanced/ceph-configuration/?h=#using-alternate-namespaces

.. zuul:rolevar:: rook_work_directory
   :default: /tmp/rook/configuration

Rook work directory inside the osism-ansible container.

.. zuul:rolevar:: rook_cleanup
   :default: false

Run rook cleanup tasks and delete the whole cluster.


**Rook CRD Variables**

Have a look at `templates/*.yml.j2` to see where exaclty the variables are applied.
For ultimate customization, change `{{ rook_template_directory }}` to point to your configuration repository.

 .. zuul:rolevar:: rook_cluster_name
    :default: rook-ceph

The name that will be used internally for the Ceph cluster. Most commonly the name is the same as the namespace since multiple clusters are not supported in the same namespace.

 .. zuul:rolevar:: rook_mon_count
    :default: 3

Set the number of MONs to be started. The number must be between 1 and 9. The recommended value is most commonly 3. For highest availability, an odd number of mons should be specified.

 .. zuul:rolevar:: rook_mds_count
    :default: 3

Set the number of MDSs to be started.

 .. zuul:rolevar:: rook_mgr_count
    :default: 3

Set the number of MGRs to be started.

 .. zuul:rolevar:: rook_mgr_modules
    :default:   - name: balancer
                  enabled: true
                - name: status
                  enabled: true
                - name: prometheus
                  enabled: true

List of MGR modules to optionally enable or disable.
Note the "dashboard" and "monitoring" modules are already configured by other settings in the cluster CR.

 .. zuul:rolevar:: rook_dashboard_enabled
    :default: true

Enable the ceph dashboard for viewing cluster status 

 .. zuul:rolevar:: rook_dashboard_ssl
    :default: true

Enable SSL/TLS for the ceph dashboard.

 .. zuul:rolevar:: rook_dashboard_port
    :default: true

Port to use for the ceph dashboard.

 .. zuul:rolevar:: rook_dashboard_port_external
    :default: true

Port to use for the ceph dashboard loadbalancer.

 .. zuul:rolevar:: rook_monitoring_enabled
    :default: false

 .. zuul:rolevar:: rook_monitoring_enabled

Enable prometheus alerting for cluster.
Requires Prometheus to be pre-installed.
Also see https://rook.io/docs/rook/latest-release/Storage-Configuration/Monitoring/ceph-monitoring/

 .. zuul:rolevar:: rook_metrics_disabled
    :default: false

If true, the prometheus mgr module and Ceph exporter are both disabled.

 .. zuul:rolevar:: rook_network_encryption
    :default: true

Whether to encrypt the data in transit across the wire to prevent eavesdropping the data on the network.
The default is false. When encryption is enabled, all communication between clients and Ceph daemons, or between Ceph daemons will be encrypted.
When encryption is not enabled, clients still establish a strong initial authentication and data integrity is still validated with a crc check.

 .. zuul:rolevar:: rook_network_compression
    :default: true

Whether to compress the data in transit across the wire.

 .. zuul:rolevar:: rook_network_require_msgr2
    :default: false

Whether to require communication over msgr2. If true, the msgr v1 port (6789) will be disabled and clients will be required to connect to the Ceph cluster with the v2 port (3300).

 .. zuul:rolevar:: rook_network_public
    :default: "192.168.16.0/20"


 .. zuul:rolevar:: rook_network_cluster
    :default: "{{ rook_network_public }}"

Ceph cluster network for host networking.

 .. zuul:rolevar:: rook_crash_disabled
    :default: false

Disable the crash collector for ceph daemon crash collection.

 .. zuul:rolevar:: rook_logcollector_enabled
    :default: true

Disable log collector, daemons will log on files and rotate.

 .. zuul:rolevar:: rook_placement
    :default: all:
                tolerations:
                  - key: node-role.kubernetes.io/master
                  operator: Exists
                  effect: NoSchedule  

Control where various services will be scheduled by kubernetes.
By default, placement on kubernetes master nodes is tolerated.

 .. zuul:rolevar:: rook_annotations
   :default: {}

Add additional annotations to the Rook cluster CRD.

 .. zuul:rolevar:: rook_labels
   :default: {}

Add additional labels to the Rook cluster CRD.

 .. zuul:rolevar:: rook_resources
   :default: {}

The requests and limits for pods are set here.

 .. zuul:rolevar:: rook_storage_useallnodes
    :default: false

Use all nodes that are found for rook cluster.

 .. zuul:rolevar:: rook_storage_usealldevices
    :default: false

Use all devices that are found for rook cluster.
Be carefull, this might wipe all your devices.

 .. zuul:rolevar:: rook_storage_config_osdsperdevice
    :default: 1

Number of OSDs per device. Can be overwritten on node level by {{ rook_storage_nodes }}.

 .. zuul:rolevar:: rook_storage_config_encrypteddevice
    :default: true

Encrypt devices with dm-crypt. Will create LVM volumes on top of the encrypted devices.

 .. zuul:rolevar:: rook_storage_devicefilter
   :default: ""

Define a device filter where to create OSDs

 .. zuul:rolevar:: rook_storage_nodes
   :default: []

Name nodes where to create OSDs.

e.g.
```
 - name: "testbed-node-0"
 - name: "testbed-node-1"
 - name: "testbed-node-2"
```

 .. zuul:rolevar:: rook_cephblockpool_default_size
    :default: 3

Default size for CephBlockPool CRDs.

 .. zuul:rolevar:: rook_cephblockpool_default_min_size
    :default: 0

Default min_size for CephBlockPool CRDs.

 .. zuul:rolevar:: rook_cephblockpool_default_pg_num
    :default: 64

Default pg_num for CephBlockPool CRDs.

 .. zuul:rolevar:: rook_cephblockpools
    :default: - backups
              - volumes
              - images
              - metrics
              - vms

CephBlockPool CRDs to create. All default {{ rook_cephblockpool_default_* }} values will be set.

 .. zuul:rolevar:: rook_cephfilesystem_default_name
    :default: cephfs

Default name for CephFilesystem CRD.

 .. zuul:rolevar:: rook_cephfilesystem_default_size
    :default: 3

Default size of replicated pools for CephFilesystem CRD.

 .. zuul:rolevar:: rook_cephfilesystem_default_metadatapool_parameters_compression_mode
    :default: none

Default compression mode of metadata pool for CephFilesystem CRD.

 .. zuul:rolevar:: rook_cephfilesystem_default_datapool_parameters_compression_mode
    :default: none

Default compression mode of data pool for CephFilesystem CRD.

 .. zuul:rolevar:: rook_cephobjectstore_default_name
    :default: rgw

Default name for CephObjectStore CRD.

 .. zuul:rolevar:: rook_cephobjectstore_default_zone
    :default: default

Default zone for CephObjectStore CRD.

 .. zuul:rolevar:: rook_cephobjectstore_default_size
    :default: 3

Default size of replicated pools for CephObjectStore CRD.

 .. zuul:rolevar:: rook_cephobjectstore_default_port
    :default: 8081

Default RGW port for CephObjectStore CRD.

 .. zuul:rolevar:: rook_cephclients
   :default: cinder-backup:
               caps:
                 mon: "profile rbd"
                 osd: "profile rbd pool=backups"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder-backup.keyring"
             cinder:
               caps:
                 mon: "profile rbd"
                 osd: "profile rbd pool=volumes, profile rbd pool=vms, profile rbd pool=images"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/nova/ceph.client.cinder.keyring"
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/cinder/cinder-volume/ceph.client.cinder.keyring"
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder.keyring"
             glance:
               caps:
                 mon: "profile rbd"
                 osd: "profile rbd pool=vms, profile rbd pool=images"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/glance/ceph.client.glance.keyring"
             gnocchi:
               caps:
                 mon: "profile rbd"
                 osd: "profile rbd pool=metrics"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/gnocchi/ceph.client.gnocchi.keyring"
             nova:
               caps:
                 mon: "profile rbd"
                 osd: "profile rbd pool=images, profile rbd pool=vms, profile rbd pool=volumes, profile rbd pool=backups"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/nova/ceph.client.nova.keyring"
             manila:
               caps:
                 mon: "allow r"
                 mgr: "allow rw"
                 osd: "allow rw pool=cephfs_data"
               dests:
                 - "{{ configuration_directory }}/environments/kolla/files/overlays/manila/ceph.client.manila.keyring"


Defines names and capabilities of CephClient CRDs. Additinally it creates keyring files in the destionations you name, e.g. to be picked up by kolla-ansible.

e.g.

```
cinder-backup:
  caps:
    mon: "profile rbd"
    osd: "profile rbd pool=backups"
  dests:
    - "{{ configuration_directory }}/environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder-backup.keyring"
```
