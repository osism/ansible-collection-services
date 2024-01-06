This role is based on the following two roles:

* https://github.com/ansible-ThoTeam/nexus3-oss
* https://github.com/savoirfairelinux/ansible-nexus3-oss

**Docker Variables**

.. zuul:rolevar:: docker_network_mtu
   :default: 1500

Set this to the MTU for your outside connection.

.. zuul:rolevar:: docker_registry
   :default: index.docker.io

Look at docker_registry_nexus.

.. zuul:rolevar:: docker_registry_nexus
   :default: docker_registry

The registry for the Nexus Docker container.


**Operator Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user which will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

Group from the user which will own the configuration directory.


**Nexus Variables**

.. zuul:rolevar:: nexus_docker_compose_directory
   :default: /opt/nexus

Path to the directory where the docker-compose-files from Nexus will be stored.

.. zuul:rolevar:: nexus_configuration_directory
   :default: /opt/nexus/configuration

In this directory the configuration files for Nexus will be stored.

.. zuul:rolevar:: nexus_host
   :default: 127.0.0.1

The host where Nexus will be reachable.

.. zuul:rolevar:: nexus_port
   :default: 8190

Port which Nexus will use for connections from outside.

.. zuul:rolevar:: nexus_tag
   :default: 3.39.0

Version from Nexus which should be used.

.. zuul:rolevar:: nexus_image
   :default: {{ docker_registry_nexus }}/osism/nexus:{{ nexus_tag }}

The container image to use.

.. zuul:rolevar:: nexus_network
   :default: 172.31.101.32/28

The subnet for Nexus in the docker-compose file.

.. zuul:rolevar:: nexus_container_name
   :default: nexus

Name of the container in which Nexus will run.

.. zuul:rolevar:: nexus_service_name
   :default: docker-compose@nexus

Name from the Nexus service to deal with it.

.. zuul:rolevar:: nexus_provision_scripts
   :default: - anonymous.json
             - cleanup.json
             - docker-hub.json
             - docker-quay.json
             - ubuntu-archive.json
             - ubuntu-docker.json

# FIX ME

.. zuul:rolevar:: nexus_provision_groovy_scripts
   :default: - create_repos_from_list
             - setup_http_proxy
             - setup_realms
             - update_admin_password

# FIX ME

.. zuul:rolevar:: nexus_admin_username
   :default: admin

Username for the Nexus admin.

.. zuul:rolevar:: nexus_admin_password
   :default: password

Password for the Nexus admin.

.. zuul:rolevar:: nexus_with_http_proxy
   :default: false

Configure Nexus to use HTTP Proxy or not.

.. zuul:rolevar:: nexus_http_proxy_host
   :default: proxy.example.com

Proxy HTTP host for Nexus.

.. zuul:rolevar:: nexus_http_proxy_port
   :default: 8080

Port which should be used for the HTTP proxy.

.. zuul:rolevar:: nexus_http_proxy_username
   :default: ""

Username for HTTP proxy.

.. zuul:rolevar:: nexus_http_proxy_password
   :default: ""

Password for HTTP proxy.

.. zuul:rolevar:: nexus_with_https_proxy
   :default: false

Configure Nexus to use HTTPS Proxy or not.

.. zuul:rolevar:: nexus_https_proxy_host
   :default: proxy.example.com

Proxy HTTPS host for Nexus.

.. zuul:rolevar:: nexus_https_proxy_port
   :default: 8080

Port which should be used for the HTTPS proxy.

.. zuul:rolevar:: nexus_https_proxy_username
   :default: ""

Username for HTTPS proxy.

.. zuul:rolevar:: nexus_https_proxy_password
   :default: ""

Password for HTTPS proxy.

.. zuul:rolevar:: nexus_proxy_exclude_hosts
   :default: - "localhost"
             - "127.*"
             - "[::1]"

If proxy is enabled these hosts should bypass the proxy.

.. zuul:rolevar:: nexus_docker_bearer_token_realm
   :default: true

Bearer token for Docker realm.

.. zuul:rolevar:: nexus_repos_apt_defaults

.. code-block:: yaml

   blob_store: default
   strict_content_validation: true
   layout_policy: strict  # strict or permissive
   write_policy: allow_once  # one of "allow", "allow_once" or "deny"
   maximum_component_age: 1440  # Nexus gui default. For proxies only
   maximum_metadata_age: 1440  # Nexus gui default. For proxies only
   negative_cache_enabled: true  # Nexus gui default. For proxies only
   negative_cache_ttl: 1440  # Nexus gui default. For proxies only
   flat: false  # Nexus gui default. For proxies only

Defines how Nexus should deal with apt repositories.

.. zuul:rolevar:: nexus_repos_docker_defaults

.. code-block:: yaml

   blob_store: default
   force_basic_auth: true
   strict_content_validation: true
   version_policy: release  # release, snapshot or mixed
   layout_policy: strict  # strict or permissive
   write_policy: allow_once  # one of "allow", "allow_once" or "deny"
   maximum_component_age: 1440  # Nexus gui default. For proxies only
   maximum_metadata_age: 1440  # Nexus gui default. For proxies only
   negative_cache_enabled: true  # Nexus gui default. For proxies only
   negative_cache_ttl: 1440  # Nexus gui default. For proxies only
   # More about Foreign Layers https://help.sonatype.com/repomanager3/formats/docker-registry/foreign-layers
   cache_foreign_layers: false  # Nexus gui default. For proxies only
   foreign_layer_url_whitelist: []  # Nexus gui default. For proxies only

Defines how Nexus should deal with Docker repositories.

.. zuul:rolevar:: nexus_repos_docker_proxy

.. code-block:: yaml

   - name: docker-quay
     http_port: 8192
     v1_enabled: false
     index_type: "HUB"
     remote_url: "https://quay.io"
     use_nexus_certificates_to_access_index: false
     force_basic_auth: false
     cache_foreign_layers: true
   - name: docker-hub
     http_port: 8191
     v1_enabled: false
     index_type: "HUB"
     remote_url: "https://registry-1.docker.io"
     use_nexus_certificates_to_access_index: false
     force_basic_auth: false
     cache_foreign_layers: true

Configuration for the used Docker registries.

.. zuul:rolevar:: nexus_repos_apt_proxy

.. code-block:: yaml

   - name: ubuntu-docker
     remote_url: https://download.docker.com/linux/ubuntu/
     distribution: focal
     flat: true
   - name: ubuntu-archive
     remote_url: http://archive.ubuntu.com/ubuntu/
     distribution: focal
     flat: true

Apt repositories that should be added to Nexus proxy.

**Traefik Variables**

.. zuul:rolevar:: nexus_traefik
   :default: false

Set the configuration from Traefik to false. If true Traefik will be used.

.. zuul:rolevar:: traefik_external_network_name
   :default: traefik

Name of the Nexus network for Traefik.

.. zuul:rolevar:: traefik_external_network_cidr
   :default: 172.31.254.0/24

The Traefik network segment for external traffic.
