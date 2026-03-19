# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This file was started on December 19, 2020. Changes prior to this date are not included in the CHANGELOG.

## [v0.20260319.0] - 2026-03-19

### Added
- FRR: YRZN Metalbox template with dual BGP sessions supporting separate BMC and DATA fabrics (osism/ansible-collection-services#2066)
- FRR: YRZN Network template with dual BGP sessions for DATA and PROVIDER fabrics (osism/ansible-collection-services#2067)
- FRR: Configurable announced /24 networks in YRZN Network template (osism/ansible-collection-services#2068)

### Changed
- FRR: Consolidate announced networks into single ANNOUNCED-NETWORKS prefix-list in YRZN Network template (osism/ansible-collection-services#2069)
- Netdata: Switch to dbengine memory mode, enable streaming compression, increase default history to 24h, and add configurable `allow_from` (osism/ansible-collection-services#2064)

### Fixed
- Manager: Skip version check for disabled ansible services (osism/ansible-collection-services#2063)
- Netdata: Fix streaming stability for large-scale deployments by adding replication control, increasing client streaming buffer, and removing connection rate limit (osism/ansible-collection-services#2065)

## [v0.20260312.0] - 2026-03-12

### Added
- Optional BGP neighbor password support for the FRR YRZN profile via `frr_yrzn001_password` (osism/ansible-collection-services#2058)
- Suppression of HTTP 206 partial content responses from httpd access log via `httpd_log_ignore_partial_content` (osism/ansible-collection-services#2059)
- Optional HTTPS/SSL support for the httpd role via `httpd_ssl_enable` (osism/ansible-collection-services#2060)
- Configurable netbox systemd service dependency in manager role via `netbox_external` to support external netbox instances (osism/ansible-collection-services#2062)

### Changed
- FRR YRZN template falls back to `_frr_uplinks` when `frr_uplinks_data` is not set (osism/ansible-collection-services#2061)

### Fixed
- FRR YRZN template now correctly accesses `item.interface` instead of `item` in uplinks loop (osism/ansible-collection-services#2057)

## [v0.20260308.0] - 2026-03-08

### Added
- httpd: Host network mode via `httpd_network_mode` and configurable ironic listen addresses via `httpd_ironic_listen_addresses`, with automatic L3 mdev accept sysctl settings in host mode (osism/ansible-collection-services#2049)
- httpd: KeepAlive, performance, and request timeout settings for Apache configuration (osism/ansible-collection-services#2052)
- manager, netbox, openstackclient, traefik: Configurable IPv6 support for internal Docker networks (osism/ansible-collection-services#2054)
- frr: YRZN configuration template with BGP setup for dual-stack (osism/ansible-collection-services#2056)

### Changed
- manager: Use localhost instead of 127.0.0.1 and add IPv6 fallback for host address defaults and URLs (osism/ansible-collection-services#2053)

### Fixed
- httpd: Remove ironic volume preparation container after run by adding detach and cleanup options (osism/ansible-collection-services#2051)

## [v0.20260223.0] - 2026-02-23

### Added
- Manager: make dnsmasq DHCP lease time configurable via `manager_inventory_reconciler_dnsmasq_lease_time` (osism/ansible-collection-services#2047)

## [v0.20260220.0] - 2026-02-20

### Added
- Add bgp-af-l2vpn-evpn tag to netbox initializers (osism/ansible-collection-services#2043)
- Allow providing FRR configuration template via `frr_config_template` variable for environments where the config repository cannot be modified (osism/ansible-collection-services#2046)

### Changed
- Make python3-docker deb package URL configurable via `docker_python3_package_deb` variable

### Fixed
- Fix default manager netbox filters using incorrect `state` query parameter instead of `status` (osism/ansible-collection-services#2044)

## [v0.20260129.0] - 2026-01-29

### Changed
- Manager: use uv for pip installations in wrapper scripts (osism/ansible-collection-services#2042)

## [v0.20260127.0] - 2026-01-27

### Added
- Add VRRP support for leaf configuration in frr role via `frr_vrrp_groups` variable
- Add `docker_default_ulimits` to set default ulimits in Docker daemon configuration (osism/ansible-collection-services#2030)
- Add inventory volume mount for api service in manager role (osism/ansible-collection-services#2041)

### Changed
- Make ospfd, ospf6d, and vrrpd daemons configurable in frr role

### Fixed
- Fix `operator_user` default value in thanos_sidecar role (osism/ansible-collection-services#2037)

### Dependencies
- ansible 11.11.0 → 11.12.0 (osism/ansible-collection-services#2033)

## [v0.20251130.0] - 2025-11-30

### Changed
- Make configuration mount in osismclient read-write (osism/ansible-collection-services#2032)

## [v0.20251128.0] - 2025-11-28

### Added
- Extra interfaces support for BGP route-map in frr via `frr_extra_interfaces` variable (osism/ansible-collection-services#2069)

## [v0.20251121.1] - 2025-11-21

### Changed
- Netbox: set custom field maintenance to false by default (osism/ansible-collection-services#2028)

## [v0.20251121.0] - 2025-11-21

### Added
- Optional BGP neighbor password support for FRR templates (k3s_cilium, leaf, loadbalancer, loadbalancer_external_uplink)
- Configurable BGP local preference support for FRR leaf template with IPv4 and IPv6 address families
- FRR local preference custom field for devices and interfaces in NetBox (osism/ansible-collection-services#2025)

### Fixed
- httpd: Prevent sonic ZTP directory permission breakage by disabling `manage_dir` in `authorized_key` tasks (osism/ansible-collection-services#2020)

## [v0.20251104.0] - 2025-11-04

### Added
- New Kepler role for deploying the Kepler energy consumption exporter via Docker Compose

### Changed
- Kepler default network changed to 172.31.102.48/28 (osism/ansible-collection-services#2018)

## [v0.20251101.0] - 2025-11-01

### Added
- FRR: Hostname-based configuration support with fallback to type-based configuration (osism/ansible-collection-services#2017)

### Dependencies
- hashicorp/vault 1.20.4 → 1.21.0 (osism/ansible-collection-services#2016)

## [v0.20251022.0] - 2025-10-22

### Added
- stepca: ACME provisioner with configurable name and optional EAB requirement (osism/ansible-collection-services#2010)
- rsyslog: Configurable logrotate support with size-based and weekly rotation (osism/ansible-collection-services#2014)

### Changed
- stepca: Rename default JWK provisioner to "jwk" and ACME provisioner to "acme" (osism/ansible-collection-services#2011)

### Dependencies
- ansible 11.10.0 → 11.11.0 (osism/ansible-collection-services#2009, osism/ansible-collection-services#2012)
- registry.osism.tech/osism/homer v25.08.1 → v25.10.1 (osism/ansible-collection-services#2013)

## [v0.20251013.0] - 2025-10-13

### Added
- New `opentelemetry_collector` role for collecting metrics via Prometheus and logs via OTLP, with Dash0 export support (osism/ansible-collection-services#2005)
- New `stepca` role for deploying Smallstep step-ca as a Docker service with automatic CA initialization (osism/ansible-collection-services#2007)

### Changed
- Substation: add dedicated entrypoint.sh script, fix configuration volume mount path to `/root/.config/openstack`, and fix command path to `/substation` (osism/ansible-collection-services#2003)

### Dependencies
- molecule 25.7.0 → 25.9.0 (osism/ansible-collection-services#1998)
- hashicorp/vault 1.20.3 → 1.20.4 (osism/ansible-collection-services#2006)
- redis 7.4.5-alpine → 7.4.6-alpine (osism/ansible-collection-services#2008)

## [v0.20251006.0] - 2025-10-06

### Added
- Substation role for deploying the substation service via Docker Compose (osism/ansible-collection-services#2002)

### Changed
- Rename `frontend_tag`, `frontend_image_namespace`, and `frontend_image` to `osism_frontend_tag`, `osism_frontend_image_namespace`, and `osism_frontend_image` in manager role (osism/ansible-collection-services#2001)

## [v0.20250927.0] - 2025-09-27

### Added
- Container version verification system for the manager role to check running Docker containers match expected versions (osism/ansible-collection-services#1999)

### Changed
- Cleanup `.ansible-lint` file by removing unnecessary exclusions and skip rules (osism/ansible-collection-services#1991)

### Fixed
- Fix ansible-lint jinja2 formatting issue in zuul role (osism/ansible-collection-services#2000)

### Dependencies
- pytest 8.4.1 → 8.4.2 (osism/ansible-collection-services#1992)
- actions/setup-python v5 → v6 (osism/ansible-collection-services#1993)
- ansible 11.9.0 → 11.10.0 (osism/ansible-collection-services#1996, osism/ansible-collection-services#1997)

## [v0.20250902.0] - 2025-09-02

### Added
- netbird: add `netbird_disable_dns` parameter to disable DNS (osism/ansible-collection-services#1983)
- manager: add `manager_inventory_ignore_maintenance_state` parameter to ignore maintenance state when using Netbox as inventory source (osism/ansible-collection-services#1988)
- manager: add share volume to the openstack service for vault secrets access (osism/ansible-collection-services#1986)
- manager: add CA certificates to the API service (osism/ansible-collection-services#1990)

### Changed
- netbird: set `--dns-resolver-address` when DNS is disabled (osism/ansible-collection-services#1984)
- netbird: bind DNS resolver to `127.0.0.1:1053` when DNS is disabled (osism/ansible-collection-services#1985)
- manager: move `INVENTORY_FROM_NETBOX` environment variable to inventory-reconciler.env (osism/ansible-collection-services#1987)

### Dependencies
- ara-server 1.7.2 → 1.7.3 (osism/ansible-collection-services#1982)
- hashicorp/vault 1.20.2 → 1.20.3 (osism/ansible-collection-services#1989)

## [v0.20250824.0] - 2025-08-24

### Added
- Frontend service for the manager role with Docker Compose integration and Traefik support (osism/ansible-collection-services#1972)

### Changed
- Add `openstack.env` to netbox service environment files (osism/ansible-collection-services#1972)

### Dependencies
- ansible 11.8.0 → 11.9.0 (osism/ansible-collection-services#1973) (osism/ansible-collection-services#1974)
- mariadb 11.8.2 → 11.8.3 (osism/ansible-collection-services#1975)
- postgres 16.9-alpine → 16.10-alpine (osism/ansible-collection-services#1978)
- actions/checkout v4 → v5 (osism/ansible-collection-services#1971)

## [v0.20250823.0] - 2025-08-23

### Added
- dnsmasq: support for extra parameters via `dnsmasq_extra_parameters` configuration option (osism/ansible-collection-services#1958)
- manager: `INVENTORY_IGNORE_PROVISION_STATE` environment variable for inventory reconciler (osism/ansible-collection-services#1977)
- netbox: custom field `device_interface_label` for devices (osism/ansible-collection-services#1967)
- netbox: storage prefix role (osism/ansible-collection-services#1965)
- netbox: transfer prefix role (osism/ansible-collection-services#1968)
- zuul: cosign secrets for container image signing (osism/ansible-collection-services#1951)

### Changed
- httpd: bind port 80 also to IPv6 addresses (osism/ansible-collection-services#1952)
- httpd: bind to all global IPv6 addresses instead of only the first one (osism/ansible-collection-services#1950)
- netbox: change default value of maintenance custom field from false to true (osism/ansible-collection-services#1956)

### Fixed
- Fix Ansible 2.19 broken conditionals across netbird, netbox, and traefik roles (osism/ansible-collection-services#1963)
- nexus: add default filter to `nexus_repos_docker_proxy` and `nexus_repos_apt_proxy` to prevent undefined variable errors (osism/ansible-collection-services#1959)

### Dependencies
- ansible 11.7.0 → 11.8.0 (osism/ansible-collection-services#1954) (osism/ansible-collection-services#1955)
- hashicorp/vault 1.20.0 → 1.20.2 (osism/ansible-collection-services#1957) (osism/ansible-collection-services#1966)
- molecule 25.6.0 → 25.7.0 (osism/ansible-collection-services#1960)
- registry.osism.tech/osism/homer v25.05.2 → v25.08.1 (osism/ansible-collection-services#1969)
- registry.osism.tech/osism/netbox v4.3.3 → v4.3.4 (osism/ansible-collection-services#1953)
- traefik v3.4.3 → v3.4.4 (osism/ansible-collection-services#1949)

## [v0.20250711.0] - 2025-07-11

### Added
- dnsmasq: support for `dhcp-option-force` configuration (osism/ansible-collection-services#1948)

### Changed
- dnsmasq: localise queries and ignore `/etc/hosts` when DNS is enabled (osism/ansible-collection-services#1946)
- zuul: remove gate pipeline (osism/ansible-collection-services#1945)

### Fixed
- gnmic: fix typo in outputs variable name in template (osism/ansible-collection-services#1944)

## [v0.20250710.0] - 2025-07-10

### Added
- Initial gnmic role for gNMI collector with Docker Compose deployment (osism/ansible-collection-services#1942)
- gnmic: Configurable targets, subscriptions, and outputs with merge_variables support (osism/ansible-collection-services#1943)

### Changed
- httpd: Add SONiC nameserver to /etc/resolv.conf in post-install script (osism/ansible-collection-services#1938)
- httpd: Run curl in mgmt VRF for Metalbox status update (osism/ansible-collection-services#1939)
- httpd: Rename API endpoint from `/v1/switches` to `/v1/sonic` (osism/ansible-collection-services#1940)

### Dependencies
- registry.osism.tech/osism/netbox v4.2.2 → v4.3.3 (osism/ansible-collection-services#1780)
- registry.osism.tech/osism/nexus 3.81.1 → 3.82.0 (osism/ansible-collection-services#1941)
- redis 7.4.4 → 7.4.5 (osism/ansible-collection-services#1937)

## [v0.20250701.0] - 2025-07-01

### Added
- httpd: Add support for Ironic integration with configurable `httpd_ironic_enable` option, volume preparation, and `/ironic/httpboot` endpoint (osism/ansible-collection-services#1919, osism/ansible-collection-services#1922, osism/ansible-collection-services#1923, osism/ansible-collection-services#1925, osism/ansible-collection-services#1928)
- httpd: Proxy port 6385 to the Ironic API via loopback interface (osism/ansible-collection-services#1924)
- httpd: Proxy `/v1/` requests to the OSISM API for SONiC ZTP deployments (osism/ansible-collection-services#1932)
- httpd: Update SONiC provision status in Metalbox after deployment (osism/ansible-collection-services#1930)
- netbox: Make Nginx Unit max/spare processes and idle timeout configurable (osism/ansible-collection-services#1931)

### Changed
- httpd: Simplify and clean up Apache httpd.conf configuration (osism/ansible-collection-services#1927)
- httpd: Use virtual host for port 80 to support per-port proxy pass rules (osism/ansible-collection-services#1934)
- httpd: Do not enforce password change on SONiC devices after deployment

### Fixed
- httpd: Use first IPv6 address of the loopback device for port binding (osism/ansible-collection-services#1933)

### Dependencies
- traefik v3.4.1 → v3.4.3 (osism/ansible-collection-services#1929)
- hashicorp/vault 1.19.5 → 1.20.0 (osism/ansible-collection-services#1921)

## [v0.20250623.1] - 2025-06-23

### Changed
- Use JSON format for inventory-reconciler `NETBOX_FILTER_CONDUCTOR_IRONIC` and `NETBOX_FILTER_CONDUCTOR_SONIC` environment variables instead of YAML (osism/ansible-collection-services#1917)

## [v0.20250623.0] - 2025-06-23

### Added
- Support for custom httpd.conf configuration in SONiC ZTP mode (osism/ansible-collection-services#1912)
- IP-based access control via .htaccess for SONiC ZTP mode (osism/ansible-collection-services#1913)
- Grouped IP allowlists for SONiC ZTP using `merge_variables` lookup (osism/ansible-collection-services#1914)
- Conductor filter parameters (`NETBOX_FILTER_CONDUCTOR_IRONIC`, `NETBOX_FILTER_CONDUCTOR_SONIC`) to inventory-reconciler environment (osism/ansible-collection-services#1916)

## [v0.20250619.0] - 2025-06-19

### Added
- netbox: Add consoleserver device role (osism/ansible-collection-services#1900)
- netbox: Add Loopback prefix role (osism/ansible-collection-services#1901)
- netbox: Add alternative_name custom field for devices (osism/ansible-collection-services#1904)
- httpd: Add SONiC ZTP post_install script for SSH permissions fix (osism/ansible-collection-services#1909)

### Changed
- dnsmasq: Reload service on configuration file changes (osism/ansible-collection-services#1908)
- httpd: Use serial-number as default SONiC ZTP identifier instead of hostname (osism/ansible-collection-services#1911)

### Fixed
- httpd: Fix typo in post_install.sh script (osism/ansible-collection-services#1910)

### Dependencies
- ansible 11.6.0 → 11.7.0 (osism/ansible-collection-services#1902, osism/ansible-collection-services#1903)
- molecule 25.5.0 → 25.6.0 (osism/ansible-collection-services#1907)
- pytest 8.4.0 → 8.4.1 (osism/ansible-collection-services#1905)

## [v0.20250616.0] - 2025-06-16

### Added
- dnsmasq: Add `bind-interfaces` parameter (osism/ansible-collection-services#1882)
- dnsmasq: Add `dhcp-boot` configuration support for PXE network boot
- dnsmasq: Add `dhcp-userclass` support (osism/ansible-collection-services#1897)
- dnsmasq: Add `dhcp-vendorclass` support (osism/ansible-collection-services#1898)
- netbox: Add `secrets` JSON custom field for devices (osism/ansible-collection-services#1883, osism/ansible-collection-services#1884)
- netbox: Add `sonic_parameters` JSON custom field for devices and interfaces (osism/ansible-collection-services#1893)
- netbox: Add `managed-by-metalbox` tag (osism/ansible-collection-services#1895)
- httpd: Add SONiC Zero Touch Provisioning (ZTP) support (osism/ansible-collection-services#1891, osism/ansible-collection-services#1892)
- frr: Add configurable `frr_hostname` variable to allow overriding the hostname
- frr: Add `frr_loopback_interface` variable to replace hardcoded loopback interface names
- manager: Add sonic-ztp directory creation and volume mounting for conductor (osism/ansible-collection-services#1899)

### Changed
- httpd: Make data directory world readable with mode 0755 (osism/ansible-collection-services#1885)
- manager: Split `netbox_filter_conductor` into separate `netbox_filter_conductor_ironic` and `netbox_filter_conductor_sonic` filters (osism/ansible-collection-services#1896)

### Fixed
- manager: Fix stdin handling in osism wrapper by always enabling stdin (`-i`) and only allocating TTY (`-t`) in interactive mode (osism/ansible-collection-services#1886)
- frr: Fix hardcoded `dummy0` interface references in loadbalancer and leaf templates to use `frr_loopback_interface` variable
- frr: Fix default value quoting for `frr_loopback_interface`

### Dependencies
- pytest 8.3.5 → 8.4.0 (osism/ansible-collection-services#1881)
- mariadb 11.7.2 → 11.8.2 (osism/ansible-collection-services#1888)
- registry.osism.tech/osism/nexus 3.80.0 → 3.81.1 (osism/ansible-collection-services#1887, osism/ansible-collection-services#1894)

## [v0.20250531.0] - 2025-05-31

### Added
- Manager: `manager_service_manual_start` parameter for manual start with docker compose (osism/ansible-collection-services#1878)
- Manager: `manager_enable_watchdog` parameter to make it possible to disable the watchdog service (osism/ansible-collection-services#1879)

### Changed
- Manager: always make /opt/configuration available in inventory reconciler (osism/ansible-collection-services#1880)

### Dependencies
- hashicorp/vault 1.19.4 → 1.19.5 (osism/ansible-collection-services#1876)
- redis 7.4.3 → 7.4.4 (osism/ansible-collection-services#1877)

## [v0.20250529.0] - 2025-05-29

### Added
- Manager parameters to configure periodic job schedules (`inventory_reconciler_schedule`, `gather_facts_schedule`) (osism/ansible-collection-services#1861)
- Netbox `dnsmasq_parameters` custom field for devices (osism/ansible-collection-services#1862)
- Dnsmasq support for multiple interfaces (osism/ansible-collection-services#1866)
- Dnsmasq support for dynamic hosts (osism/ansible-collection-services#1867)
- Netbox cable management device role (osism/ansible-collection-services#1868)
- Netbox `netplan_parameters` custom field to interfaces (osism/ansible-collection-services#1875)

### Changed
- Httpd data container now only runs when `httpd_data_enable` is true (osism/ansible-collection-services#1865)
- Dnsmasq only disables DNS port when `dnsmasq_enable_dns` is false (osism/ansible-collection-services#1869)
- Dnsmasq defaults cleaned up, removed hardcoded example values for `dnsmasq_dns_servers` and `dnsmasq_dns_hosts` (osism/ansible-collection-services#1870)
- Netbox service restarts can be skipped via `netbox_service_allow_restart` (osism/ansible-collection-services#1871)
- Manager service restarts can be skipped via `manager_service_allow_restart` (osism/ansible-collection-services#1872)
- Manager service starts after netbox service when netbox is enabled (osism/ansible-collection-services#1874)

### Fixed
- Netbox wrong data type of `dnsmasq_parameters` custom field (text → json) (osism/ansible-collection-services#1864)

### Dependencies
- molecule 25.4.0 → 25.5.0 (osism/ansible-collection-services#1863)
- traefik v3.4.0 → v3.4.1 (osism/ansible-collection-services#1873)

## [v0.20250525.0] - 2025-05-25

### Added
- Inventory-reconciler environment file for configuring the netbox to inventory sync (osism/ansible-collection-services#1850)
- `netbox_ignored_roles` and `netbox_role_mapping` parameters for the inventory reconciler (osism/ansible-collection-services#1854)
- Metalbox device role to netbox initializers (osism/ansible-collection-services#1855)
- `netbox_filter_inventory` parameter to filter devices included in the inventory (osism/ansible-collection-services#1858)
- `manager_inventory_reconciler_mode` parameter to set the inventory-reconciler mode (osism/ansible-collection-services#1859)
- `inventory_hostname` custom field to netbox to allow overwriting the default device name in the generated inventory (osism/ansible-collection-services#1860)

### Changed
- Use JSON format instead of YAML for `NETBOX_DATA_TYPES` in inventory-reconciler environment (osism/ansible-collection-services#1853)
- Rename `netbox_filter_list` to `netbox_filter_conductor` (osism/ansible-collection-services#1857)

### Removed
- OOB Leaf device role from netbox initializers (osism/ansible-collection-services#1856)

## [v0.20250521.0] - 2025-05-21

### Added
- netbox: Add custom fields for netplan and frr parameters (osism/ansible-collection-services#1843)
- netbox: Add custom field `dnsmasq_dhcp_tag` to overwrite the default dnsmasq DHCP tag (osism/ansible-collection-services#1847)
- netbox: Add custom field `frr_local_as` to overwrite the default FRR local AS (osism/ansible-collection-services#1848)
- dnsmasq: Add support for providing DHCP ranges and hosts via host vars using `merge_variables` lookup (osism/ansible-collection-services#1844)
- dnsmasq: Add support for `dhcp-mac` entries (osism/ansible-collection-services#1845)
- dnsmasq: Add support for `dhcp-option` entries (osism/ansible-collection-services#1846)

### Changed
- netbox: Cleanup and extend device roles and tags initializers (osism/ansible-collection-services#1849)
- netbox: Hide custom fields in UI when not set via `ui_visibility: hidden-ifunset` (osism/ansible-collection-services#1847)
- dnsmasq: Change default values for `dnsmasq_dhcp_ranges` and `dnsmasq_dhcp_hosts` to empty lists (osism/ansible-collection-services#1846)

### Fixed
- docker: Fix IPv6 configuration by using correct `fixed-cidr-v6` and `ip6tables` settings (osism/ansible-collection-services#1852)

### Dependencies
- hashicorp/vault 1.19.3 → 1.19.4 (osism/ansible-collection-services#1841)
- osism/homer v25.05.1 → v25.05.2 (osism/ansible-collection-services#1842)
- ansible 11.4.0 → 11.6.0 (osism/ansible-collection-services#1811, osism/ansible-collection-services#1812, osism/ansible-collection-services#1851)

## [v0.20250516.0] - 2025-05-16

### Added
- netbox: Add out-of-band tag (osism/ansible-collection-services#1822)
- netbox: Add custom field for ironic parameters
- netbox: Add parameters to change container image namespaces (osism/ansible-collection-services#1838)
- zuul: Add ZooKeeper data and datalog volumes
- zuul: Add IPv6 network support to services (osism/ansible-collection-services#1827)
- manager: Add share volume to conductor container
- manager: Add parameters to change container image namespaces (osism/ansible-collection-services#1837)
- manager: Add new netbox parameters NETBOX_FILTER_LIST and NETBOX_SECONDARIES (osism/ansible-collection-services#1834)
- manager: Support OSISM_RETRY environment variable (osism/ansible-collection-services#1839)
- docker: Add parameter to set fixed-cidr-v6 (osism/ansible-collection-services#1840)

### Changed
- zuul: Bump ZooKeeper to 3.8.4, MariaDB to 11.7, Nodepool to 11.0.0, and Zuul to 12.0.0 (osism/ansible-collection-services#1831)
- zuul: Use named volume for MariaDB by default (osism/ansible-collection-services#1830)
- zuul: Update sample tenant configuration to use osism org (osism/ansible-collection-services#1829)
- zuul: Refresh Zuul CI secrets (osism/ansible-collection-services#1835)
- netbox: Update to version 4.2.2 (osism/ansible-collection-services#1797)

### Fixed
- zuul: Fix typo in ZooKeeper volume variable names (osism/ansible-collection-services#1832)
- zuul: Add missing quote in docker-compose template (osism/ansible-collection-services#1833)
- zuul: Fix wrong secret (osism/ansible-collection-services#1836)

### Removed
- netbox: Remove out-of-band custom fields (oob_type, oob_address, oob_port) (osism/ansible-collection-services#1821)

### Dependencies
- traefik v3.3.6 → v3.4.0 (osism/ansible-collection-services#1818)
- nexus 3.79.1 → 3.80.0 (osism/ansible-collection-services#1820)
- postgres 16.8 → 16.9 (osism/ansible-collection-services#1823)

## [v0.20250505.0] - 2025-05-05

### Changed
- dnsmasq: allow multiple DHCP ranges by replacing `dnsmasq_dhcp_range` with `dnsmasq_dhcp_ranges` list (osism/ansible-collection-services#1817)

### Dependencies
- hashicorp/vault 1.19.2 → 1.19.3 (osism/ansible-collection-services#1814)
- registry.osism.tech/osism/homer v25.04.1 → v25.05.1 (osism/ansible-collection-services#1815)

## [v0.20250428.0] - 2025-04-28

### Added
- Hubble wrapper script for the manager role (osism/ansible-collection-services#1807)

### Removed
- kubernetes-monitoring role, moved to osism/osism-kubernetes (osism/ansible-collection-services#1806)

### Dependencies
- nexus 3.79.0 → 3.79.1 (osism/ansible-collection-services#1805)
- traefik v3.3.5 → v3.3.6 (osism/ansible-collection-services#1809)
- hashicorp/vault 1.19.1 → 1.19.2 (osism/ansible-collection-services#1810)
- redis 7.4.2-alpine → 7.4.3-alpine (osism/ansible-collection-services#1813)

## [v0.20250407.0] - 2025-04-07

### Added
- Flux wrapper script for manager role (osism/ansible-collection-services#1786)
- DNS support for dnsmasq role with configurable DNS servers and host entries (osism/ansible-collection-services#1791)
- netbox: Set postgres shared memory size (osism/ansible-collection-services#1794)
- netbox: Add postgres configuration file with tuned settings (osism/ansible-collection-services#1795)
- netbox: Add DPU device role (osism/ansible-collection-services#1793)
- netbox: Add OOB device role (osism/ansible-collection-services#1798)
- netbox: Add oob_address and oob_port custom fields (osism/ansible-collection-services#1802)

### Changed
- Simplified manager healthchecks to use `pgrep osism` for compatibility with new Alpine-based image (osism/ansible-collection-services#1789)
- Default to non-interactive mode in wrapper scripts when any of stdin, stdout, or stderr is not a terminal
- Cleanup ansible-lint configuration (osism/ansible-collection-services#1788)
- netbox: Rename out-of-band prefix/VLAN role to OOB (osism/ansible-collection-services#1799)
- netbox: Rename out_of_band_type custom field to oob_type (osism/ansible-collection-services#1802)

### Removed
- Rook role, moved to osism/osism-kubernetes (osism/ansible-collection-services#1787)
- CloudNative PG role (osism/ansible-collection-services#1790)
- netbox: Remove deprecated custom fields: deployment_enabled, ironic_enabled, configuration_template, device_state, device_transition, device_type, deployment_type, deployment_state, introspection_state, network_interface_name, ironic_state (osism/ansible-collection-services#1802)

### Dependencies
- ansible 11.3.0 → 11.4.0 (osism/ansible-collection-services#1784, osism/ansible-collection-services#1785)
- pytest-testinfra 10.1.1 → 10.2.2 (osism/ansible-collection-services#1792)
- traefik v3.3.4 → v3.3.5 (osism/ansible-collection-services#1796)
- molecule 25.3.1 → 25.4.0 (osism/ansible-collection-services#1800)
- nexus 3.78.2 → 3.79.0 (osism/ansible-collection-services#1801)
- vault 1.19.0 → 1.19.1 (osism/ansible-collection-services#1803)
- homer v25.03.3 → v25.04.1 (osism/ansible-collection-services#1804)

## [v0.20250323.0] - 2025-03-23

### Added
- OS_CACERT setting to manager's OpenStack environment configuration (osism/ansible-collection-services#1783)

### Changed
- Default container registry from quay.io to registry.osism.tech across multiple roles (osism/ansible-collection-services#1777)
- Nexus proxy remote URL from osism.harbor.regio.digital to registry.osism.tech (osism/ansible-collection-services#1777)
- OpenStack client version from "xena" to "2024.2" (osism/ansible-collection-services#1777)
- Grouped postgres version updates in Renovate configuration for netbox role (osism/ansible-collection-services#1781)

### Dependencies
- ansible 11.2.0 → 11.3.0 (osism/ansible-collection-services#1770, osism/ansible-collection-services#1771)
- homer v25.02.1 → v25.03.3 (osism/ansible-collection-services#1778)
- nexus 3.76.1 → 3.78.2 (osism/ansible-collection-services#1779)
- postgres 16.7 → 16.8 (osism/ansible-collection-services#1767)

## [v0.20250314.0] - 2025-03-14

### Changed
- Remove usage of `osism_netbox_image` in manager role, replaced with generic `osism_image` (osism/ansible-collection-services#1775)

### Dependencies
- molecule 25.2.0 → 25.3.1 (osism/ansible-collection-services#1765)
- rook/ceph v1.16.3 → v1.16.5 (osism/ansible-collection-services#1766, osism/ansible-collection-services#1774)
- traefik v3.3.3 → v3.3.4 (osism/ansible-collection-services#1769)
- pytest 8.3.4 → 8.3.5 (osism/ansible-collection-services#1772)
- hashicorp/vault 1.18.4 → 1.19.0 (osism/ansible-collection-services#1768)
- jinja2 3.1.5 → 3.1.6 (osism/ansible-collection-services#1773)

## [v0.20250218.0] - 2025-02-18

### Changed
- Docker role now uses `docker_version` variable by default, allowing version override via `__docker_default_version` (osism/ansible-collection-services#1762)
- Docker role prints used Docker and Docker CLI versions during execution (osism/ansible-collection-services#1763)
- Renamed Docker test functions for improved clarity (osism/ansible-collection-services#1762)

### Fixed
- Manager: fixed `depends_on` of the inventory reconciler service to correctly depend on all *-ansible services (osism/ansible-collection-services#1764)

## [v0.20250217.0] - 2025-02-17

### Added
- Add httpd role with Docker Compose deployment, configurable host/port, and health check (osism/ansible-collection-services#1756)
- httpd: support data sidecar container images (osism/ansible-collection-services#1757)
- dnsmasq: add TFTP support with configurable `dnsmasq_enable_tftp` option (osism/ansible-collection-services#1754)

### Fixed
- dnsmasq: add missing `-d` parameter to container command and add container test (osism/ansible-collection-services#1753)
- molecule: fix ANSIBLE_COLLECTIONS_PATH for CentOS by adding fallback collections path (osism/ansible-collection-services#1755)
- docker: change `docker_storage_containerd_snapshotter` from string to boolean type (osism/ansible-collection-services#1761)

### Dependencies
- quay.io/ceph/ceph v19.2.0 → v19.2.1 (osism/ansible-collection-services#1758)
- postgres 16.6-alpine → 16.7-alpine (osism/ansible-collection-services#1759)
- mariadb 11.6.2 → 11.7.2 (osism/ansible-collection-services#1760)

## [v0.20250205.0] - 2025-02-05

### Added
- Add cgit dashboard to homer (osism/ansible-collection-services#1200)
- Add skyline dashboard to homer (osism/ansible-collection-services#1202)
- Add configurable private key support via wireguard_users
- Add wireguard_dns parameter for DNS server configuration
- New dnsmasq role for DHCP server deployment via Docker Compose (osism/ansible-collection-services#1750)

### Changed
- Rename `docker_configure_repository` to `containerd_configure_repository` in containerd role (osism/ansible-collection-services#1739)
- Switch falco service from falco-kmod to falco-modern-bpf.service (osism/ansible-collection-services#1749)
- Add not supported for CentOS message to falco role (osism/ansible-collection-services#1748)
- Add ANSIBLE_COLLECTIONS_PATH to molecule provisioner environment (osism/ansible-collection-services#1746)
- Remove netbox repository from cgit default repositories

### Fixed
- Fix documentation and bug report links in homer dashboard (osism/ansible-collection-services#1735)
- Fix wireguard_dns default value to empty string to avoid NoneType error (osism/ansible-collection-services#1737)

### Removed
- Remove old keycloak role (osism/ansible-collection-services#1725)
- Remove virtualbmc role (osism/ansible-collection-services#1747)

### Dependencies
- jinja2 3.1.4 → 3.1.5 (osism/ansible-collection-services#1722)
- quay.io/osism/netbox v4.1.9 → v4.1.10 (osism/ansible-collection-services#1723)
- index.docker.io/rook/ceph v1.16.0 → v1.16.3 (osism/ansible-collection-services#1724, osism/ansible-collection-services#1740, osism/ansible-collection-services#1752)
- quay.io/osism/dnsdist 1.9.6 → 1.9.8 (osism/ansible-collection-services#1726)
- quay.io/osism/homer v24.05.1 → v25.02.1 (osism/ansible-collection-services#1727, osism/ansible-collection-services#1745)
- traefik v3.2.3 → v3.3.3 (osism/ansible-collection-services#1732, osism/ansible-collection-services#1738, osism/ansible-collection-services#1744)
- redis 7.4.1-alpine → 7.4.2-alpine (osism/ansible-collection-services#1731)
- quay.io/osism/nexus 3.75.1 → 3.76.1 (osism/ansible-collection-services#1734, osism/ansible-collection-services#1742)
- molecule 24.12.0 → 25.2.0 (osism/ansible-collection-services#1741)
- ansible 10.7.0 → 11.2.0 (osism/ansible-collection-services#1697, osism/ansible-collection-services#1696)
- hashicorp/vault 1.18.3 → 1.18.4 (osism/ansible-collection-services#1743)

## [v0.20241219.0] - 2024-12-19

### Changed
- Renamed cephclient keyring template from `ceph-keyring-config.j2` to `keyring.j2` (osism/ansible-collection-services#1717)

### Dependencies
- hashicorp/vault 1.18.2 → 1.18.3 (osism/ansible-collection-services#1720)
- postgres 16.5-alpine → 16.6-alpine (osism/ansible-collection-services#1704)
- quay.io/osism/netbox v4.1.7 → v4.1.9 (osism/ansible-collection-services#1716, osism/ansible-collection-services#1721)
- quay.io/osism/nexus 3.75.0 → 3.75.1 (osism/ansible-collection-services#1714)
- index.docker.io/rook/ceph v1.15.6 → v1.16.0 (osism/ansible-collection-services#1719)
- traefik v3.2.1 → v3.2.3 (osism/ansible-collection-services#1715, osism/ansible-collection-services#1718)

## [v0.20241206.0] - 2024-12-06

### Added
- New teleport role with service configuration, Debian and CentOS support (osism/ansible-collection-services#1672) (osism/ansible-collection-services#1673) (osism/ansible-collection-services#1674) (osism/ansible-collection-services#1676)
- New sshd role for managing OpenSSH server (osism/ansible-collection-services#1681)
- New `wazuh-agent` role for deploying and configuring Wazuh agents on Debian and RedHat systems (osism/ansible-collection-services#1682)
- Configurable `wazuh_agent_config_profile` parameter for wazuh_agent role (osism/ansible-collection-services#1683)
- Configurable `frr_options_bgpd` and `frr_options_bfdd` parameters for FRR daemon options (osism/ansible-collection-services#1684)
- Configurable `frr_allow_service_restart` parameter to control automatic FRR restarts after configuration changes (osism/ansible-collection-services#1698)
- Configurable `frr_config_file`, `frr_vtysh_file`, and `frr_daemons_file` parameters for FRR config file locations (osism/ansible-collection-services#1698)
- Cilium wrapper script for manager role when Kubernetes is enabled (osism/ansible-collection-services#1685)
- Keystone and Swift integration for Rook CephObjectStore (osism/ansible-collection-services#1705)
- Pre-pull of container images for netbox service via `netbox_pre_pull` parameter (osism/ansible-collection-services#1638)
- frr: support for overlaying configuration file from the configuration repository (osism/ansible-collection-services#1677)
- frr: manage the vtysh.conf file (osism/ansible-collection-services#1678)

### Changed
- rsyslog: make work directory configurable via `rsyslog_workdir` variable and enhance CI tests (osism/ansible-collection-services#1653)
- zabbix_agent: add CentOS and Debian support (osism/ansible-collection-services#1675)
- teleport: use `join_params` instead of `auth_token`, add `ca_pin` and `role` label parameters (osism/ansible-collection-services#1674)
- Improved netbox health check handler with rescue block and configurable compose directory (osism/ansible-collection-services#1638)
- Netbox health check now uses `/login/` endpoint instead of `/metrics` (osism/ansible-collection-services#1638)
- wireguard: enhance CI tests (osism/ansible-collection-services#1669)
- virtualbmc: enhance CI tests (osism/ansible-collection-services#1668)
- zabbix_agent: enhance CI tests (osism/ansible-collection-services#1664)
- traefik: enhance CI tests (osism/ansible-collection-services#1663)
- squid: enhance CI tests (osism/ansible-collection-services#1659)
- docker: enhance CI tests (osism/ansible-collection-services#1607)
- thanos_sidecar: enhance CI tests (osism/ansible-collection-services#1662)
- tang: enhance CI tests (osism/ansible-collection-services#1660)

### Fixed
- Netbox plugins configuration rendering with missing trailing comma (osism/ansible-collection-services#1693)
- Installation of python3-docker on Ubuntu 24.04 by using osism/deb-packaging source (osism/ansible-collection-services#1709)

### Removed
- Metering service role, which was a technical preview from the SCS project and will not be maintained (osism/ansible-collection-services#1706)
- Tang service (osism/ansible-collection-services#1707)

### Dependencies
- ansible 10.4.0 → 10.7.0 (osism/ansible-collection-services#1666) (osism/ansible-collection-services#1691) (osism/ansible-collection-services#1692) (osism/ansible-collection-services#1710) (osism/ansible-collection-services#1711)
- hashicorp/vault 1.17.6 → 1.18.2 (osism/ansible-collection-services#1667) (osism/ansible-collection-services#1687) (osism/ansible-collection-services#1700)
- traefik v3.1.5 → v3.2.1 (osism/ansible-collection-services#1670) (osism/ansible-collection-services#1686) (osism/ansible-collection-services#1699)
- quay.io/osism/netbox v4.1.3 → v4.1.7 (osism/ansible-collection-services#1679) (osism/ansible-collection-services#1688) (osism/ansible-collection-services#1689) (osism/ansible-collection-services#1702)
- quay.io/osism/nexus 3.72.0 → 3.75.0 (osism/ansible-collection-services#1671) (osism/ansible-collection-services#1690) (osism/ansible-collection-services#1712)
- index.docker.io/rook/ceph v1.15.3 → v1.15.6 (osism/ansible-collection-services#1680) (osism/ansible-collection-services#1694) (osism/ansible-collection-services#1701)
- redis 7.4.0 → 7.4.1 (osism/ansible-collection-services#1661)
- postgres 16.4-alpine → 16.5-alpine (osism/ansible-collection-services#1695)
- mariadb 11.5.2 → 11.6.2 (osism/ansible-collection-services#1703)
- quay.io/ceph/ceph v18.2.4 → v19.2.0 (osism/ansible-collection-services#1634)
- pytest 8.3.3 → 8.3.4 (osism/ansible-collection-services#1708)
- molecule 24.9.0 → 24.12.0 (osism/ansible-collection-services#1713)

## [v0.20241006.0] - 2024-10-06

### Added
- FRR: Add k3s_cilium template for BGP with Cilium (osism/ansible-collection-services#1623)
- FRR: Allow enabling/disabling bgpd and bfdd services via `frr_enable_bgpd` and `frr_enable_bfdd` parameters (osism/ansible-collection-services#1621)
- FRR: Support `frr_uplinks__*` host var parameters merged with `frr_uplinks` (osism/ansible-collection-services#1624)
- Docker: Add `docker_storage_containerd_snapshotter` parameter for containerd snapshotter support (osism/ansible-collection-services#1626)
- Rook: Add loadbalancer resources for Ceph dashboard and RGW (osism/ansible-collection-services#1618)
- Wireguard: Ensure iptables package is installed (osism/ansible-collection-services#1619)
- fail2ban: Install an sshd jail by default with configurable ban settings
- Nexus: Add `nexus_force_init` parameter to force service initialisation (osism/ansible-collection-services#1657)

### Changed
- Manager: Enforce update wrappers to run only with the operator user (osism/ansible-collection-services#1620)
- Manager: Use `community.docker.docker_compose_v2_pull` module for pulling container images (osism/ansible-collection-services#1643)
- Rook: Change loadbalancer service names to namespace-based naming (osism/ansible-collection-services#1636)
- Rook: Improve handling of helm values with consolidated deployment workflow, new `values.yml.j2` template, and renamed variables (`rook_namespace` → `rook_ceph_cluster_helm_release_namespace`, `rook_cephclients` → `rook_ceph_cluster_clients`) (osism/ansible-collection-services#1639)
- Netbox: Move rescue tasks into a separate file (osism/ansible-collection-services#1612)
- Netbox: Use tmpfs instead of zram for tests (osism/ansible-collection-services#1656)
- Enhanced CI tests for adminer (osism/ansible-collection-services#1627), auditd (osism/ansible-collection-services#1628), cgit (osism/ansible-collection-services#1630), cephclient (osism/ansible-collection-services#1629), dnsdist, clamav, lldpd, homer, osquery, openstackclient, and fail2ban (osism/ansible-collection-services#1644, osism/ansible-collection-services#1642, osism/ansible-collection-services#1649, osism/ansible-collection-services#1648, osism/ansible-collection-services#1652, osism/ansible-collection-services#1651)
- Enhanced FRR CI tests with BGPd and BFDd function tests and added test template (osism/ansible-collection-services#1646)
- Enhanced manager CI tests with version check function test (osism/ansible-collection-services#1650)

### Fixed
- Rook: Fix Ceph image version and Renovate datasource configuration (osism/ansible-collection-services#1632)
- Docker: Fix python3-docker installation on Ubuntu 24.04 by using package from Debian Sid (osism/ansible-collection-services#1641)

### Dependencies
- hashicorp/vault 1.17.5 → 1.17.6 (osism/ansible-collection-services#1625)
- traefik v3.1.4 → v3.1.5 (osism/ansible-collection-services#1654)
- rook/ceph v1.15.2 → v1.15.3 (osism/ansible-collection-services#1655)
- netbox v4.1.1 → v4.1.3 (osism/ansible-collection-services#1633)

## [v0.20240924.0] - 2024-09-24

### Added
- netbox: automatic PostgreSQL major version upgrade using pgautoupgrade (osism/ansible-collection-services#1604)
- rook: support fetching Ceph admin keyring via `rook_fetch_ceph_admin_keyring` flag (osism/ansible-collection-services#1593)
- scaphandre: add `scaphandre_share_pids_with_host` option to share PID namespace with host for detailed process monitoring (osism/ansible-collection-services#1616)
- zuul: add missing `mariadb_data` volume to docker-compose template (osism/ansible-collection-services#1602)

### Changed
- cephclient: improve task names in rook tasks (osism/ansible-collection-services#1594)
- chrony: enhance CI tests with server reachability and status checks (osism/ansible-collection-services#1606)
- manager: replace `virtualenv` with `python3 -m venv` and remove `python3-virtualenv` dependency (osism/ansible-collection-services#1588)
- molecule: use galaxy dependency handler instead of forced shell install for ansible requirements (osism/ansible-collection-services#1599)
- nexus: fix typo in provision scripts comment (osism/ansible-collection-services#1600)
- phpMyAdmin: enhance CI tests with HTTP connectivity checks (osism/ansible-collection-services#1608)
- rook: improve handling of helm values by using inline values instead of template files, simplify deployment tasks, and add `create_namespace` and `wait` options (osism/ansible-collection-services#1613)
- rook: improve task names, variable naming conventions, and overall code cleanup (osism/ansible-collection-services#1614)
- rook: move directory creation from cleanup tasks to main tasks (osism/ansible-collection-services#1614)
- Use dictionary syntax for `ansible.builtin.service` register result across all roles (osism/ansible-collection-services#1596)
- zuul: re-enable manager role tests on CentOS (osism/ansible-collection-services#1588)
- zuul: use `community.docker.docker_compose_v2` module (osism/ansible-collection-services#1603)
- zuul: use ZRAM device for netbox tests (osism/ansible-collection-services#1563)
- zuul: use ZRAM device for nexus tests (osism/ansible-collection-services#1600)

### Fixed
- rook: fix cluster cleanup/purge by adding helm release deletion step (osism/ansible-collection-services#1617)
- rook: fix swapped placement labels between MDS and RGW (osism/ansible-collection-services#1615)

### Removed
- rook: remove unused `metallb_rook_external_IP` and `rook_cleanup` defaults (osism/ansible-collection-services#1614)

### Dependencies
- ansible 10.3.0 → 10.4.0
- molecule 24.8.0 → 24.9.0 (osism/ansible-collection-services#1592)
- nodepool 9.0.0 → 10.0.0 (osism/ansible-collection-services#1601)
- quay.io/osism/netbox v4.1.0 → v4.1.1 (osism/ansible-collection-services#1595)
- rook/ceph v1.15.1 → v1.15.2 (osism/ansible-collection-services#1610)
- traefik v3.1.2 → v3.1.4 (osism/ansible-collection-services#1611)

## [v0.20240911.0] - 2024-09-11

### Added
- Healthcheck for the osismclient service in manager (osism/ansible-collection-services#1586)

### Changed
- Use ZRAM device for manager tests in Zuul (osism/ansible-collection-services#1587)

### Dependencies
- pytest 8.3.2 → 8.3.3 (osism/ansible-collection-services#1589)
- ansible 10.3.0 → 10.4.0 (osism/ansible-collection-services#1591)

## [v0.20240907.0] - 2024-09-07

### Added
- Task to remove and change labels regarding Rook (osism/ansible-collection-services#1576)
- Molecule tests for metering and tang roles (osism/ansible-collection-services#1573)
- Rook and rook_operator roles to Renovate configuration for automated version management (osism/ansible-collection-services#1582)

### Changed
- Netbox: make healthcheck start_period configurable for all services (osism/ansible-collection-services#1578)
- Tang: simplify package variable, update systemd path, and clean up socket configuration (osism/ansible-collection-services#1573)
- Fix quoting of rook version tags for Renovate compatibility (osism/ansible-collection-services#1584)

### Dependencies
- quay.io/osism/netbox v4.0.9 → v4.1.0 (osism/ansible-collection-services#1574, osism/ansible-collection-services#1579, osism/ansible-collection-services#1583)
- hashicorp/vault 1.17.3 → 1.17.5 (osism/ansible-collection-services#1575, osism/ansible-collection-services#1577)
- quay.io/osism/ara-server 1.7.1 → 1.7.2 (osism/ansible-collection-services#1580)
- quay.io/osism/nexus 3.71.0 → 3.72.0 (osism/ansible-collection-services#1581)
- index.docker.io/rook/ceph v1.14.5 → v1.15.1 (osism/ansible-collection-services#1585)

## [v0.20240825.0] - 2024-08-25

### Added
- Chrony role now checks minimum number of configured NTP servers before proceeding (osism/ansible-collection-services#1554)

### Changed
- Wireguard default allowed IPs now include additional testbed CIDRs `192.168.112.0/20` and `192.168.128.0/20` (osism/ansible-collection-services#1569)

### Fixed
- Manager CA certificate handling now uses OS-specific certificate file paths, fixing compatibility with CentOS/RedHat (osism/ansible-collection-services#1570)
- OpenStack client CA certificate path corrected for RedHat-family systems and simplified `REQUESTS_CA_BUNDLE` environment variable configuration (osism/ansible-collection-services#1571)

## [v0.20240818.0] - 2024-08-18

### Added
- Support for zram devices in docker role for CI and testing (osism/ansible-collection-services#1564)

### Changed
- Zuul: add DTRACK_API_KEY secret (osism/ansible-collection-services#1568)

### Fixed
- Docker: ignore errors in fact scripts when Docker socket is unavailable (osism/ansible-collection-services#1556)
- Netbox: fix container user to `unit:root` to resolve git data source sync issues (osism/ansible-collection-services#1560)
- Netbox: fix default SCRIPTS_ROOT path in configuration.py to `/opt/netbox/netbox/scripts` (osism/ansible-collection-services#1561)

### Removed
- Remove openstack-health-monitor role (osism/ansible-collection-services#1565)

### Dependencies
- mariadb 11.4.2 → 11.5.2 (osism/ansible-collection-services#1557, osism/ansible-collection-services#1566)
- ansible 10.2.0 → 10.3.0 (osism/ansible-collection-services#1558, osism/ansible-collection-services#1559)
- quay.io/osism/netbox v4.0.8 → v4.0.9 (osism/ansible-collection-services#1562)
- molecule 24.7.0 → 24.8.0 (osism/ansible-collection-services#1567)

## [v0.20240812.0] - 2024-08-12

### Added
- cephclient: Remove old container and package installations when switching to rook (osism/ansible-collection-services#1524)
- New zabbix_agent role with Zabbix Agent 2 support for Ubuntu (osism/ansible-collection-services#1545)
- Data directory for osismclient in manager role (osism/ansible-collection-services#1555)

### Changed
- squid: Update default image tag from 5.7-23.04_beta to 6.1-23.10_beta (osism/ansible-collection-services#1528)
- netbox: Avoid unnecessary service restart by using internal fact instead of configurable variable (osism/ansible-collection-services#1532)
- manager: Avoid unnecessary service restart by using internal fact instead of configurable variable (osism/ansible-collection-services#1533)
- nexus: Avoid unnecessary service restart by using internal fact (osism/ansible-collection-services#1534)
- Add ansible-collection-ensure-readme CI job (osism/ansible-collection-services#1537)
- Wireguard: allow default cilium LB CIDR and k3s services CIDR in client allowed IPs by default (osism/ansible-collection-services#1542) (osism/ansible-collection-services#1543)
- Docker: sync Debian and RedHat task names and reorder RedHat install steps (osism/ansible-collection-services#1550)
- FRR: pin package version on Debian and RedHat (osism/ansible-collection-services#1549)
- Zuul: also test fail2ban on Ubuntu 24.04 (osism/ansible-collection-services#1546)
- Netbox: do not use tmpfs for molecule tests and reorganize defaults sections (osism/ansible-collection-services#1544)

### Fixed
- Fix handling of service restarts for netbox, manager and nexus by migrating to dedicated systemd unit files (osism/ansible-collection-services#1535)

### Removed
- Remove old and out-of-date README files for multiple roles (osism/ansible-collection-services#1536)

### Dependencies
- ansible 9.7.0 → 10.2.0 (osism/ansible-collection-services#1499)
- pytest 8.3.1 → 8.3.2 (osism/ansible-collection-services#1529)
- postgres 15.7-alpine → 16.4 (osism/ansible-collection-services#1151) (osism/ansible-collection-services#1553)
- quay.io/osism/netbox v3.7.8 → v4.0.8 (osism/ansible-collection-services#1501) (osism/ansible-collection-services#1538)
- traefik v3.1.0 → v3.1.2 (osism/ansible-collection-services#1540) (osism/ansible-collection-services#1547)
- redis 7.2.5 → 7.4.0 (osism/ansible-collection-services#1539)
- hashicorp/vault 1.17.2 → 1.17.3 (osism/ansible-collection-services#1548)
- quay.io/osism/nexus 3.70.1 → 3.71.0 (osism/ansible-collection-services#1552)

## [v0.20240723.0] - 2024-07-23

### Changed
- Require ansible >= 2.16 instead of >= 2.14 (osism/ansible-collection-services#1520)
- openstackclient: make use within screen possible without problems by adding `exec` to docker command (osism/ansible-collection-services#1515)
- Mark metering role as tech preview and remove its tests (osism/ansible-collection-services#1519)
- Mark openstack_health_monitor role as tech preview and remove its tests (osism/ansible-collection-services#1521)
- docker: remove two unnecessary `changed_when` directives (osism/ansible-collection-services#1518)
- traefik: disable new version checks and anonymous usage reporting (osism/ansible-collection-services#1523)
- squid: add `max_filedescriptors` limit (1048576) to config (osism/ansible-collection-services#1525)
- squid: handle the start of the service gracefully with retries and health checks (osism/ansible-collection-services#1526)

### Removed
- netbox: remove OSISM webhook initializer (osism/ansible-collection-services#1513)

### Dependencies
- molecule 24.6.1 → 24.7.0 (osism/ansible-collection-services#1511)
- quay.io/osism/nexus 3.69.0 → 3.70.1 (osism/ansible-collection-services#1512)
- traefik v3.0.4 → v3.1.0 (osism/ansible-collection-services#1514)
- ansible 10.1.0 → 10.2.0 (osism/ansible-collection-services#1516)
- pytest 8.2.2 → 8.3.1 (osism/ansible-collection-services#1522)
- quay.io/osism/dnsdist 1.8.0 → 1.9.6 (osism/ansible-collection-services#1527)

## [v0.20240710.1] - 2024-07-10

### Added
- Ensure that jq is installed for the netbox role, required by the "Wait for an healthy netbox service" handler (osism/ansible-collection-services#1509)

### Dependencies
- hashicorp/vault 1.17.1 → 1.17.2 (osism/ansible-collection-services#1510)

## [v0.20240710.0] - 2024-07-10

### Changed
- rook: Improve wait task names and increase check frequency for CephCluster readiness checks (osism/ansible-collection-services#1502)
- netbox: Improve service start with container health checks using `docker compose ps` (osism/ansible-collection-services#1503)
- netbox: Increase wait time for healthy service to 10 minutes for slow manager nodes (osism/ansible-collection-services#1504)
- hddtemp: Replace `hddtemp_enable_module` parameter with automatic drivetemp module availability check (osism/ansible-collection-services#1506)
- Migrated `mariadb_operator` and `rabbitmq_operator` roles to osism/osism-kubernetes (osism/ansible-collection-services#1508)

### Fixed
- Fixed drivetemp module check in hddtemp role to use `stdout_lines` length instead of return code (osism/ansible-collection-services#1507)

### Removed
- traefik: Remove `traefik_pilot_dashboard` parameter (Pilot configuration removed in v3) (osism/ansible-collection-services#1496)

### Dependencies
- traefik v2.11.5 → v3.0.4 (osism/ansible-collection-services#1416, osism/ansible-collection-services#1498)
- ansible 9.7.0 → 10.1.0 (osism/ansible-collection-services#1500)
- molecule 24.6.0 → 24.6.1 (osism/ansible-collection-services#1505)

## [v0.20240702.0] - 2024-07-02

### Added
- New mariadb_operator role for deploying MariaDB operator via Helm (osism/ansible-collection-services#1461)
- Netbird role parameters: hostname, interface name, log level, management URL, preshared key, and WireGuard port, using environment variables instead of CLI flags (osism/ansible-collection-services#1457, osism/ansible-collection-services#1458)
- manager: `manager_enable_openstack` parameter to disable OpenStack integration (osism/ansible-collection-services#1477)
- hddtemp: `hddtemp_enable_module` flag to control kernel module loading (osism/ansible-collection-services#1467)
- cephclient: `cephclient_host_networking` option for host networking instead of container networking (osism/ansible-collection-services#1482)
- openstackclient: `openstackclient_host_networking` option for host networking instead of container networking (osism/ansible-collection-services#1482)
- Kubernetes monitoring role with optional OpenStack exporter support (osism/ansible-collection-services#1434)
- manager: osism-kubernetes container support (osism/ansible-collection-services#1487)
- Rook role for initial Kubernetes Ceph deployment (osism/ansible-collection-services#1427)
- Rook install type support for cephclient role (osism/ansible-collection-services#1427)

### Changed
- EPEL repository installation moved from individual roles to osism.commons.repository (osism/ansible-collection-services#1459, osism/ansible-collection-services#1464)
- Rename `lock_timeout` to `dnf_lock_timeout` across all RedHat family install tasks (osism/ansible-collection-services#1462)
- Netdata: remove duplicate service management tasks and unnecessary directory creation, consolidate service management in main tasks (osism/ansible-collection-services#1463)
- Molecule: unify clamav test function names for consistency (osism/ansible-collection-services#1465)
- Add `ipwrap` filter to docker-compose port bindings for IPv6 support across multiple roles (osism/ansible-collection-services#1478)
- molecule: centralize docker, netaddr, and requests package installation in common prepare task (osism/ansible-collection-services#1483) (osism/ansible-collection-services#1484)
- molecule: disable python3-docker package installation in Zuul CI via `docker_python_install: false` (osism/ansible-collection-services#1473)
- molecule: remove hardcoded `ansible_python_interpreter` setting (osism/ansible-collection-services#1488)
- Do not skip fail2ban molecule tests on Ubuntu 24.04, use dedicated Zuul job excluding Ubuntu 24.04 instead (osism/ansible-collection-services#1466)
- Support Ansible version 2.17 (osism/ansible-collection-services#1489)
- Remove crushtool wrapper from cephclient role (osism/ansible-collection-services#1492)
- Stop copying old wrapper scripts in manager role (osism/ansible-collection-services#1493)
- Netbox SECRET_KEY default now meets minimum 50 character length requirement (osism/ansible-collection-services#1494)
- Disable netbox osism plugin by default (osism/ansible-collection-services#1495)

### Fixed
- rabbitmq_operator: fix image reference separator from `/` to `:` between image and tag (osism/ansible-collection-services#1460)
- Fix typo in thanos_sidecar docker-compose template (osism/ansible-collection-services#1490)

### Dependencies
- pytest 8.2.1 → 8.2.2 (osism/ansible-collection-services#1469)
- molecule 24.2.1 → 24.6.0 (osism/ansible-collection-services#1474)
- ansible 9.6.0 → 9.7.0 (osism/ansible-collection-services#1475) (osism/ansible-collection-services#1476) (osism/ansible-collection-services#1485) (osism/ansible-collection-services#1486)
- hashicorp/vault 1.16.3 → 1.17.1 (osism/ansible-collection-services#1481) (osism/ansible-collection-services#1491)
- quay.io/osism/nexus 3.68.1 → 3.69.0 (osism/ansible-collection-services#1470)
- traefik v2.11.3 → v2.11.5 (osism/ansible-collection-services#1479)
- quay.io/osism/netbox v3.4.8 → v3.7.8 (osism/ansible-collection-services#1343)

## [v0.20240531.0] - 2024-05-31

### Added
- Add rabbitmq-operator role for Kubernetes deployment (osism/ansible-collection-services#1446)
- Add warning in manager update wrapper when Ansible is installed on the manager node (osism/ansible-collection-services#1449)
- New `netbird` role for managing NetBird VPN client with Debian and RedHat support (osism/ansible-collection-services#1453)
- `docker_python_install` parameter to enable or disable installation of Python docker bindings (osism/ansible-collection-services#1456)

### Changed
- Rename "Add app repository" task to "Add repository" in cephclient, falco, and netdata roles (osism/ansible-collection-services#1454)
- Improved and renamed netdata molecule tests for consistency and added proper skip logic (osism/ansible-collection-services#1455)

### Fixed
- Fix check for encrypted vault files in manager update wrapper (osism/ansible-collection-services#1450)

### Removed
- Removed netdata cloud.conf configuration and `netdata_config_path` variable (osism/ansible-collection-services#1455)

### Dependencies
- pytest-testinfra 10.1.0 → 10.1.1 (osism/ansible-collection-services#1447)
- netaddr 1.2.1 → 1.3.0 (osism/ansible-collection-services#1448)
- hashicorp/vault 1.16.2 → 1.16.3 (osism/ansible-collection-services#1451)
- mariadb 11.3.2 → 11.4.2 (osism/ansible-collection-services#1452)

## [v0.20240524.0] - 2024-05-24

### Added
- Traefik extra configuration support via `traefik_configuration_extra` (osism/ansible-collection-services#1423)
- Traefik extra ports support via `traefik_ports_extra` (osism/ansible-collection-services#1425)
- Traefik dynamic service configuration via `traefik_configuration_dynamic` (osism/ansible-collection-services#1426)
- Manager configurable ulimit nofile for Ansible containers (osism/ansible-collection-services#1429)
- Docker throttle service restarts via `docker_throttle_restart` (osism/ansible-collection-services#1431)
- Docker configurable wait time after service restart via `docker_wait_after_restart` (osism/ansible-collection-services#1432)
- Manager configurable netbox inventory sync via `manager_inventory_from_netbox` (osism/ansible-collection-services#1444)

### Changed
- Netdata switched to new official repository at repo.netdata.cloud (osism/ansible-collection-services#1435)
- README cleanup and updated documentation link (osism/ansible-collection-services#1443)

### Fixed
- Traefik removed incorrect osism.yml volume mount (osism/ansible-collection-services#1422)
- Traefik restart service when configuration changes (osism/ansible-collection-services#1424)
- Fixed truthy yamllint warnings in multiple roles (osism/ansible-collection-services#1439)
- Fixed yamllint "too few spaces before comment" warning in rook_operator (osism/ansible-collection-services#1442)

### Removed
- Tuned README removed as docs migrated to osism/osism.github.io (osism/ansible-collection-services#1428)
- Release notes removed, now managed in central repositories (osism/ansible-collection-services#1445)

### Dependencies
- jinja2 3.1.3 → 3.1.4 (osism/ansible-collection-services#1419)
- quay.io/osism/nexus 3.67.1 → 3.68.1 (osism/ansible-collection-services#1420, osism/ansible-collection-services#1430)
- postgres 15.6-alpine → 15.7-alpine (osism/ansible-collection-services#1421)
- pytest 8.2.0 → 8.2.1 (osism/ansible-collection-services#1433)
- redis 7.2.4-alpine → 7.2.5-alpine (osism/ansible-collection-services#1436)
- ansible 9.5.1 → 9.6.0 (osism/ansible-collection-services#1437, osism/ansible-collection-services#1438)
- traefik 2.11.2 → v2.11.3 (osism/ansible-collection-services#1440)
- quay.io/osism/homer v24.04.1 → v24.05.1 (osism/ansible-collection-services#1441)

## [v0.20240503.0] - 2024-05-03

### Added
- Manager: detect if ANSIBLE_ASK_VAULT_PASS is required (osism/ansible-collection-services#1367)
- Manager: get Ansible collection versions from the manager environment (osism/ansible-collection-services#1385)
- Manager: pull container images before service start and restart (osism/ansible-collection-services#1391)
- Manager: support scripts based on testbed repository (osism/ansible-collection-services#1418)
- Testing on Ubuntu 24.04 (noble) for zuul and manager roles (osism/ansible-collection-services#1370, osism/ansible-collection-services#1414)

### Changed
- Docker: upgrade default version to 26.0.2 (osism/ansible-collection-services#1379)
- Docker: use docker_version as default for docker_cli_version to simplify configuration (osism/ansible-collection-services#1380)
- Docker: use prefix variables for OS specific defaults to allow user overrides (osism/ansible-collection-services#1406)
- Containerd: use prefix variables for OS specific defaults to allow user overrides (osism/ansible-collection-services#1409)
- Chrony: use prefix variables for OS specific defaults to allow user overrides (osism/ansible-collection-services#1410)
- Rsyslog: use prefix variables for OS specific defaults to allow user overrides (osism/ansible-collection-services#1408)
- Wait until managed service is active for adminer, cephclient, cgit, dnsdist, homer, manager, netbox, nexus, openstackclient, phpmyadmin, scaphandre, and virtualbmc (osism/ansible-collection-services#1393, osism/ansible-collection-services#1395, osism/ansible-collection-services#1396, osism/ansible-collection-services#1398, osism/ansible-collection-services#1399, osism/ansible-collection-services#1400, osism/ansible-collection-services#1401, osism/ansible-collection-services#1402, osism/ansible-collection-services#1403, osism/ansible-collection-services#1404, osism/ansible-collection-services#1405, osism/ansible-collection-services#1407)
- Remove unnecessary `become` from handlers using docker-compose commands (osism/ansible-collection-services#1382, osism/ansible-collection-services#1387)
- Manager: get Ansible collection versions from run.sh in osism-update-docker script (osism/ansible-collection-services#1412)
- Manager: detect use of Ansible Vault in osism-update-docker script (osism/ansible-collection-services#1413)
- Role metadata updated to support Debian bookworm, Ubuntu noble, and EL 9; min Ansible version bumped to 2.16.0; removed focal support (osism/ansible-collection-services#1373)
- Manage collection requirements via osism/release instead of local requirements.yml (osism/ansible-collection-services#1388)
- Zuul: use ubuntu-jammy nodes instead of ubuntu-jammy-large (osism/ansible-collection-services#1368)
- Zuul: disable manager CentOS 9 job due to MariaDB startup issues (osism/ansible-collection-services#1381)
- Zuul: use SQLite database backend for manager tests (osism/ansible-collection-services#1383)
- Zuul: install docker pip package for the manager role tests (osism/ansible-collection-services#1384)
- Molecule: install missing docker package in venv across all test preparations (osism/ansible-collection-services#1394)
- Ansible-lint: do not mock kubernetes.core.helm (osism/ansible-collection-services#1390)

### Fixed
- Cephclient: make copy of the bash completion script more reliable by moving wait and copy logic to handlers (osism/ansible-collection-services#1386)
- Docker: use the cli version variable for the cli package instead of the engine version (osism/ansible-collection-services#1411)
- Nexus: make start of the service more reliable with health checks and retry logic (osism/ansible-collection-services#1389)
- Manager: fix syntax issue in osism-update-manager script (osism/ansible-collection-services#1392)
- Fix Ubuntu 24.04 compatibility for chrony and fail2ban roles (osism/ansible-collection-services#1417)

### Removed
- Remove requirements.yml file in favor of managing requirements via osism/release (osism/ansible-collection-services#1388)

### Dependencies
- ansible 9.4.0 → 9.5.1 (osism/ansible-collection-services#1376, osism/ansible-collection-services#1377)
- hashicorp/vault 1.16.1 → 1.16.2 (osism/ansible-collection-services#1375)
- homer v23.10.1 → v24.04.1 (osism/ansible-collection-services#1374)
- netaddr 0.10.1 → 1.2.1 (osism/ansible-collection-services#1289)
- pytest 8.1.1 → 8.2.0 (osism/ansible-collection-services#1378, osism/ansible-collection-services#1397)

## [v0.20240417.0] - 2024-04-17

### Added
- Debian support for roles: cephclient, chrony, containerd, docker, falco, hddtemp, netbox, netdata, openstackclient, osquery, rsyslog, thanos_sidecar, tuned
- Debian Bookworm node to CI test matrix
- FRR template `loadbalancer_external_uplink` for load balancers with external uplink BGP sessions (osism/ansible-collection-services#1358)
- FRR configuration version is now configurable via `frr_version` variable (osism/ansible-collection-services#1360)
- Warning when the OSISM CLI command is executed as root user (osism/ansible-collection-services#1356)

### Changed
- Renamed OS-specific task and variable files to use `-family` and `-dist` suffix convention across all roles
- Refactored test utilities to use `get_family_role_variable` and `get_dist_role_variable` helpers instead of `get_os_role_variable`
- Removed deprecated `apt-key` usage in favor of signed-by GPG key files in roles cephclient, containerd, docker, falco, netdata, openstackclient, osquery
- Removed Ubuntu version-specific conditionals (< 22.04) from multiple roles
- Added 30-second healthcheck start period for manager database-based services (osism/ansible-collection-services#1348)
- Added retry logic for thanos_sidecar service start to improve reliability
- Updated README to include Debian support column in role compatibility matrix
- Renamed "Start/enable" to "Manage" in all Ansible service task names (osism/ansible-collection-services#1359)
- Netdata uses stable repository by default instead of edge repository (osism/ansible-collection-services#1366)

### Fixed
- Zuul configuration file regex pattern for `.zuul.yaml` (osism/ansible-collection-services#1361)

### Dependencies
- ansible 9.3.0 → 9.4.0 (osism/ansible-collection-services#1350, osism/ansible-collection-services#1351)
- hashicorp/vault 1.16.0 → 1.16.1 (osism/ansible-collection-services#1357)
- molecule 24.2.0 → 24.2.1 (osism/ansible-collection-services#1362)
- quay.io/osism/nexus 3.66.0 → 3.67.1 (osism/ansible-collection-services#1353, osism/ansible-collection-services#1364)
- traefik 2.11.0 → 2.11.2 (osism/ansible-collection-services#1363, osism/ansible-collection-services#1365)

## [v0.20240327.0] - 2024-03-27

### Added
- CentOS 9 Stream support for roles: auditd, bird, clamav, fail2ban, tuned, docker, rsyslog, smartd, rng, osquery, chrony, homer, adminer, cephclient, lldpd, journald, cgit, hddtemp, containerd, frr, virtualbmc, traefik, dnsdist, falco, squid, phpmyadmin, scaphandre, manager, metering, openstackclient, nexus, wireguard, netbox, thanos_sidecar, netdata
- CentOS 9 Stream CI testing nodes across all Zuul molecule test jobs
- RedHat-specific install tasks using dnf and EPEL repository for bird, clamav, fail2ban, auditd, tuned, docker, rsyslog, smartd, osquery, lldpd, cephclient, containerd, frr, hddtemp, manager, netdata, openstackclient
- RedHat-specific Docker repository configuration for containerd role
- RedHat repository configuration for falco and netdata roles
- OS-family-specific test files for bird, clamav, docker, osquery, cephclient, containerd, falco, and netdata roles
- OS-specific variables files (`Debian.yml`, `RedHat.yml`) for docker, rsyslog, and cephclient roles
- `get_centos_repo_key` test utility helper for verifying RPM GPG keys
- Configurable `netdata_config_path` variable for cross-platform netdata configuration
- OS-specific timezone path variable (`manager_timezone_path`) for manager role
- Add MariaDB upgrade check to healthcheck for MariaDB >= 11.0.0 (osism/ansible-collection-services#1347)

### Changed
- Split `auditd_package_name` into `auditd_package_name_debian` and `auditd_package_name_redhat`
- Changed default `auditd_plugin_path` to `/etc/audit/plugins.d`, removing Ubuntu Jammy special-casing
- Improved clamav freshclam initialization and definition file permissions handling
- Moved bird configuration file deployment to distribution-specific install tasks
- Updated molecule prepare scripts for bird, clamav, fail2ban, tuned, and auditd to support both Debian (apt) and RedHat (dnf) package managers
- Docker role no longer restricted to Debian OS family only
- Docker version variables moved from `defaults/main.yml` to OS-specific vars files with separate `docker_version` and `docker_cli_version`
- Docker socket service enablement no longer gated on Debian OS family
- Rsyslog user in `rsyslog.conf.j2` is now templated via `rsyslog_user` variable instead of hardcoded `syslog`
- Cephclient `cephclient_debian_repository_key` renamed to `cephclient_repository_key` for OS-agnostic usage
- Cephclient `cephclient_debian_packages` renamed to `cephclient_packages`
- Cephclient default version changed from `pacific` to `reef`
- Cephclient container task file renamed from `container-Debian.yml` to `container.yml`
- Docker and osquery molecule tests restructured into per-OS test modules (`debian.py`, `redhat.py`, `main.py`)
- Test URL fetcher now sends a User-Agent header to avoid HTTP 403 errors
- Renamed `falco_debian_repository_key` to `falco_repository_key` for cross-platform use
- Switched wireguard package installation from `ansible.builtin.apt` to `ansible.builtin.package` for cross-platform support
- Simplified metering role by inlining tasks directly in main.yml instead of dispatching by OS family
- Updated docker-compose templates for metering, openstackclient, and thanos_sidecar to use OS-appropriate SSL certificate paths
- Removed OS family restriction from containerd service task and main task file
- Restructured molecule test files for containerd, falco, and netdata into package directories with shared and OS-specific tests
- Remove all package cache updates from molecule prepare steps
- Replace `ansible.builtin.yum` tasks with `ansible.builtin.dnf` across all RedHat install tasks
- Add `lock_timeout` parameter to all dnf tasks for improved reliability
- Replace `yum-config-manager` commands with `ansible.builtin.yum_repository` module for cephclient, falco, netdata, and osquery roles
- Remove unnecessary `yum-utils` package installations where no longer needed
- Refactored Zuul CI configuration to use abstract job definition, reducing duplication across molecule test jobs
- Replace osism.github.io URLs with osism.tech (osism/ansible-collection-services#1346)
- Update README.md with Ubuntu/CentOS compatibility matrix and additional roles (cloudnative_pg, rook_operator)

### Fixed
- Fixed typo "Upate" → "Update" in clamav configuration task name

### Removed
- Removed Ubuntu Jammy-specific vars file (`jammy.yml`) for auditd role
- Unrelated `auditd.conf.j2` and `rules/20-neo23x0.rules.j2` templates from lldpd role
- Remove bird role (osism/ansible-collection-services#1346)

### Dependencies
- hashicorp/vault 1.15.6 → 1.16.0 (osism/ansible-collection-services#1349)

## [v0.20240319.0] - 2024-03-19

### Changed
- Docker role now supports Debian in addition to Ubuntu (osism/ansible-collection-services#1340)

### Removed
- Bifrost integration from manager role (osism/ansible-collection-services#1339)

### Dependencies
- mariadb 11.2.3 → 11.3.2 (osism/ansible-collection-services#1307)

## [v0.20240311.0] - 2024-03-11

### Added
- New `rook_operator` role for installation and configuration of the Rook Ceph operator via Helm (osism/ansible-collection-services#1337)

### Dependencies
- pytest 8.1.0 → 8.1.1 (osism/ansible-collection-services#1338)

## [v0.20240307.0] - 2024-03-07

### Added
- Import custom CA cert into Java keystore for Keycloak (osism/ansible-collection-services#1321)

### Removed
- Remove openldap role (osism/ansible-collection-services#1334)

### Dependencies
- pytest 8.0.1 → 8.1.0 (osism/ansible-collection-services#1311, osism/ansible-collection-services#1322)
- ansible 9.2.0 → 9.3.0 (osism/ansible-collection-services#1317, osism/ansible-collection-services#1318)
- hashicorp/vault 1.15.5 → 1.15.6 (osism/ansible-collection-services#1320)
- quay.io/osism/nexus 3.65.0 → 3.66.0 (osism/ansible-collection-services#1335)

## [v0.20240221.0] - 2024-02-21

### Added
- Tasks to remove old architecture-dependent repositories for cephclient, containerd, docker, falco, netdata, openstackclient, and osquery (osism/ansible-collection-services#1287)
- New `cloudnative_pg` role for deploying the CloudNativePG operator (osism/ansible-collection-services#1296)
- Missing CloudNativePG template for keycloak database deployment (osism/ansible-collection-services#1298)
- keycloak: Create namespace before deploying database on CloudNativePG cluster (osism/ansible-collection-services#1300)
- keycloak: Add explicit deploy task for keycloakx chart (osism/ansible-collection-services#1301)
- zuul: Add job to push osism-ansible container image (osism/ansible-collection-services#1304)

### Changed
- Scaphandre container now runs in privileged mode instead of mounting individual /proc and /sys paths (osism/ansible-collection-services#1283)
- Scaphandre updated to version 1.0.0 (osism/ansible-collection-services#1291)
- Keycloak role refactored from Docker Compose to Helm/k3s deployment using codecentric/keycloakx chart and CloudNativePG (osism/ansible-collection-services#1296)
- Falco driver installation now uses `falcoctl` instead of `falco-driver-loader` (osism/ansible-collection-services#1290)
- keycloak: Rename container registry and TLS variables for consistency (`container_registry_keycloak`, `keycloak_tls_*`) (osism/ansible-collection-services#1301, osism/ansible-collection-services#1303)
- keycloak: Rename template from `codecentric-scs-keycloak.yml.j2` to `codecentric-keycloak.yml.j2` (osism/ansible-collection-services#1301)
- keycloak: Disable dbchecker to avoid Docker Hub rate limits from Busybox pulls (osism/ansible-collection-services#1302)
- keycloak: Update TLS certificate mount paths in Helm values template (osism/ansible-collection-services#1303)
- cloudnative_pg: Wait for webhook service to be ready before proceeding (osism/ansible-collection-services#1306)

### Fixed
- keycloak: Fix double slash in deploy values file path (osism/ansible-collection-services#1303)
- keycloak: Fix documentation to reflect renamed variables (osism/ansible-collection-services#1303)
- nexus: Fix yamllint warning by replacing `yes` with `true` (osism/ansible-collection-services#1308)

### Removed
- `molecule/default` directory (osism/ansible-collection-services#1295)
- Keycloak molecule test job and associated test/prepare/vars files (osism/ansible-collection-services#1296)
- Keycloak Docker Compose deployment, Traefik integration, and MariaDB/Galera backend support (osism/ansible-collection-services#1296)
- keycloak: Remove handler-based chart deployment in favor of explicit deploy task (osism/ansible-collection-services#1301)

### Dependencies
- ansible 9.1.0 → 9.2.0 (osism/ansible-collection-services#1278)
- quay.io/osism/nexus 3.64.0 → 3.65.0 (osism/ansible-collection-services#1285)
- quay.io/osism/ara-server 1.7.0 → 1.7.1 (osism/ansible-collection-services#1286)
- molecule 6.0.3 → 24.2.0 (osism/ansible-collection-services#1288)
- mariadb 11.2.2 → 11.2.3 (osism/ansible-collection-services#1292)
- postgres 15.5-alpine → 15.6-alpine (osism/ansible-collection-services#1293)
- traefik 2.10.7 → 2.11.0 (osism/ansible-collection-services#1294)
- pytest-testinfra 10.0.0 → 10.1.0 (osism/ansible-collection-services#1299)
- pytest 8.0.0 → 8.0.1 (osism/ansible-collection-services#1305)

## [v0.20240204.0] - 2024-02-04

### Added
- Thanos sidecar role for deploying Thanos sidecar alongside Prometheus (osism/ansible-collection-services#1221)
- Manager: MariaDB healthcheck is now automatically set based on the MariaDB image version (osism/ansible-collection-services#1224) (osism/ansible-collection-services#1225)
- Unit tests (pt. 1) with testinfra verification for multiple roles including adminer, auditd, bird, cephclient, cgit, dnsdist, docker, falco, homer, netbox, nexus, openstack_health_monitor, openstackclient, phpmyadmin, scaphandre, squid, traefik, virtualbmc, and others (osism/ansible-collection-services#1238)
- Testinfra tests for multiple roles including keycloak, manager, metering, netdata, openldap, osquery, smartd, and others (osism/ansible-collection-services#1184)
- `ara_server_mariadb_volume_type` parameter in manager role to support tmpfs volumes for MariaDB (osism/ansible-collection-services#1244)
- `netbox_postgres_volume_type` parameter in netbox role to support tmpfs volumes for PostgreSQL (osism/ansible-collection-services#1245)
- Support for `OSISM_APPLY_RETRY` environment variable in the manager wrapper (osism/ansible-collection-services#1258)
- Statsd configuration options for Zuul Scheduler, Nodepool builder and launcher
- Metrics configuration option for Zuul Zookeeper component

### Changed
- Manager: Ensure all containers are up after service restart or start, with a wait period before checking (osism/ansible-collection-services#1234) (osism/ansible-collection-services#1235) (osism/ansible-collection-services#1236) (osism/ansible-collection-services#1237)
- Manager role now allows passing arguments to `osism update manager` and `osism update docker` commands (osism/ansible-collection-services#1242)
- Manager: make redis stateless (osism/ansible-collection-services#1281)
- Openstackclient service start improved by moving health check and bash completion to handlers (osism/ansible-collection-services#1246)
- Squid role no longer performs dstdomain filtering, all external access is now allowed (osism/ansible-collection-services#1249)
- Homer role replaces `homer_kibana_url` with `homer_url_opensearch_dashboards` and updates docs/issues URLs (osism/ansible-collection-services#1251)
- Revived and simplified the nexus service, removing Traefik path prefix and legacy proxy configurations, adding `nexus_bind_host` variable, and adding docker-osism proxy repository (osism/ansible-collection-services#1252)
- Docker: force cache update when repository is added instead of using cache valid time (osism/ansible-collection-services#1259)
- Docker: move proxy settings to the daemon.json file
- Docker: always update the package cache (osism/ansible-collection-services#1282)
- Docker: ensure docker-buildx-plugin and docker-ce-rootless-extras packages are not installed
- Docker wrappers: make `INTERACTIVE=false` environment override work in both directions
- Remove hardcoded amd64 architecture from repository definitions for dynamic arch resolution (osism/ansible-collection-services#1270)
- Zuul: make volume settings configurable with new `zuul_log_volume` and `zuul_mariadb_volume` parameters
- Zuul: add restart policy `unless-stopped` to all services
- Zuul CI job definitions simplified by moving file filters to job definitions (osism/ansible-collection-services#1253)
- Disable Zuul CI jobs for openldap, openstack_health_monitor, and zuul roles that may be removed in the future (osism/ansible-collection-services#1262)
- Wireguard: use `no_log` for "Copy client configuration files" to prevent preshared key logging

### Fixed
- Docker: only unlock containerd package when it is already installed (osism/ansible-collection-services#1260)
- Containerd: only unlock package when it is already installed (osism/ansible-collection-services#1261)
- Fix netdata repository reference missing distribution release (osism/ansible-collection-services#1272)

### Removed
- `homer_kibana_url` parameter from homer role, replaced by `homer_url_opensearch_dashboards` (osism/ansible-collection-services#1251)
- Squid dstdomain whitelist (`squid_allowed_addresses` and related parameters) (osism/ansible-collection-services#1249)

### Dependencies
- ansible 8.6.1 → 9.2.0 (osism/ansible-collection-services#1218) (osism/ansible-collection-services#1219) (osism/ansible-collection-services#1231) (osism/ansible-collection-services#1232) (osism/ansible-collection-services#1279)
- docker 24.0.7 → 24.0.9 (osism/ansible-collection-services#1274)
- hashicorp/vault 1.15.2 → 1.15.5 (osism/ansible-collection-services#1227) (osism/ansible-collection-services#1229) (osism/ansible-collection-services#1280)
- jinja2 3.1.2 → 3.1.3 (osism/ansible-collection-services#1257)
- molecule 6.0.2 → 6.0.3 (osism/ansible-collection-services#1241)
- netaddr 0.9.0 → 0.10.1 (osism/ansible-collection-services#1250)
- pytest 7.4.0 → 8.0.0 (osism/ansible-collection-services#1239) (osism/ansible-collection-services#1247) (osism/ansible-collection-services#1275)
- pytest-testinfra 8.1.0 → 10.0.0 (osism/ansible-collection-services#1240)
- quay.io/osism/nexus 3.62.0 → 3.64.0 (osism/ansible-collection-services#1228) (osism/ansible-collection-services#1256)
- redis 7.2.3 → 7.2.4 (osism/ansible-collection-services#1255)
- traefik 2.10.5 → 2.10.7 (osism/ansible-collection-services#1226) (osism/ansible-collection-services#1233)
- actions/setup-python v4 → v5 (osism/ansible-collection-services#1230)

## [v0.20231126.0] - 2023-11-26

### Added
- Additional parameters for the ara-server service in the manager role (`ara_threads`, `ara_worker_connections`) and changed default of `ara_worker_class` to gevent (osism/ansible-collection-services#1165)
- Deprecation notice to the `osism-custom` wrapper script (osism/ansible-collection-services#1167)
- Manager: `osism-update-docker` wrapper script for updating the Docker service on the manager, also available via `osism update docker` (osism/ansible-collection-services#1172)
- Manager: set `MARIADB_AUTO_UPGRADE=1` environment variable for the MariaDB container to enable automatic upgrades (osism/ansible-collection-services#1169)
- Manager: make OpenSearch protocol configurable via `manager_opensearch_protocol` parameter (osism/ansible-collection-services#1183)
- Manager: allow resource limits for Ansible services via `manager_mem_limit`, `manager_mem_reservation`, and `manager_cpus` parameters (osism/ansible-collection-services#1185)
- Manager: add health checks for listener, openstack, watchdog, netbox worker, and conductor services (osism/ansible-collection-services#1190) (osism/ansible-collection-services#1191)
- Manager: make git sources configurable in `osism update manager` script via `ANSIBLE_COLLECTION_SERVICES_SOURCE` and `ANSIBLE_PLAYBOOKS_MANAGER_SOURCE` environment variables (osism/ansible-collection-services#1201)
- Squid: add `.debian.org` to allowed targets so Debian-based servers can download packages (osism/ansible-collection-services#1192)
- Traefik health check using `/ping` endpoint (osism/ansible-collection-services#1203)
- Netbox worker service health check using process detection (osism/ansible-collection-services#1204)
- Squid container health check using process detection (osism/ansible-collection-services#1205)
- Wait for healthy openstackclient and cephclient containers before copying bash completion scripts (osism/ansible-collection-services#1209)
- Install `jq` as required package for manager health check handler (osism/ansible-collection-services#1214)

### Changed
- Migrated Ansible Molecule tests from GitHub Actions to Zuul
- Simplified Zuul job names by replacing `ansible-molecule` with `molecule` prefix
- Molecule driver name changed from `delegated` to `default` for molecule v6 compatibility (osism/ansible-collection-services#1129)
- Default squid image tag from 5.2-22.04_beta to 5.7-23.04_beta (osism/ansible-collection-services#1166)
- Manager: disable the listener service by default; set `enable_listener: true` to re-enable (osism/ansible-collection-services#1171)
- Manager: use `healthcheck.sh` script for MariaDB healthcheck instead of `mysqladmin` (osism/ansible-collection-services#1181)
- Manager: "Wait for an healthy manager service" task now also waits for containers in `created` state (osism/ansible-collection-services#1189)
- Manager: after a service restart, always wait for a healthy service before continuing (osism/ansible-collection-services#1200)
- Manager: update osismclient bash completion always and at the end via handler (osism/ansible-collection-services#1199)
- Manager: only copy the bash completion script when the manager service is healthy (osism/ansible-collection-services#1202)
- Manager: improve `osism-update-docker` script with full standalone playbook execution support (osism/ansible-collection-services#1206)
- Manager: improve "Wait for an healthy manager service" handler to use `docker compose` and `jq` instead of multiple `docker ps` calls (osism/ansible-collection-services#1210)
- Manager: ignore errors in "Copy osismclient bash completion script" task (osism/ansible-collection-services#1212)
- Manager: only install requirements in `osism-update-docker` when `requirements.txt` exists (osism/ansible-collection-services#1215)
- Documentation build removed, docs migrated to osism.github.io (osism/ansible-collection-services#1186)
- Allow use of ansible-core 2.16 by extending version constraint to `<2.17.0` (osism/ansible-collection-services#1222)

### Fixed
- Fix yamllint issues in release notes and netbox role (osism/ansible-collection-services#1173)
- Fix flake8 issues in documentation config and netbox startup scripts (osism/ansible-collection-services#1174)
- Manager: copy bash completion script only when Celery integration is enabled (osism/ansible-collection-services#1188)
- Manager: set `fs.inotify.max_user_instances = 256` to fix "Too many open files" issue (osism/ansible-collection-services#1211)
- Chrony: check if `systemd-timesyncd` service exists before attempting to stop/disable it (osism/ansible-collection-services#1196)

### Removed
- Removed `osism-mirror` wrapper script from the manager role, replaced by scripts in the `osism/sbom` repository
- Remove patchman and patchman_client roles, which were deprecated with OSISM 6.0.0 (osism/ansible-collection-services#1162)

### Dependencies
- netaddr 0.8.0 → 0.9.0 (osism/ansible-collection-services#1153)
- molecule 5.1.0 → 6.0.2 (osism/ansible-collection-services#1129)
- ansible 8.4.0 → 8.6.1 (osism/ansible-collection-services#1175) (osism/ansible-collection-services#1176) (osism/ansible-collection-services#1193) (osism/ansible-collection-services#1194) (osism/ansible-collection-services#1207) (osism/ansible-collection-services#1208)
- mariadb 10.11.5 → 11.2.2 (osism/ansible-collection-services#1076) (osism/ansible-collection-services#1216) (osism/ansible-collection-services#1220)
- quay.io/osism/virtualbmc 3.0.1 → 3.1.0 (osism/ansible-collection-services#1155)
- hashicorp/vault 1.14.3 → 1.15.2 (osism/ansible-collection-services#1158) (osism/ansible-collection-services#1180) (osism/ansible-collection-services#1195)
- quay.io/osism/homer v23.05.1 → v23.10.1 (osism/ansible-collection-services#1160) (osism/ansible-collection-services#1179)
- quay.io/osism/nexus 3.60.0 → 3.62.0 (osism/ansible-collection-services#1170) (osism/ansible-collection-services#1198)
- traefik v2.10.4 → 2.10.5 (osism/ansible-collection-services#1177)
- redis 7.2.1-alpine → 7.2.3-alpine (osism/ansible-collection-services#1178) (osism/ansible-collection-services#1187)
- docker 5:24.0.6 → 5:24.0.7 (osism/ansible-collection-services#1182)
- postgres 15.4-alpine → 15.5-alpine (osism/ansible-collection-services#1213)

## [v0.20230919.0] - 2023-09-19

### Removed
- Unused Open Policy Agent (OPA) integration from the docker role (osism/ansible-collection-services#1152)
- Unused OpenStack Zun integration from the docker role (osism/ansible-collection-services#1154)

## [v0.20230915.0] - 2023-09-15

### Added
- Handle update manager in osism wrapper script (osism/ansible-collection-services#1149)

### Changed
- Update Zuul and Nodepool image references to quay.io registry, Zuul 8.2.0 → 9.1.0, Nodepool 8.2.0 → 9.0.0 (osism/ansible-collection-services#1147)
- Update documentation link to new docs website (osism/ansible-collection-services#1150)

### Dependencies
- ansible 8.3.0 → 8.4.0 (osism/ansible-collection-services#1144) (osism/ansible-collection-services#1145)
- ara-server 1.6.1 → 1.7.0 (osism/ansible-collection-services#1146)
- docker 24.0.5 → 24.0.6 (osism/ansible-collection-services#1140)
- hashicorp/vault 1.14.2 → 1.14.3 (osism/ansible-collection-services#1148)
- nexus 3.59.0 → 3.60.0 (osism/ansible-collection-services#1143)
- redis 7.2.0 → 7.2.1 (osism/ansible-collection-services#1142)

## [v0.20230906.0] - 2023-09-06

### Changed
- Add deprecation note to old manager wrapper scripts recommending the OSISM CLI (osism/ansible-collection-services#1141)

### Dependencies
- quay.io/osism/dnsdist 1.7.3 → 1.8.0 (osism/ansible-collection-services#1138)
- actions/checkout v3 → v4 (osism/ansible-collection-services#1139)

## [v0.20230901.0] - 2023-09-01

### Added
- New metering role for billing data collection (osism/ansible-collection-services#1091)

### Changed
- squid: Refactor `squid_allowed_addresses` into defaults and extra lists for better flexibility (osism/ansible-collection-services#1115)
- manager: Add full configuration repository to inventory-reconciler with backward compatibility for versions <= 5.2.0 (osism/ansible-collection-services#1119, osism/ansible-collection-services#1120, osism/ansible-collection-services#1121)
- auditd: Sync neo23x0 rules (osism/ansible-collection-services#1122)
- rsyslog: Make additional log server protocol configurable and improve documentation

### Fixed
- netbox: Ensure default network is available for postgres and redis services (osism/ansible-collection-services#1113)

### Removed
- traefik: Remove default network and related `traefik_network`/`docker_network_mtu` parameters (osism/ansible-collection-services#1114)
- docker: Remove unused `docker_dragonfly` parameter (osism/ansible-collection-services#1123)

### Dependencies
- ansible 8.2.0 → 8.3.0 (osism/ansible-collection-services#1131, osism/ansible-collection-services#1132)
- dnsdist 1.6.1 → 1.7.3 (osism/ansible-collection-services#1137)
- docker 24.0.4 → 24.0.5 (osism/ansible-collection-services#1116)
- hashicorp/vault 1.14.0 → 1.14.2 (osism/ansible-collection-services#1118, osism/ansible-collection-services#1135)
- mariadb 10.11.4 → 10.11.5 (osism/ansible-collection-services#1130)
- nexus 3.58.1 → 3.59.0 (osism/ansible-collection-services#1134)
- postgres 15.3 → 15.4 (osism/ansible-collection-services#1128)
- redis 7.0.12 → 7.2.0 (osism/ansible-collection-services#1133)
- traefik v2.10.3 → v2.10.4 (osism/ansible-collection-services#1117)

## [v0.20230722.1] - 2023-07-22

### Changed
- Replace `docker_compose` task with `ansible.builtin.command` in manager and netbox roles to remove python docker-compose dependency (osism/ansible-collection-services#1112)

### Dependencies
- keycloak 19.0.1-legacy → 19.0.3-legacy (osism/ansible-collection-services#1111)

## [v0.20230722.0] - 2023-07-22

### Added
- New `tuned` role for installing and configuring tuned (osism/ansible-collection-services#1091)
- Support for `init.sql` file to speed up netbox database initialization (osism/ansible-collection-services#1088)
- OpenSearch integration for the manager role (osism/ansible-collection-services#1090)
- Missing container restart handler for cephclient (osism/ansible-collection-services#1081)
- Persistent volume for squid cache storage (osism/ansible-collection-services#1095)
- Squid cache configuration (memory, object sizes, cache directory) (osism/ansible-collection-services#1095)
- `wait-for-an-healthy-manager-service` tag to manager service health check task (osism/ansible-collection-services#1107)

### Changed
- Pin Sphinx version to 6.2.1 to fix broken documentation build pipeline (osism/ansible-collection-services#558)
- Refactor ansible-lint rules and noqa annotations for cleaner linting configuration (osism/ansible-collection-services#1078)
- Use `requirements.yml` for Ansible collection dependencies instead of mock modules (osism/ansible-collection-services#1019)
- Update squid allowed addresses to whitelist regio.digital/regiocloud.tech services
- Netbox initializers can now be disabled via `netbox_init` variable (osism/ansible-collection-services#1088)
- Netbox postgres healthcheck now uses netbox user and includes a start period (osism/ansible-collection-services#1088)
- Improve start of the netbox-worker service by using proper `depends_on` health condition and explicit network configuration (osism/ansible-collection-services#1106)
- Handle service start errors via block/rescue for manager and netbox services (osism/ansible-collection-services#1108)

### Removed
- Remove minikube role in favor of k3s (osism/ansible-collection-services#1103)
- Remove unused jenkins role (osism/ansible-collection-services#1104)
- Remove unused rundeck role (osism/ansible-collection-services#1105)

### Dependencies
- docker 5:20.10.24 → 5:24.0.4 (osism/ansible-collection-services#1044)
- quay.io/osism/nexus 3.55.0 → 3.58.1 (osism/ansible-collection-services#1082, osism/ansible-collection-services#1096, osism/ansible-collection-services#1099, osism/ansible-collection-services#1109)
- traefik v2.10.1 → v2.10.3 (osism/ansible-collection-services#1084)
- hashicorp/vault 1.13.3 → 1.14.0 (osism/ansible-collection-services#1083)
- ansible 8.0.0 → 8.2.0 (osism/ansible-collection-services#1085, osism/ansible-collection-services#1086, osism/ansible-collection-services#1100, osism/ansible-collection-services#1101)
- molecule 5.0.1 → 5.1.0 (osism/ansible-collection-services#1087)
- redis 7.0.11-alpine → 7.0.12-alpine (osism/ansible-collection-services#1098)

## [v0.20230614.0] - 2023-06-14

### Added
- Scaphandre role for electrical power consumption metrics with configurable exporter and flags (osism/ansible-collection-services#1042, osism/ansible-collection-services#1045, osism/ansible-collection-services#1046)
- `manager_service_restart` parameter to control restart handler behavior (osism/ansible-collection-services#1043)
- Environment variables `CONFIGURATION_DIRECTORY`, `ANSIBLE_INVENTORY`, and `ANSIBLE_PRIVATE_KEY` to osism-update-manager script (osism/ansible-collection-services#1033)
- Configurable Python executable (`PYTHON_EXECUTABLE`) in osism-update-manager script (osism/ansible-collection-services#1036)
- Share volume for the osismclient service to share keys with *-ansible containers (osism/ansible-collection-services#1061)
- Wait for a healthy manager service before proceeding with further tasks
- frr: Backup config for loadbalancer to support active/passive scenarios with higher metric on internal and external BGP sessions (osism/ansible-collection-services#1058)
- manager: Mount Docker socket in osismclient container for container inspection (osism/ansible-collection-services#1074)

### Changed
- rng: Replace haveged with rngd for enhanced entropy behavior (osism/ansible-collection-services#1025)
- docker: Allow downgrade of docker packages when version is pinned
- squid: Allow subdomains for quay.io and archive.ubuntu.com (osism/ansible-collection-services#1031)
- squid: Add `.cloudfront.net` to whitelist for packagecloud.io CDN (osism/ansible-collection-services#1034)
- squid: Allow Docker Hub addresses (registry-1.docker.io, auth.docker.io, production.cloudflare.docker.com)
- squid: Sort allowed addresses alphabetically
- ansible-lint: Mock missing modules and skip `args[module]` rule (osism/ansible-collection-services#1020)
- ansible-lint: Use `package-latest` rule name instead of deprecated `403` (osism/ansible-collection-services#1037)
- ansible-lint: Enable `fqcn-builtins` rule (osism/ansible-collection-services#1047)
- ansible-lint: Enable `var-spacing` rule and fix all violations across roles (osism/ansible-collection-services#1048)
- ansible-lint: Enable `args[module]` rule (osism/ansible-collection-services#1050)
- ansible-lint: Enable `parser-error` rule (osism/ansible-collection-services#1052)
- ansible-lint: Enable `name[template]` rule and reorder task name templates to avoid variable at start (osism/ansible-collection-services#1053)
- Remove Ubuntu 20.04 from CI test matrix (osism/ansible-collection-services#1051)
- manager: Increase wait timeout for healthy services from 300s to 1000s to handle slow Netbox availability
- manager: Always use pinned Ansible version in virtual environment for osism-update-manager (osism/ansible-collection-services#1068)
- Update supported Ansible versions to >=2.14.0,<2.16.0 (osism/ansible-collection-services#1077)

### Fixed
- Manager: Avoid 2nd manager restart in the osism.manager.manager playbook
- Manager: Set executable to /bin/bash for healthy manager service check to support pipefail (osism/ansible-collection-services#1065)
- Netbox: Avoid restart when service was started via ansible.builtin.service to prevent issues with initial database bootstrap
- chrony: Fix use of local chrony template file referencing wrong variable

### Dependencies
- ansible 7.4.0 → 8.0.0 (osism/ansible-collection-services#1028, osism/ansible-collection-services#1029, osism/ansible-collection-services#1056, osism/ansible-collection-services#1057, osism/ansible-collection-services#1059, osism/ansible-collection-services#1060)
- hashicorp/vault 1.13.1 → 1.13.3 (osism/ansible-collection-services#1030, osism/ansible-collection-services#1071)
- mariadb 10.11.2 → 10.11.4 (osism/ansible-collection-services#1039, osism/ansible-collection-services#1075)
- molecule 4.0.4 → 5.0.1 (osism/ansible-collection-services#1026)
- postgres 15.2-alpine → 15.3-alpine (osism/ansible-collection-services#1038)
- quay.io/osism/homer v23.02.2 → v23.05.1 (osism/ansible-collection-services#1041)
- quay.io/osism/netbox v3.4.7 → v3.4.8 (osism/ansible-collection-services#1017)
- quay.io/osism/nexus 3.51.0 → 3.55.0 (osism/ansible-collection-services#1022, osism/ansible-collection-services#1035, osism/ansible-collection-services#1040, osism/ansible-collection-services#1055, osism/ansible-collection-services#1067)
- redis 7.0.10-alpine → 7.0.11-alpine (osism/ansible-collection-services#1018)
- traefik v2.9.10 → v2.10.1 (osism/ansible-collection-services#1027, osism/ansible-collection-services#1032)

## [v0.20230407.0] - 2023-04-07

### Added
- Periodic-daily jobs (yamllint, ansible-lint, flake8) in Zuul CI (osism/ansible-collection-services#1012)

### Fixed
- Auditd handler syntax check by adding `changed_when` to "Generate auditd rules" handler

### Dependencies
- redis 7.0.9 → 7.0.10 (osism/ansible-collection-services#1004)
- ansible 7.3.0 → 7.4.0 (osism/ansible-collection-services#1008, osism/ansible-collection-services#1009)
- traefik v2.9.8 → v2.9.10 (osism/ansible-collection-services#1005, osism/ansible-collection-services#1016)
- nexus 3.49.0 → 3.51.0 (osism/ansible-collection-services#1006, osism/ansible-collection-services#1015)
- netbox v3.4.6 → v3.4.7 (osism/ansible-collection-services#1010)
- vault 1.13.0 → 1.13.1 (osism/ansible-collection-services#1011)
- docker 20.10.23 → 20.10.24 (osism/ansible-collection-services#1013)

## [v0.20230321.0] - 2023-03-21

### Added
- Allow disabling/enabling the openstack health monitor cronjob (osism/ansible-collection-services#1002)
- Sync reconciler after a manager update (osism/ansible-collection-services#832)

### Changed
- Enable celery by default and disable flower by default in manager role (osism/ansible-collection-services#1003)

### Dependencies
- quay.io/osism/netbox v3.4.5 → v3.4.6 (osism/ansible-collection-services#1001)

## [v0.20230312.0] - 2023-03-12

### Added
- Zuul installation guide with documentation for server preparation, secrets, GitHub App setup, and example playbook (osism/ansible-collection-services#959)
- `enable_listener` option to enable/disable the listener service in the manager role (osism/ansible-collection-services#1000)

### Changed
- Refactored wireguard role to support multiple VPN clients with per-user peer configuration (osism/ansible-collection-services#927)
- Zuul role variables renamed with `zuul_` prefix to avoid conflicts with other roles (osism/ansible-collection-services#959)

### Removed
- Removed all "Wait for apt lock" tasks from roles auditd, bird, cephclient, chrony, clamav, containerd, docker, fail2ban, falco, frr, hddtemp, lldpd, manager, netdata, openstackclient, osquery, patchman_client, rng, rsyslog, smartd, and tang (osism/ansible-collection-services#979, osism/ansible-collection-services#980, osism/ansible-collection-services#981, osism/ansible-collection-services#982, osism/ansible-collection-services#983, osism/ansible-collection-services#984, osism/ansible-collection-services#985, osism/ansible-collection-services#986, osism/ansible-collection-services#987, osism/ansible-collection-services#988, osism/ansible-collection-services#989, osism/ansible-collection-services#990, osism/ansible-collection-services#991, osism/ansible-collection-services#992, osism/ansible-collection-services#993, osism/ansible-collection-services#994, osism/ansible-collection-services#995, osism/ansible-collection-services#996, osism/ansible-collection-services#997, osism/ansible-collection-services#998, osism/ansible-collection-services#999)

### Dependencies
- quay.io/osism/virtualbmc 3.0.0 → 3.0.1 (osism/ansible-collection-services#978)

## [v0.20230308.0] - 2023-03-08

### Added
- Kernel module `drivetemp` for disk and NVMe temperature monitoring via lm-sensors on Ubuntu 22.04+ (osism/ansible-collection-services#977)

## [v0.12.0] - 2023-03-07

### Changed
- Set apt lock timeout to 300 seconds by default across all roles (osism/ansible-collection-services#973)
- Use lm-sensors instead of hddtemp on Ubuntu 22.04 (osism/ansible-collection-services#974)
- Use `get_url` for GPG keys instead of deprecated `apt-key` on Ubuntu 22.04 (osism/ansible-collection-services#975)

### Dependencies
- hashicorp/vault 1.12.3 → 1.13.0 (osism/ansible-collection-services#971)
- quay.io/osism/nexus 3.48.0 → 3.49.0 (osism/ansible-collection-services#976)

## [v0.11.0] - 2023-03-01

### Added
- New osquery role for installing and configuring osquery (osism/ansible-collection-services#886)
- Containerd role for standalone containerd installation and management (osism/ansible-collection-services#669)
- FRR configuration templates for leaf and loadbalancer types with BGP support (osism/ansible-collection-services#880)
- Manager: copy osismclient bash completion script (osism/ansible-collection-services#917)
- Manager: add /opt/state volume to the conductor service (osism/ansible-collection-services#925)
- Manager: add /opt/state volume to the ara-server service (osism/ansible-collection-services#926)
- Manager: allow disabling beat and flower services via `beat_enable` and `flower_enable` parameters (osism/ansible-collection-services#929)
- Manager: add `/interface` volume to the osismclient container for reading available playbooks (osism/ansible-collection-services#941)
- Openstackclient: add REQUESTS_CA_BUNDLE environment variable (osism/ansible-collection-services#918)
- Netbox: add device role loadbalancer (osism/ansible-collection-services#916)
- Netbox: add device role "Housing" (osism/ansible-collection-services#900)
- Netdata: add `page_cache_size` and `accept_a_streaming_request_every_seconds` configuration options (osism/ansible-collection-services#902)
- dnsdist: allow multiple host bindings with `dnsdist_hosts` parameter (osism/ansible-collection-services#928)
- docker: add `docker_facts` parameter to control copying of docker fact files (osism/ansible-collection-services#945)
- zuul: add auth config for `zuul_operator` to allow token generation for zuul-client (osism/ansible-collection-services#953)
- zuul: add `zuul_user` variable to role defaults (osism/ansible-collection-services#953)
- zuul: add squash-merge mode (osism/ansible-collection-services#957)
- CI: enable ansible-lint, yamllint, and flake8 checks via Zuul jobs (osism/ansible-collection-services#949)(osism/ansible-collection-services#956)(osism/ansible-collection-services#961)

### Changed
- Refactor ansible-lint rules for fixing issues after version update (osism/ansible-collection-services#843)
- Fix ansible-lint errors by replacing `copy` with `template` module for secret/config files across cephclient, keycloak, manager, netbox, openldap, rundeck, and traefik roles, and fix task name casing in zuul role (osism/ansible-collection-services#846)
- Fix creating netbox secret files by using `template` instead of `copy` for remaining location (osism/ansible-collection-services#847)
- Remove deprecated `version` key from docker-compose files across multiple roles (osism/ansible-collection-services#417)
- Remove remaining docker-compose version keys from cgit, dnsdist, nexus, squid, traefik, and zuul roles (osism/ansible-collection-services#885)
- openstack-health-monitor: use docker-compose systemd service instead of direct docker-compose commands (osism/ansible-collection-services#887)
- netbox: fix static share path for nginx unit > 1.26 (osism/ansible-collection-services#895)
- netbox: update to v3.3.9 and add support for older nginx unit versions (osism/ansible-collection-services#896, osism/ansible-collection-services#897)
- netbox: enable netbox_initializers plugin by default (osism/ansible-collection-services#915)
- netbox: wait for healthy Redis and PostgreSQL services using `condition: service_healthy` (osism/ansible-collection-services#935)
- Homer: update dark mode color scheme (osism/ansible-collection-services#913)
- ansible-lint: only warn about experimental rules instead of failing (osism/ansible-collection-services#906)
- ansible-lint: add `galaxy[no-changelog]` to skip list (osism/ansible-collection-services#922)
- Auditd: sync rules with Neo23x0/auditd (osism/ansible-collection-services#923)
- Change copyright date to 2022-2023 (osism/ansible-collection-services#910)
- Manager: improve readability of docker-compose template with section comments (osism/ansible-collection-services#934)
- Manager: wait for healthy Redis and database services using `condition: service_healthy` (osism/ansible-collection-services#936)
- Manager: decouple listener and openstack services from mandatory Netbox dependency (osism/ansible-collection-services#934)
- zuul: fix mismatched variable names for nodepool images (osism/ansible-collection-services#953)
- zuul: rename `zuul_tag` to `zuul_zuul_tag` for consistency and reorder definitions alphabetically (osism/ansible-collection-services#955)
- Add Ubuntu Jammy (22.04) to supported platforms and update Ansible version requirement to <2.15.0 (osism/ansible-collection-services#965)
- CI: update test-role workflows to use Python 3.10 (osism/ansible-collection-services#950)
- CI: remove GitHub Action checks for ansible-lint and yamllint in favor of Zuul (osism/ansible-collection-services#949)(osism/ansible-collection-services#956)

### Fixed
- docker: correctly update apt cache when repository is added (osism/ansible-collection-services#876)
- github: narrow wireguard test trigger to avoid running for all changes in molecule/delegated (osism/ansible-collection-services#883)
- Molecule: fix rng and hddtemp tests (osism/ansible-collection-services#911)
- Manager: add missing `if` in Jinja2 template for beat and flower service blocks (osism/ansible-collection-services#930)
- Manager: do not fail deployment when osismclient container is not yet available (osism/ansible-collection-services#933)
- Manager: remove duplicate healthcheck test line for MariaDB (osism/ansible-collection-services#936)
- Netbox: add missing colon in docker-compose depends_on syntax (osism/ansible-collection-services#937)

### Removed
- Drop Kata container integration from docker role (osism/ansible-collection-services#837)
- Remove cockpit from README roles list (osism/ansible-collection-services#884)
- openstackclient: remove ospurge wrapper script (osism/ansible-collection-services#839)
- Remove unused `*_traefik_path_prefix` and `*_traefik_host` variables from cgit, keycloak, manager, netbox, patchman, and phpmyadmin roles (osism/ansible-collection-services#919)
- Remove custom ansible-lint rules directory (osism/ansible-collection-services#966)

### Dependencies
- ansible 6.3.0 → 7.3.0 (osism/ansible-collection-services#835, osism/ansible-collection-services#836, osism/ansible-collection-services#855, osism/ansible-collection-services#856, osism/ansible-collection-services#869, osism/ansible-collection-services#870, osism/ansible-collection-services#878, osism/ansible-collection-services#890, osism/ansible-collection-services#891, osism/ansible-collection-services#951, osism/ansible-collection-services#967, osism/ansible-collection-services#968)
- docker 5:20.10.17 → 5:20.10.23 (osism/ansible-collection-services#833, osism/ansible-collection-services#857, osism/ansible-collection-services#860, osism/ansible-collection-services#862, osism/ansible-collection-services#904, osism/ansible-collection-services#924)
- traefik v2.8.4 → v2.9.8 (osism/ansible-collection-services#834, osism/ansible-collection-services#842, osism/ansible-collection-services#850, osism/ansible-collection-services#851, osism/ansible-collection-services#864, osism/ansible-collection-services#874, osism/ansible-collection-services#892, osism/ansible-collection-services#952, osism/ansible-collection-services#954)
- mariadb 10.9.2 → 10.11.2 (osism/ansible-collection-services#840, osism/ansible-collection-services#873, osism/ansible-collection-services#875, osism/ansible-collection-services#943, osism/ansible-collection-services#958)
- redis 7.0.4 → 7.0.9 (osism/ansible-collection-services#841, osism/ansible-collection-services#894, osism/ansible-collection-services#903, osism/ansible-collection-services#921, osism/ansible-collection-services#970)
- postgres 14.5 → 15.2-alpine (osism/ansible-collection-services#858, osism/ansible-collection-services#872, osism/ansible-collection-services#948)
- quay.io/osism/nexus 3.41.1 → 3.48.0 (osism/ansible-collection-services#845, osism/ansible-collection-services#867, osism/ansible-collection-services#901, osism/ansible-collection-services#908, osism/ansible-collection-services#920, osism/ansible-collection-services#932, osism/ansible-collection-services#946, osism/ansible-collection-services#947, osism/ansible-collection-services#969)
- quay.io/osism/homer v22.08.1 → v23.02.2 (osism/ansible-collection-services#853, osism/ansible-collection-services#865, osism/ansible-collection-services#871, osism/ansible-collection-services#881, osism/ansible-collection-services#944, osism/ansible-collection-services#962)
- hashicorp/vault 1.11.3 → 1.12.3 (osism/ansible-collection-services#848, osism/ansible-collection-services#854, osism/ansible-collection-services#866, osism/ansible-collection-services#879, osism/ansible-collection-services#942)
- quay.io/osism/netbox v3.2.5-ldap → v3.4.5 (osism/ansible-collection-services#896, osism/ansible-collection-services#899, osism/ansible-collection-services#909, osism/ansible-collection-services#938, osism/ansible-collection-services#940, osism/ansible-collection-services#963)
- quay.io/osism/ara-server 1.5.8 → 1.6.1 (osism/ansible-collection-services#889, osism/ansible-collection-services#898)
- quay.io/osism/virtualbmc 2.2.2 → 3.0.0 (osism/ansible-collection-services#863)
- molecule 4.0.1 → 4.0.4 (osism/ansible-collection-services#859, osism/ansible-collection-services#861, osism/ansible-collection-services#888)
- molecule-docker 2.0.0 → 2.1.0 (osism/ansible-collection-services#847)
- jinja2 3.0.3 → 3.1.2 (osism/ansible-collection-services#887)
- zuul/zuul 8.0.1 → 8.2.0 (osism/ansible-collection-services#955)
- zuul/nodepool 8.0.0 → 8.2.0 (osism/ansible-collection-services#955)

## [v0.10.0] - 2022-09-04

### Added
- Documentation for the Adminer role (osism/ansible-collection-services#715)
- Documentation for the auditd role (osism/ansible-collection-services#716)
- Documentation for the bird role (osism/ansible-collection-services#717)
- Documentation for the cephclient role (osism/ansible-collection-services#719)
- Documentation for the cgit role (osism/ansible-collection-services#721)
- Documentation for the Chrony role (osism/ansible-collection-services#722)
- Documentation for the Clamav role (osism/ansible-collection-services#723)
- Documentation for the Dnsdist role (osism/ansible-collection-services#724)
- Documentation for the docker role (osism/ansible-collection-services#729)
- Documentation for the Fail2ban role (osism/ansible-collection-services#730)
- Documentation for the Falco role (osism/ansible-collection-services#731)
- Documentation for the FRR role (osism/ansible-collection-services#732)
- Documentation for the Hddtemp role (osism/ansible-collection-services#733)
- Documentation for the Homer role (osism/ansible-collection-services#734)
- Documentation for the Jenkins role (osism/ansible-collection-services#735)
- Documentation for the Journald role (osism/ansible-collection-services#736)
- Documentation for the Keycloak role (osism/ansible-collection-services#737)
- Documentation for the Manager role (osism/ansible-collection-services#741)
- Documentation for the minikube role (osism/ansible-collection-services#742)
- Documentation for the netbox role (osism/ansible-collection-services#744)
- Documentation for the netdata role (osism/ansible-collection-services#745)
- Documentation for the nexus role (osism/ansible-collection-services#746)
- Documentation for the openldap role (osism/ansible-collection-services#747)
- Documentation for the openstack_health_monitor role (osism/ansible-collection-services#748)
- Documentation for the openstackclient role (osism/ansible-collection-services#749)
- Documentation for the patchman role (osism/ansible-collection-services#750)
- Documentation for the patchman-client role (osism/ansible-collection-services#751)
- Documentation for the phpmyadmin role (osism/ansible-collection-services#752)
- Documentation for the rng role (osism/ansible-collection-services#753)
- Documentation for the rsyslog role (osism/ansible-collection-services#754)
- Documentation for the rundeck role (osism/ansible-collection-services#755)
- Documentation for the smartd role (osism/ansible-collection-services#756)
- Documentation for the traefik role (osism/ansible-collection-services#758)
- Documentation for the virtualbmc role (osism/ansible-collection-services#759)
- Ansible-lint checks with custom OSISM rules for FQCN and attribute ordering (osism/ansible-collection-services#790)
- Squid proxy role for managing allowed addresses via Docker-based deployment (osism/ansible-collection-services#792)
- `manager_enable_bifrost` parameter for bifrost service integration (osism/ansible-collection-services#803)
- `manager_enable_ironic` parameter for ironic service integration (osism/ansible-collection-services#804)
- `wireguard_client_configuration_file` parameter to configure the client configuration filename (osism/ansible-collection-services#807)
- Ubuntu 22.04 test support for multiple roles (auditd, clamav, fail2ban, frr, journald, lldpd, netdata, rng, rsyslog, smartd, wireguard) (osism/ansible-collection-services#810)
- Ubuntu 22.04 test support for chrony role (osism/ansible-collection-services#811)
- Ubuntu 22.04 test support for hddtemp role (osism/ansible-collection-services#814)
- Job to publish docs to docs.osism.tech (osism/ansible-collection-services#815)
- Documentation link in README (osism/ansible-collection-services#816)
- Distribution-specific audisp plugin path configuration for Ubuntu 22.04 (osism/ansible-collection-services#823)

### Changed
- Zuul role container image variable names standardized to match naming conventions of other repositories (osism/ansible-collection-services#786)
- Manager: tune ARA performance with `ARA_DATABASE_CONN_MAX_AGE` and `ARA_CALLBACK_THREADS` settings (osism/ansible-collection-services#801)
- Update `requires_ansible` upper bound from `<2.13.0` to `<2.14.0` in `meta/runtime.yml` (osism/ansible-collection-services#806)
- Manager: mount `environments/openstack` to `/etc/openstack` in conductor container (osism/ansible-collection-services#808)
- Chrony and hddtemp molecule tests migrated from `default` to `delegated` scenario (osism/ansible-collection-services#811) (osism/ansible-collection-services#814)
- Keycloak image tag pinned to `19.0.1-legacy` with Renovate tracking (osism/ansible-collection-services#813)
- Auditd neo23x0 rules synced with upstream (2022/07/19), adding new audit rules for data compression, credential searches, shell profiles, anonymous file creation, IPC, socket creation, and additional suspicious activity monitoring (osism/ansible-collection-services#817)
- Nexus container image source changed to quay.io (osism/ansible-collection-services#818)

### Fixed
- Docker role documentation formatting by replacing code-block with proper note directives (osism/ansible-collection-services#794)
- Squid: use correct `squid_allowed_addresses` variable name in allow list template (osism/ansible-collection-services#799)
- Fix ansible-lint errors across multiple roles: use FQCN for `docker_network` and `docker_login`, add missing `changed_when` and `mode` attributes (osism/ansible-collection-services#800)
- Manager: add missing default value for `manager_enable_ironic` (osism/ansible-collection-services#805)

### Removed
- `scan_services` module removed in favor of `ansible.builtin.service_facts` (osism/ansible-collection-services#812)

### Dependencies
- ansible 5.9.0 → 6.3.0 (osism/ansible-collection-services#774, osism/ansible-collection-services#775, osism/ansible-collection-services#784, osism/ansible-collection-services#785, osism/ansible-collection-services#824, osism/ansible-collection-services#825)
- hashicorp/vault 1.11.0 → 1.11.3 (osism/ansible-collection-services#798, osism/ansible-collection-services#809, osism/ansible-collection-services#828)
- homer 22.02.2 → v22.08.1 (osism/ansible-collection-services#827, osism/ansible-collection-services#831)
- mariadb 10.8.3 → 10.9.2 (osism/ansible-collection-services#826)
- molecule 3.6.1 → 4.0.1 (osism/ansible-collection-services#770, osism/ansible-collection-services#797)
- molecule-docker 1.1.0 → 2.0.0 (osism/ansible-collection-services#795)
- nexus 3.40.1 → 3.41.1 (osism/ansible-collection-services#802, osism/ansible-collection-services#830)
- postgres 14.4-alpine → 14.5-alpine (osism/ansible-collection-services#820)
- redis 7.0.2-alpine → 7.0.4-alpine (osism/ansible-collection-services#791, osism/ansible-collection-services#796)
- traefik v2.7.2 → v2.8.4 (osism/ansible-collection-services#787, osism/ansible-collection-services#819, osism/ansible-collection-services#821, osism/ansible-collection-services#829)

## [v0.9.4] - 2022-06-30

### Added
- Zuul job to create role documentation (osism/ansible-collection-services#685)
- Netbox: add out-of-band custom field for devices (osism/ansible-collection-services#4f05bb5c)
- Cgit: add inventory repository to default repositories (osism/ansible-collection-services#0bc2d14c)
- Manager: make the number of netbox replicas configurable (osism/ansible-collection-services#671)
- Tang role for Network Bound Disk Encryption (osism/ansible-collection-services#706)
- Wireguard role for VPN setup with client/server configuration (osism/ansible-collection-services#688)
- Documentation index entries for all existing roles (osism/ansible-collection-services#714)
- Manager support for updates via seed container image (osism/ansible-collection-services#712)
- Manager conductor.yml mapping for netbox/openstack services (osism/ansible-collection-services#661622c7)
- Configurable logging level for traefik (osism/ansible-collection-services#725)
- Docker role ensures package cache is up to date before installation (osism/ansible-collection-services#698)
- Virtualbmc container name configuration (osism/ansible-collection-services#a089fdd3)
- Ansible configurations (env files, volumes) to the osismclient service in the manager role (osism/ansible-collection-services#743)
- Documentation for the lldpd role (osism/ansible-collection-services#738)
- Description to the tang role documentation (osism/ansible-collection-services#757)
- README.md files to all roles for ansible-galaxy compatibility (osism/ansible-collection-services#788, osism/ansible-collection-services#789)

### Changed
- Add service prefix to infrastructure images to avoid conflicts with Kolla (osism/ansible-collection-services#201a4011)
- Netbox: use absolute versions for redis and postgres images (osism/ansible-collection-services#c5a06ad4)
- Manager: use absolute versions for redis and mariadb images (osism/ansible-collection-services#c3fc74fc)
- Manager: set container names for vault and ansible services after Compose v2 migration (osism/ansible-collection-services#fba51bfd)
- Patchman: do not wait for memcached, only wait for postgres (osism/ansible-collection-services#16647ab2)
- Rename role README files from .md to .rst format (osism/ansible-collection-services#685)
- Nexus traefik router rules now use `nexus_traefik_host` variable instead of `nexus_host` (osism/ansible-collection-services#728)
- Rename `traefik_host` to `nexus_traefik_host` in the nexus role (osism/ansible-collection-services#740)
- Zuul and nodepool updated to 6.0.0 (osism/ansible-collection-services#705)
- Move `become` condition before task parameters in the zuul role (osism/ansible-collection-services#767)
- Add default-branch to zuul configuration (osism/ansible-collection-services#771)
- Remove static port definition fallback from tang template (osism/ansible-collection-services#781)

### Fixed
- Patchman: fix "Wait for patchman service" task to handle Traefik routing delays (osism/ansible-collection-services#edc809fa)
- Manager "Check for conductor.yml" task now reads from remote host instead of localhost (osism/ansible-collection-services#690)
- Manager syntax issue in osism-update-manager script (osism/ansible-collection-services#727)
- Manager fix handling of traefik/netbox in osism-update-manager (osism/ansible-collection-services#661e7ad9)
- Nexus typo in variable `call_script_netxus_url` corrected to `call_script_nexus_url` (osism/ansible-collection-services#707)
- Nexus docker health check now uses correct `/nexus/` path (osism/ansible-collection-services#726)
- Typo in renovate.json for traefik path (osism/ansible-collection-services#496d3fa2)
- Add `become: true` to tang systemd configuration tasks and open firewall port (osism/ansible-collection-services#780)

### Removed
- Cockpit role (osism/ansible-collection-services#f82e95c1)
- Docker: remove docker-compose plugin, now available via osism.common.docker_compose (osism/ansible-collection-services#676)

### Dependencies
- actions/setup-python v3 → v4 (osism/ansible-collection-services#763, osism/ansible-collection-services#764)
- ansible 5.6.0 → 5.9.0 (osism/ansible-collection-services#672, osism/ansible-collection-services#673, osism/ansible-collection-services#682, osism/ansible-collection-services#700, osism/ansible-collection-services#681, osism/ansible-collection-services#701, osism/ansible-collection-services#760, osism/ansible-collection-services#761)
- docker 5:20.10.14 → 20.10.17 (osism/ansible-collection-services#684, osism/ansible-collection-services#693, osism/ansible-collection-services#762)
- docker/setup-buildx-action v1 → v2 (osism/ansible-collection-services#683)
- hashicorp/vault 1.10.0 → 1.11.0 (osism/ansible-collection-services#670, osism/ansible-collection-services#677, osism/ansible-collection-services#692, osism/ansible-collection-services#766, osism/ansible-collection-services#773)
- mariadb 10.8.2 → 10.8.3 (osism/ansible-collection-services#709)
- phpmyadmin/phpmyadmin 5.1 → 5.2 (osism/ansible-collection-services#691)
- postgres 14.2 → 14.4 (osism/ansible-collection-services#699, osism/ansible-collection-services#776)
- quay.io/osism/homer 21.09.2 → 22.02.2 (osism/ansible-collection-services#697)
- quay.io/osism/netbox v3.2.1-ldap → v3.2.5 (osism/ansible-collection-services#694, osism/ansible-collection-services#739, osism/ansible-collection-services#777)
- quay.io/osism/nexus 3.38.0 → 3.40.1 (osism/ansible-collection-services#695, osism/ansible-collection-services#704, osism/ansible-collection-services#778, osism/ansible-collection-services#783)
- quay.io/osism/virtualbmc 2.2.0 → 2.2.2 (osism/ansible-collection-services#696, osism/ansible-collection-services#772)
- redis 6.2.6-alpine → 7.0.2 (osism/ansible-collection-services#674, osism/ansible-collection-services#675, osism/ansible-collection-services#765, osism/ansible-collection-services#768)
- traefik v2.5.4 → v2.7.2 (osism/ansible-collection-services#703, osism/ansible-collection-services#710, osism/ansible-collection-services#769, osism/ansible-collection-services#782)

## [v0.9.3] - 2022-04-22

### Changed
- openstack_health_monitor: Pin image tag to `v3.0.0` instead of `latest` (osism/ansible-collection-services#652)
- docker: Split `docker_proxy_no_proxy` into `docker_proxy_no_proxy_default` and `docker_proxy_no_proxy_extra` for unified proxy configuration with `osism.commons.proxy` (osism/ansible-collection-services#654)
- docker: Use single ticks for version arguments in defaults (osism/ansible-collection-services#662)
- docker: Move `become` directive to the top of tasks for consistency (osism/ansible-collection-services#661)
- docker: Enable Renovate tracking for `docker_version` (osism/ansible-collection-services#660)
- zuul: Update webserver to use SSL with HTTPS, HTTP-to-HTTPS redirect, directory indexing for logs, and httpd reverse proxy for zuul-web (osism/ansible-collection-services#649)
- renovate: Add `github>osism/renovate-config:python` configuration preset
- netbox: Add 120 second healthcheck start period to avoid unnecessary unhealthy state during initial migrations (osism/ansible-collection-services#666)
- cgit: Rewrite `/` to `/cgit` via Traefik middleware for direct root access (osism/ansible-collection-services#668)
- Use Ansible fully qualified collection names (FQCN) in manager role (osism/ansible-collection-services#664)

### Fixed
- Fix logging path in zuul builder role pointing to launcher instead of builder logs (osism/ansible-collection-services#665)
- Fix trailing comma in Renovate configuration

### Dependencies
- quay.io/osism/ara-server 1.5.7 → 1.5.8 (osism/ansible-collection-services#653)
- quay.io/osism/netbox v3.1.9-ldap → v3.2.1-ldap (osism/ansible-collection-services#667)
- zuul 5.0.0 → 5.2.2 (osism/ansible-collection-services#658)
- ansible 5.5.0 → 5.6.0 (osism/ansible-collection-services#656, osism/ansible-collection-services#657)
- docker 20.10.6 → 20.10.14 (osism/ansible-collection-services#663)

## [v0.9.2] - 2022-03-30

### Added
- Renovate regex manager for `osism-update-manager.j2` template to handle Python dependency updates (osism/ansible-collection-services#a10a5588)
- Renovate regex managers for Docker image tags in role defaults (osism/ansible-collection-services#d3893dc1)
- Docker role fact files for collecting container and image information (osism/ansible-collection-services#647)
- rsyslog: additional log server configuration support (osism/ansible-collection-services#645)

### Changed
- manager: use `osism.manager` playbooks from Galaxy instead of local playbook files (osism/ansible-collection-services#644)
- manager: update default ceph-ansible tag from `nautilus` to `pacific` (osism/ansible-collection-services#d3893dc1)
- manager: update default kolla-ansible tag from `victoria` to `xena` (osism/ansible-collection-services#d3893dc1)
- manager: update default vault tag from `latest` to `1.10.0` (osism/ansible-collection-services#d3893dc1)
- docker: rename `docker_open_policy_agent` variables to `docker_openpolicyagent` (osism/ansible-collection-services#b77ef635)
- cgit: switch to versioned quay.io/osism/cgit image, replacing clearlinux/cgit:latest (osism/ansible-collection-services#eca22cea)
- patchman: use versioned image instead of `latest` tag (osism/ansible-collection-services#646)
- patchman: pin postgres and memcached image versions (osism/ansible-collection-services#648)

### Fixed
- docker: fix `AnsibleUndefinedVariable` error for `docker_registry_docker_openpolicyagent` (osism/ansible-collection-services#b331d9ca)
- docker: fix missing `facts/` path prefix when copying fact files (osism/ansible-collection-services#8364009a)

### Dependencies
- ansible 5.2.0 → 5.5.0 (osism/ansible-collection-services#637)
- quay.io/osism/ara-server 1.5.4 → 1.5.7 (osism/ansible-collection-services#639)
- quay.io/osism/netbox v3.0.9-ldap → v3.1.9-ldap (osism/ansible-collection-services#638)
- mariadb 10.5 → 10.8 (osism/ansible-collection-services#640)
- phpmyadmin/phpmyadmin 4.9 → 5.1 (osism/ansible-collection-services#643)
- quay.io/osism/nexus 3.36.0 → 3.38.0 (osism/ansible-collection-services#642)

## [v0.9.1] - 2022-03-26

### Fixed
- Fix wrong parameter name in phpMyAdmin docker-compose template (`nexus_traefik` → `phpmyadmin_traefik`) (osism/ansible-collection-services#57b92661)

## [v0.9.0] - 2022-03-22

### Changed
- Patchman: use `uri` module instead of `wait_for` to wait for the patchman service (osism/ansible-collection-services#635)

### Fixed
- Fix indentation in the Homer config template that broke YAML formatting (osism/ansible-collection-services#636)

## [v0.8.0] - 2022-03-17

### Added
- Zuul: Add nodepool-builder container support (osism/ansible-collection-services#634)
- Zuul: Deploy logging configuration for all services (osism/ansible-collection-services#634)

### Changed
- Homer: Hide service dashboards when their URL is not configured (osism/ansible-collection-services#631)
- Zuul: Use configurable tags for container image versions (osism/ansible-collection-services#634)
- Zuul: Use pre-configured SSH keypair for nodepool/zuul worker node communication (osism/ansible-collection-services#634)
- Zuul: Increase default RSA key size to 4096 bits (osism/ansible-collection-services#634)
- Zuul: Rename CA directory from `demoCA` to `CA` (osism/ansible-collection-services#634)

### Removed
- Zuul: Remove worker node Docker container setup (osism/ansible-collection-services#634)
- Zuul: Remove gearman configuration (osism/ansible-collection-services#634)

### Dependencies
- ansible 5.4.0 → 5.5.0 (osism/ansible-collection-services#633)

## [v0.7.0] - 2022-03-15

### Added
- Add virtualbmc service with Docker Compose deployment (osism/ansible-collection-services#287)
- Add switch device roles (core, aggregation, access, spine, leaf) to netbox initializers
- Add configurable host and port arguments for OpenLDAP UDM and UMC services
- Add `docker_enforce_restart` and `docker_ignore_restart_groupname` options to docker role
- Add Homer role as a dashboard service replacement for Heimdall
- Add Homer configuration template with operations dashboard layout and theme customization
- Add Homer dashboard entries for ARA, NetBox, Ceph, Cockpit, Grafana, Horizon, Keycloak, Kibana, Netdata, Patchman, phpMyAdmin, Prometheus, and RabbitMQ
- Add Homer service restart handler when configuration or docker-compose files change
- Add Zuul role for single-node installation with docker-compose (osism/ansible-collection-services#249)
- Add missing Kolla modules (kolla_container_facts, kolla_docker, kolla_toolbox) and parameters to keycloak (osism/ansible-collection-services#328)
- Add Tailscale service role with package installation, service management, IP forwarding, and route advertisement
- Add generic-switch device role to netbox
- Add firewall-node device role to netbox
- Add netbox object permissions initialization via groups (osism/ansible-collection-services#343) (osism/ansible-collection-services#344)
- Add nexus role for Sonatype Nexus Repository Manager deployment
- Add celery worker support with flower monitoring and beat scheduler to manager (osism/ansible-collection-services#371, osism/ansible-collection-services#374)
- Add osism wrapper script to manager (osism/ansible-collection-services#372)
- Add AWX initialization tasks with database migration, admin user creation, and instance provisioning to manager (osism/ansible-collection-services#365)
- Add receptor service for AWX to manager (osism/ansible-collection-services#365, osism/ansible-collection-services#366)
- Add AWX supervisord configuration to manager (osism/ansible-collection-services#367)
- Add interface volume to inventory_reconciler service in manager (osism/ansible-collection-services#384)
- Add missing tags (control, compute, network) to netbox (osism/ansible-collection-services#363)
- Add ceph-resource tag to netbox (osism/ansible-collection-services#364)
- Add `patchman_update_force` parameter to force updates on every run (osism/ansible-collection-services#378)
- Add `patchman_client_update_force` parameter to patchman client (osism/ansible-collection-services#379)
- Add lldpd role for LLDP daemon management (osism/ansible-collection-services#397)
- Add initial FRR (Free Range Routing) role (osism/ansible-collection-services#411)
- Install docker-compose CLI plugin in docker role (osism/ansible-collection-services#390)
- Add plugin support with nextbox_ui_plugin and netbox_bgp plugins to netbox (osism/ansible-collection-services#407) (osism/ansible-collection-services#408)
- Add initialization tasks with script provisioning to nexus (osism/ansible-collection-services#400)
- Add ubuntu-docker proxy repository to nexus (osism/ansible-collection-services#401)
- Add vault initialization with key shares output to manager (osism/ansible-collection-services#403) (osism/ansible-collection-services#404)
- Add Vault dashboard entry and move Flower to management section in homer (osism/ansible-collection-services#409)
- Add pgrep healthchecks for celery beat and flower services to manager (osism/ansible-collection-services#406)
- Add Zun container service support for docker role with CNI configuration and containerd integration (osism/ansible-collection-services#418)
- Add Kolla address filter plugins (`kolla_address`, `put_address_in_context`) (osism/ansible-collection-services#419)
- Add Traefik role with docker-compose deployment, TLS certificate support, and external network configuration (osism/ansible-collection-services#422, osism/ansible-collection-services#425, osism/ansible-collection-services#426, osism/ansible-collection-services#429)
- Add Traefik integration for netbox with HTTP/HTTPS routing, path prefix support, and host-based routing (osism/ansible-collection-services#423, osism/ansible-collection-services#427, osism/ansible-collection-services#428)
- Add netbox_dns plugin to netbox plugins list (osism/ansible-collection-services#470)
- Add device roles (Access, Transfer, External, Mixed) and VLAN roles (External, Provisioning) to netbox (osism/ansible-collection-services#434)
- Add watchdog service to manager role (osism/ansible-collection-services#474)
- Add dynamic configuration for TLS certificates in traefik (osism/ansible-collection-services#476)
- Add default certificate support in traefik (osism/ansible-collection-services#475)
- Add Internal prefix/VLAN role to netbox initializers (osism/ansible-collection-services#477)
- Add managed-by tags (Ironic, Bifrost, OSISM) to netbox initializers (osism/ansible-collection-services#478) (osism/ansible-collection-services#479)
- Add Reserved and Parking lot VLAN/prefix roles to netbox initializers (osism/ansible-collection-services#480)
- Add custom field for device state in netbox (osism/ansible-collection-services#481)
- Add journald role for managing systemd-journald configuration (osism/ansible-collection-services#495)
- Add Traefik integration for nexus role with configurable path prefix and host-based routing (osism/ansible-collection-services#489)
- Add HTTP/HTTPS proxy support and admin password management for nexus (osism/ansible-collection-services#506)
- Add `nexus.env` file for nexus traefik environment configuration (osism/ansible-collection-services#492)
- Add osism-netbox service to manager role (osism/ansible-collection-services#498)
- Add configurable MTU for Docker container networks across all roles via `docker_network_mtu` (osism/ansible-collection-services#494)
- Add clamav role for installing and configuring the ClamAV daemon with support for Debian and RedHat (osism/ansible-collection-services#511)
- Add Traefik integration for phpmyadmin role (osism/ansible-collection-services#510)
- Add Traefik integration for ara-server in the manager role (osism/ansible-collection-services#503)
- Add molecule tests for clamav role (osism/ansible-collection-services#511)
- Add molecule tests for journald role (osism/ansible-collection-services#513)
- Add molecule tests for lldpd role (osism/ansible-collection-services#514)
- Add molecule test scenario for the frr role (osism/ansible-collection-services#515)
- Add osismclient container to manager service (osism/ansible-collection-services#518)
- Add `netdata_hostname` parameter for configurable netdata hostname (osism/ansible-collection-services#520)
- Add plugins configuration support for netbox (osism/ansible-collection-services#521)
- Add API service to manager (osism/ansible-collection-services#525)
- Add LDAP authentication configuration for netbox (osism/ansible-collection-services#530) (osism/ansible-collection-services#532)
- Add generic "view all objects" permission and viewers group for netbox (osism/ansible-collection-services#534)
- Add HTTP to HTTPS redirect middleware for traefik-enabled services (osism/ansible-collection-services#529)
- Add dnsdist role for DNS load balancing via Docker Compose (osism/ansible-collection-services#535)
- Add bird role for BGP routing with BFD support (osism/ansible-collection-services#541)
- Add state directory to manager role (osism/ansible-collection-services#543)
- Add state directory volume mount to manager ansible services (osism/ansible-collection-services#544)
- Add `configuration_template` custom field to netbox initializers (osism/ansible-collection-services#542)
- Add `deployment_playbook` custom field to netbox initializers (osism/ansible-collection-services#547)
- Add CA certificate bundle volume mounts to manager containers (osism/ansible-collection-services#552)
- Add `manager_environment_extra` parameter for custom environment variables in manager (osism/ansible-collection-services#554)
- Add TLS support for openstackclient container via CA certificates bind mount (osism/ansible-collection-services#556)
- Add network operating system tags (EOS, Junos, IOS, NX-OS, Onyx) to netbox initializers (osism/ansible-collection-services#562)
- Add cgit role for browsing Git repositories via web interface with Traefik integration support (osism/ansible-collection-services#578)
- Add `chrony_bindaddresses` parameter to bind Chrony to specific addresses (osism/ansible-collection-services#565)
- Add `deployment_type` and `device_type` custom fields to netbox device object (osism/ansible-collection-services#571)
- Add `deployment_parameters` custom field (JSON type) replacing `deployment_playbook` to netbox (osism/ansible-collection-services#572)
- Add `device_transition` custom field for tracking device state transitions to netbox (osism/ansible-collection-services#582)
- Add Ironic-related custom fields (`maintenance`, `provisioning_state`, `power_state`) to netbox (osism/ansible-collection-services#586)
- Add `introspection_state` custom field to netbox (osism/ansible-collection-services#590)
- Add OSISM API webhooks initializer for device and interface objects to netbox (osism/ansible-collection-services#579)
- Add Manager, Switch, Router, Firewall, Other, and Power device roles to netbox (osism/ansible-collection-services#585) (osism/ansible-collection-services#588)
- Add separate `netbox.env` file for NetBox configuration to manager (osism/ansible-collection-services#575)
- Add NetBox parameters to beat, watchdog, and osismclient services in manager (osism/ansible-collection-services#583)
- Add listener service for evaluating OpenStack notifications to manager (osism/ansible-collection-services#593)
- Add Traefik integration with customized Keycloak image support (osism/ansible-collection-services#568)
- Add netbox environment to the listener service in manager (osism/ansible-collection-services#595)
- Add openstack worker service to manager (osism/ansible-collection-services#598)
- Add conductor service with OpenStack access to manager (osism/ansible-collection-services#601)
- Add configurable branch for ansible-collection-services in manager update script (osism/ansible-collection-services#612)
- Add `network_interface_name` custom field for interfaces to netbox (osism/ansible-collection-services#597)
- Add `deployment_state` custom field for devices to netbox (osism/ansible-collection-services#599)
- Add `ironic_state` custom field for devices to netbox (osism/ansible-collection-services#602)
- Add `deployment_enabled` and `ironic_enabled` custom fields for devices to netbox (osism/ansible-collection-services#604)
- Add option to run homer behind traefik (osism/ansible-collection-services#610)
- Add option to run patchman behind traefik (osism/ansible-collection-services#629)
- Add Flower accessible via traefik in manager role (osism/ansible-collection-services#624)
- Add `netbox_extra` parameter to support custom parameters in netbox.env (osism/ansible-collection-services#628)
- Add restart notification handlers for netbox configuration and initializer changes (osism/ansible-collection-services#579)

### Changed
- Do not restart docker service on manager nodes by default (osism/ansible-collection-services#303)
- OpenLDAP: change default domain from `scs-organization.intranet` to `osism.local`
- OpenLDAP: use `password_hash` filter instead of pre-generated hash (osism/ansible-collection-services#274)
- OpenLDAP: use empty list by default for SERVICE_PROVIDERS (osism/ansible-collection-services#284)
- OpenLDAP: update default image names and tags (osism/ansible-collection-services#277) (osism/ansible-collection-services#285) (osism/ansible-collection-services#295)
- Netbox: use default postgres and redis image variable names instead of netbox-prefixed ones
- Netbox: use v3.0-ldap image tag (osism/ansible-collection-services#298)
- Netbox: rename device roles and tags with more descriptive names (osism/ansible-collection-services#299)
- Use postgres 14 across keycloak, manager, and netbox roles
- Update documentation URL from docs.osism.de to docs.osism.tech
- Update project URLs from osism.de to osism.tech (osism/ansible-collection-services#308)
- Netbox metrics are now configurable via `netbox_metrics` variable
- Minimum required Ansible version updated to >=2.11.0,<2.12.0
- Homer corporate identity colours to match OSISM branding
- Homer docker-compose volume changed from named volume to bind mount for configuration file
- Enable use of the MariaDB Galera cluster as database backend for keycloak (osism/ansible-collection-services#325)
- Downgrade minimum Ansible version requirement from 3.0.0 to 2.10.0 across all roles (osism/ansible-collection-services#327)
- Keycloak role refactored into separate config, service, and handler files with systemd service management
- OpenLDAP role refactored into separate config, service, and handler files with systemd service management
- Netbox default admin username changed from 'netbox' to 'admin' (osism/ansible-collection-services#342)
- Netbox removed CACHE_TIMEOUT and RELEASE_CHECK_TIMEOUT configuration parameters (osism/ansible-collection-services#335)
- Patchman client script synced with upstream (added Arch Linux support, hostname flag, zypper updates, improved boolean handling)
- Patchman postgres switched to tmpfs volume for faster repository imports (osism/ansible-collection-services#354)
- Relaxed minimum Ansible version requirement to >=2.10.0 in runtime.yml (osism/ansible-collection-services#357)
- Allow use of Ansible 2.11 (requires_ansible upper bound changed to <2.12.0)
- Manager: revise AWX service to use upstream `ansible/awx:19.4.0` image with receptor support (osism/ansible-collection-services#365)
- Manager: always enable Redis as it is required as broker for celery (osism/ansible-collection-services#370)
- Manager: improve vault configuration with persistent file storage and HCL config file (osism/ansible-collection-services#385, osism/ansible-collection-services#387)
- Manager: make vault usable independently of AWX (osism/ansible-collection-services#386)
- Manager: set interface volume to read-write in AWX service (osism/ansible-collection-services#368)
- Netbox: use OSISM's own netbox image `osism/netbox:v3.0.9-ldap` (osism/ansible-collection-services#369)
- Homer: replace Cockpit with Flower in dashboard (osism/ansible-collection-services#377)
- Add `changed_when: false` to all "Wait for apt lock" tasks across roles (osism/ansible-collection-services#381)
- Nexus role refactored into separate config, service, and initialize task files with configurable provision scripts (osism/ansible-collection-services#396) (osism/ansible-collection-services#413)
- Nexus: switch to osism/nexus image and add configuration directory with nexus.properties (osism/ansible-collection-services#396)
- Manager: improve celery support with healthchecks and environment variables (osism/ansible-collection-services#402)
- Manager: reduce default ARA workers from dynamic CPU-based calculation to fixed value of 5 (osism/ansible-collection-services#395)
- Docker: enable repository configuration by default (osism/ansible-collection-services#414)
- Docker Zun configuration refactored to merge hosts and options dynamically instead of modifying systemd ExecStart line (osism/ansible-collection-services#420)
- Use fully qualified collection names (FQCN) for filter plugins in docker role (osism/ansible-collection-services#420)
- Rework netbox device roles and VLAN roles to use simplified, shorter names (osism/ansible-collection-services#432)
- Traefik TLS certificates read from Ansible variables instead of files to support ansible-vault encryption (osism/ansible-collection-services#431)
- Traefik TLS cert and key consolidated into single dictionary (osism/ansible-collection-services#433)
- Manager osism-update-manager wrapper updated to include infrastructure environment for netbox and traefik playbooks (osism/ansible-collection-services#430)
- Use fully qualified collection names (FQCN) for Ansible modules across all roles (osism/ansible-collection-services#435, osism/ansible-collection-services#436, osism/ansible-collection-services#437, osism/ansible-collection-services#438, osism/ansible-collection-services#439, osism/ansible-collection-services#440, osism/ansible-collection-services#441, osism/ansible-collection-services#442, osism/ansible-collection-services#443, osism/ansible-collection-services#444, osism/ansible-collection-services#445, osism/ansible-collection-services#446, osism/ansible-collection-services#447, osism/ansible-collection-services#448, osism/ansible-collection-services#449, osism/ansible-collection-services#450, osism/ansible-collection-services#451, osism/ansible-collection-services#452, osism/ansible-collection-services#453, osism/ansible-collection-services#454, osism/ansible-collection-services#456, osism/ansible-collection-services#457, osism/ansible-collection-services#458, osism/ansible-collection-services#459, osism/ansible-collection-services#460, osism/ansible-collection-services#461, osism/ansible-collection-services#462, osism/ansible-collection-services#463, osism/ansible-collection-services#464, osism/ansible-collection-services#466, osism/ansible-collection-services#467, osism/ansible-collection-services#468, osism/ansible-collection-services#469)
- Rename manager role enable variables from `*_enable` to `enable_*` pattern (osism/ansible-collection-services#472)
- Disable all netbox plugins by default (osism/ansible-collection-services#483)
- Use fully qualified `ansible.builtin` task names in molecule test files (osism/ansible-collection-services#435)
- Nexus initialization now retries reading `/nexus-data/admin.password` instead of using `wait_for` (osism/ansible-collection-services#491)
- Nexus provisions scripts before setting admin password during initialization (osism/ansible-collection-services#508)
- Rename `enable_nexus_traefik` to `nexus_traefik` for consistency (osism/ansible-collection-services#508)
- Use `traefik_external_network_name` variable instead of hardcoded network name in netbox traefik labels (osism/ansible-collection-services#489)
- Enforce installation of osism.services collection in manager update wrapper (osism/ansible-collection-services#501)
- Manager netbox worker service uses `osism worker netbox` command (osism/ansible-collection-services#500)
- Nexus role overhauled with Groovy-based provisioning scripts, configurable repository definitions for Docker and APT proxies, API readiness checks, and Docker Bearer Token Realm support (osism/ansible-collection-services#509)
- Netbox role replaced gunicorn configuration with nginx-unit and improved traefik integration (osism/ansible-collection-services#512)
- Reorganized default variables across roles, moving `docker_network_mtu` to docker section and splitting list variables into defaults/extra pattern (osism/ansible-collection-services#516)
- Enable `netbox_plugin_osism` by default in netbox plugins (osism/ansible-collection-services#517)
- Improve docker OPA default policy with configurable allowed registries (osism/ansible-collection-services#523)
- Restrict GitHub Actions branch builds to main branch only (osism/ansible-collection-services#524)
- Add `osism` galaxy tag to all roles (osism/ansible-collection-services#526)
- Allow undefined LDAP environment variables in netbox configuration to prevent setting unused variables (osism/ansible-collection-services#536)
- Make netbox object permissions, groups, and users initializers configurable via dictionaries (osism/ansible-collection-services#538)
- Template netbox users initializer dictionary to properly evaluate variable keys (osism/ansible-collection-services#539)
- Remove `--reload` parameter from uvicorn command in manager API service (osism/ansible-collection-services#551)
- Rename `wrapper_scripts` to `manager_wrapper_scripts` for consistency (osism/ansible-collection-services#555)
- Use `ansible.builtin` and `ansible.posix` fully qualified task names in bird role (osism/ansible-collection-services#563)
- Update GitHub CI workflows to use Ansible 5.2.0 (osism/ansible-collection-services#540)
- Update manager update wrapper script to use Ansible 5.2.0 (osism/ansible-collection-services#550)
- Replace deprecated `ansible.builtin.include` with `ansible.builtin.include_tasks` across all roles (osism/ansible-collection-services#564)
- Change chrony `chrony_bind_local_interfaces_only` to set `port 0` instead of `bindcmdaddress` directives (osism/ansible-collection-services#565)
- Manager: merge `env_file` parameters for NetBox environment in docker-compose (osism/ansible-collection-services#576)
- Manager: use `osism service` command for flower, beat, watchdog, and api services (osism/ansible-collection-services#591) (osism/ansible-collection-services#592)
- Manager: switch listener from config file to environment file (`listener.env`) (osism/ansible-collection-services#594)
- Homer: add `target: "_blank"` to all links for consistent behavior (osism/ansible-collection-services#584)
- Rename netbox `provisioning_state` custom field to `provision_state` (osism/ansible-collection-services#596)
- Manager: resize manager network from /28 to /27 and relocate virtualbmc network (osism/ansible-collection-services#600)
- Manager: do not enable vault service by default (osism/ansible-collection-services#609)
- Manager: simplify ara-server traefik routing to use host-based rules (osism/ansible-collection-services#615)
- Update cephclient default version from octopus to pacific (osism/ansible-collection-services#608)
- Update openstackclient default version from victoria to xena (osism/ansible-collection-services#607)
- Add `no_log` to traefik certificate file copy tasks to prevent key leakage (osism/ansible-collection-services#570) (osism/ansible-collection-services#614)
- Traefik labels changed from path prefix routing to host-based routing (osism/ansible-collection-services#619)
- Set permanent option to true for traefik HTTPS redirections (osism/ansible-collection-services#613)
- Use `osism/renovate-config` for Renovate configuration
- Extend `requires_ansible` upper bound to `<2.13.0`
- Use legacy Keycloak image by default
- Set default `flower_traefik` to false (osism/ansible-collection-services#626)
- Improve the publish-collection workflow (osism/ansible-collection-services#632)
- Use `ansible-core` instead of `ansible` in publish-collection workflow

### Fixed
- OpenLDAP: fix UDM REST port configuration containing duplicate port number
- Virtualbmc: fix incorrect variable references and YAML indentation in templates
- Homer: fix broken URLs with missing `//` in URL schemes and swapped Ceph/Prometheus ports
- Manager: fix default branch name from `master` to `main` in osism-update-manager wrapper
- Keycloak and OpenLDAP service names corrected to use docker-compose@ prefix
- Keycloak template fixed to use `keycloak_galera_backend_enable` instead of `galera_backend_enable`
- Keycloak service handler now skips restart when service was just started (osism/ansible-collection-services#358)
- Homer light theme header text color mismatch (osism/ansible-collection-services#355)
- Nexus: fix volume name in docker-compose template
- Manager: fix receptor service command and container configuration (osism/ansible-collection-services#366)
- Manager: fix wrong flower parameter names in docker-compose template (osism/ansible-collection-services#373)
- Manager: fix vault backend configuration indentation (osism/ansible-collection-services#386)
- Manager: fix vault configuration - enable web UI, fix vault.hcl file permissions to 0644, listen on 0.0.0.0 (osism/ansible-collection-services#389)
- Docker: fix wrong parameter name for docker-compose plugin condition (osism/ansible-collection-services#391)
- Homer: fix internal Flower URL protocol from https to http (osism/ansible-collection-services#393)
- Nexus: fix copy & paste issue using wrong variable name in config task (osism/ansible-collection-services#398)
- Manager: fix vault_key_shares_path to use manager_secrets_directory (osism/ansible-collection-services#405)
- Homer: fix duplicate target key in config template (osism/ansible-collection-services#410)
- Manager: add netaddr pip package dependency for node_id usage in update wrapper (osism/ansible-collection-services#415)
- Fix incorrect parameter name `zun_cni_config_dir` to `docker_cni_config_dir` in docker zun config (osism/ansible-collection-services#420)
- Fix Jinja2 template syntax errors in netbox (`endif` instead of `endfor`, `bool` instead of `book`) (osism/ansible-collection-services#424)
- Fix yamllint issues in molecule config, keycloak, tailscale, manager, and virtualbmc roles (osism/ansible-collection-services#473)
- Fix custom field name and default value in netbox device state initializer (osism/ansible-collection-services#482)
- Fix double `.yml` extension in netbox custom_fields template filename (osism/ansible-collection-services#484)
- Journald role uses correct `systemd-journald` service name (osism/ansible-collection-services#497)
- Journald role uses `template` module instead of `copy` for configuration file (osism/ansible-collection-services#496)
- Fix YAML indentation in docker-compose network sections across multiple roles (osism/ansible-collection-services#494)
- Fix phpmyadmin traefik template using wrong middleware name for secure router without host (osism/ansible-collection-services#503)
- Fix typo in osismclient sleep command (osism/ansible-collection-services#519)
- Fix broken table formatting in README (osism/ansible-collection-services#533)
- Fix netbox LDAP template conditionals and typos in environment variable names (`AAUTH_` → `AUTH_`), add remote auth support to configuration.py (osism/ansible-collection-services#537)
- Remove `REQUESTS_CA_BUNDLE` from manager environment due to conflicts with self-signed Traefik certificates (osism/ansible-collection-services#553)
- Fix traefik service label definitions using wrong key (`traefik.http.routers` instead of `traefik.http.services`) (osism/ansible-collection-services#623)

### Removed
- Remove UCS role (osism/ansible-collection-services#276)
- OpenLDAP: remove unused `ldap/server/ip` variables from templates (osism/ansible-collection-services#278)
- Remove Zabbix and zabbix_agent roles
- Remove Heimdall role
- Homer: remove Cockpit from dashboard (osism/ansible-collection-services#377)
- Manager: remove `redis_enable` parameter (Redis is now always enabled) (osism/ansible-collection-services#370)
- Manager: remove `VAULT_LOCAL_CONFIG` from vault environment, replaced by vault.hcl file (osism/ansible-collection-services#388)
- Remove vendor-specific network OS tags (Arista EOS, Junos OS, Cisco IOS, Cisco NX-OS, Nvidia Onyx) from netbox (osism/ansible-collection-services#572)
- Manager: remove AWX integration including postgres, receptor, and all related configuration (osism/ansible-collection-services#605)
- Remove `deployment_parameters` custom field from netbox in favor of Config Context (osism/ansible-collection-services#603)
- Remove Tailscale role due to security concerns (osism/ansible-collection-services#622)
- Remove unused `keycloak_for_traefik_image` parameter (osism/ansible-collection-services#627)

### Dependencies
- molecule 3.3.4 → 3.6.1 (osism/ansible-collection-services#288, osism/ansible-collection-services#294, osism/ansible-collection-services#310, osism/ansible-collection-services#616)
- molecule-docker 0.3.4 → 1.1.0 (osism/ansible-collection-services#294, osism/ansible-collection-services#348)
- openpolicyagent/opa-docker-authz-v2 0.7 → 0.8 (osism/ansible-collection-services#522)
- actions/checkout v2 → v3 (osism/ansible-collection-services#617)
- actions/setup-python v2 → v3 (osism/ansible-collection-services#618)
- ansible 5.2.0 → 5.4.0 (osism/ansible-collection-services#621)

## [v0.5.0] - 2021-07-12

### Added
- New minikube role with systemd service support and configurable driver (osism/ansible-collection-services#175) (osism/ansible-collection-services#176) (osism/ansible-collection-services#178)
- New rundeck role with PostgreSQL backend and Docker Compose deployment (osism/ansible-collection-services#192) (osism/ansible-collection-services#193) (osism/ansible-collection-services#194) (osism/ansible-collection-services#195)
- New heimdall role with Docker Compose deployment (osism/ansible-collection-services#213) (osism/ansible-collection-services#214) (osism/ansible-collection-services#215) (osism/ansible-collection-services#216)
- Jenkins role with Docker Compose deployment, environment configuration, and persistent volume support (osism/ansible-collection-services#221) (osism/ansible-collection-services#223) (osism/ansible-collection-services#225) (osism/ansible-collection-services#226) (osism/ansible-collection-services#227)
- OpenLDAP role with Docker Compose deployment, TLS certificate management, UDM REST API, and UMC services (osism/ansible-collection-services#244) (osism/ansible-collection-services#252) (osism/ansible-collection-services#263)
- CentOS support for chrony role with OS-specific configuration paths and service names (osism/ansible-collection-services#245)
- CentOS support for rng role (osism/ansible-collection-services#246)
- CentOS support for hddtemp role with OS-specific configuration files and paths (osism/ansible-collection-services#248)
- Inventory-reconciler service to manager role (osism/ansible-collection-services#196) (osism/ansible-collection-services#197) (osism/ansible-collection-services#198)
- Healthcheck for netbox service using curl against metrics endpoint (osism/ansible-collection-services#219)
- Healthcheck for inventory-reconciler service using pgrep (osism/ansible-collection-services#220)
- Interface volume and configuration volume to manager docker-compose template (osism/ansible-collection-services#228) (osism/ansible-collection-services#229)
- Manager: `awx_group_queues` parameter (osism/ansible-collection-services#182)
- Manager: `netbox_enable` parameter to control NetBox integration (osism/ansible-collection-services#205)
- Manager: `ara_worker_class` parameter for ARA server (osism/ansible-collection-services#204)
- Manager: `docker_allow_restart` parameter to control Docker service restarts (osism/ansible-collection-services#203)
- Manager: `osism-validate` wrapper script (osism/ansible-collection-services#217)
- Manager: NetBox details to the inventory_reconciler container (osism/ansible-collection-services#210)
- Manager: missing `secrets.yml` to osism-update-manager script (osism/ansible-collection-services#211)
- Handler to restart manager service after docker-compose.yml changes (osism/ansible-collection-services#188)
- Restart handlers for adminer, netbox, and openstackclient roles when docker-compose files change
- Molecule test workflows for hddtemp, auditd, fail2ban, rsyslog, smartd, cockpit, and netdata roles
- Delegated molecule scenario for roles that don't use Docker

### Changed
- Manager ansible services made modular using a configurable list instead of hardcoded ceph-ansible and kolla-ansible entries (osism/ansible-collection-services#218)
- Manager AWX configuration synced with awx-operator defaults, including broadcast websocket support, receptor socket, and updated logging/settings configuration (osism/ansible-collection-services#230) (osism/ansible-collection-services#231)
- Manager AWX settings moved from `settings.py` to configurable defaults (osism/ansible-collection-services#180) (osism/ansible-collection-services#181)
- Consolidated AWX into a single container by removing the separate awx-web container (osism/ansible-collection-services#184) (osism/ansible-collection-services#185)
- Changed AWX default UUIDs from all-zeros to non-zero values (osism/ansible-collection-services#183)
- Manager: use inventory-reconciler volume for AWX instead of dedicated awx_inventory volume (osism/ansible-collection-services#199)
- Manager: Ansible services now depend on inventory_reconciler service (osism/ansible-collection-services#200)
- Manager: ARA default worker class changed from eventlet to sync (osism/ansible-collection-services#234)
- Manager: mariadb.env file made optional, only generated when database type is mysql (osism/ansible-collection-services#243)
- Manager: allow Netbox integration without requiring AWX integration
- Docker: ensure `docker_registry_username` is cast to string before length check (osism/ansible-collection-services#201)
- Docker role fails early if `ansible_os_family` is not Debian (osism/ansible-collection-services#247)
- Cockpit login title changed from "Open Source Infrastructure & Service Manager" to "OSISM" (osism/ansible-collection-services#239)
- Apt tasks refactored to pass package lists directly instead of using loops (osism/ansible-collection-services#233)
- Remove `become: true` from all "Wait for apt lock" tasks across multiple roles (osism/ansible-collection-services#207)
- Patchman PostgreSQL image updated from 12-alpine to 13-alpine (osism/ansible-collection-services#237)
- UDM REST image path updated to `univention-upx-container-udm-rest-udm` (osism/ansible-collection-services#263)
- Company name from "Betacloud Solutions GmbH" to "OSISM GmbH" in all role metadata (osism/ansible-collection-services#250)
- Homepage and contact email domain from osism.de to osism.tech (osism/ansible-collection-services#251)

### Deprecated
- Zabbix and zabbix_agent roles with deprecation notice (override with `ignore_deprecations` parameter)

### Fixed
- Netbox service name to use `docker-compose@netbox` format (osism/ansible-collection-services#179)
- Missing quotes in CI workflow files for chrony and rng roles (osism/ansible-collection-services#187)
- Patchman memcached image variable names to use `patchman_memcached_` prefix avoiding conflicts (osism/ansible-collection-services#212)
- Required Ansible version constraint corrected from `>=3.0.0,<4.0.0` to `>=2.10.0,<2.11.0` (osism/ansible-collection-services#235)
- Missing `restart: unless-stopped` settings for UDM REST, UMC server, UMC web, and UMC gateway containers in OpenLDAP role (osism/ansible-collection-services#265)
- Molecule test jobs restructured with templated workflows and configurable scenarios
- Galaxy metadata "authors list must not be greater than 64 characters" error

### Removed
- osquery role (osism/ansible-collection-services#189)
- pulp role (osism/ansible-collection-services#190)
- bird role (osism/ansible-collection-services#202)
- "PR Labeler" GitHub workflow (osism/ansible-collection-services#206)

### Dependencies
- awxclient 16.0.0 → 19.0.0 (osism/ansible-collection-services#174)
- docker 5:20.10.5 → 5:20.10.6 (osism/ansible-collection-services#191)
- molecule 3.3.0 → 3.3.4 (osism/ansible-collection-services#232) (osism/ansible-collection-services#236) (osism/ansible-collection-services#240) (osism/ansible-collection-services#241)
- molecule-docker 0.2.4 → 0.3.4 (osism/ansible-collection-services#238)

## [v0.4.0] - 2021-04-09

### Added
- Netbox role with Docker Compose deployment, PostgreSQL, Redis, initializers, and startup scripts (osism/ansible-collection-services#167)

### Changed
- Manager role now uses `netbox_api_url` and `netbox_api_token` variables for external NetBox integration instead of managing a local NetBox instance (osism/ansible-collection-services#171)
- Manager role now uses netbox image from quay.io registry instead of service registry (osism/ansible-collection-services#158)
- Docker default version updated from 20.10.0 to 20.10.5 (osism/ansible-collection-services#163)
- Require Ansible >= 3.0.0 and drop Ubuntu Bionic support across all roles (osism/ansible-collection-services#168)

### Fixed
- Netbox role: add missing Redis service, fix initializer paths, fix postgres password variable, add netbox_userid and netbox_initializers defaults (osism/ansible-collection-services#169)
- Netbox role: add missing `services:` key in docker-compose template, remove nginx proxy in favor of direct netbox port exposure, fix worker entrypoint path, correct network subnet (osism/ansible-collection-services#170)

### Removed
- Embedded NetBox service from manager role (moved to a separate role) (osism/ansible-collection-services#171)

### Dependencies
- molecule 3.2.2 → 3.3.0 (osism/ansible-collection-services#160, osism/ansible-collection-services#162, osism/ansible-collection-services#164)

## [v0.3.0] - 2021-01-17

### Added
- New `fail2ban` role for intrusion prevention (osism/ansible-collection-services#117)
- New `bird` role for BGP routing with BFD support (osism/ansible-collection-services#124)
- bird: add configurable BFD and BGP timing parameters (osism/ansible-collection-services#125)
- scan_services module for collecting facts about system services (osism/ansible-collection-services#138)
- manager: add configurable `ara_workers` parameter for ARA server (osism/ansible-collection-services#114)
- manager: add configurable ARA database backend with option to disable MariaDB dependency (osism/ansible-collection-services#139)
- netdata: add configurable `netdata_memory_mode` parameter (osism/ansible-collection-services#120)
- netdata: add configurable `netdata_update_every` parameter (osism/ansible-collection-services#121)
- netdata: add configurable `netdata_default_history` parameter (osism/ansible-collection-services#123)
- netdata: add configurable `netdata_sys_vm_max_map_count` sysctl parameter for server nodes (osism/ansible-collection-services#126)
- rsyslog: add `rsyslog_fluentd` toggle to enable/disable fluentd forwarding (osism/ansible-collection-services#113)
- zabbix: add configurable `zabbix_server_name` parameter (osism/ansible-collection-services#128)
- zabbix_agent: allow zabbix server network on zabbix server nodes (osism/ansible-collection-services#136)

### Changed
- auditd: update neo23x0 audit rules to latest upstream version (osism/ansible-collection-services#110)
- auditd: disable monitoring of `/usr/bin/dockerd` to reduce log volume (osism/ansible-collection-services#111)
- auditd: disable monitoring of `/var/lib/docker` to reduce log volume (osism/ansible-collection-services#112)
- rsyslog: rename fluentd parameters to use `rsyslog_fluentd_` prefix (osism/ansible-collection-services#113)
- netdata: remove `netdata_action` parameter and simplify task structure (osism/ansible-collection-services#118)
- netdata: create `/var/lib/netdata/cloud.d` directory before copying cloud.conf (osism/ansible-collection-services#119)
- netdata: disable access logs on server (osism/ansible-collection-services#122)
- zabbix: update default image tags to alpine-5.2-latest and switch web frontend from Apache to Nginx (osism/ansible-collection-services#128)
- zabbix: switch database backend from MariaDB to PostgreSQL (osism/ansible-collection-services#129)
- zabbix_agent: clean up old zabbix-agent package before installing new version (osism/ansible-collection-services#130, osism/ansible-collection-services#131)
- zabbix_agent: start/enable service after config tasks instead of during install (osism/ansible-collection-services#132)
- zabbix_agent: clean up zabbix_agent2 configuration template by removing verbose comments and setting sensible defaults (osism/ansible-collection-services#133)
- zabbix_agent: upgrade default version from 5.0 to 5.2 (osism/ansible-collection-services#143)
- zabbix_agent: switch repository management from `apt_repository` to `copy` to handle version changes cleanly (osism/ansible-collection-services#144)
- zabbix_agent: check if old service exists before stopping it during cleanup (osism/ansible-collection-services#137)
- zabbix_agent, netdata, falco, and osquery packages now install latest version and restart service after upgrade (osism/ansible-collection-services#145, osism/ansible-collection-services#146, osism/ansible-collection-services#147, osism/ansible-collection-services#148, osism/ansible-collection-services#149, osism/ansible-collection-services#150, osism/ansible-collection-services#151)
- Migrated adminer, cephclient, manager, openstackclient, phpmyadmin, zabbix, and patchman roles from docker_compose module/command to docker-compose systemd service (osism/ansible-collection-services#152, osism/ansible-collection-services#153, osism/ansible-collection-services#154, osism/ansible-collection-services#155)

### Fixed
- Fixed typo "Rmove" to "Remove" in zabbix_agent cleanup task (osism/ansible-collection-services#137)
- Fixed missing "service" suffix in zabbix_agent handler name (osism/ansible-collection-services#149)
- Fixed wrong docker-compose service names for manager and patchman roles (osism/ansible-collection-services#156)

### Removed
- Removed old zabbix_agentd.conf.d directory during zabbix_agent cleanup (osism/ansible-collection-services#134)

### Dependencies
- actions/checkout v1 → v2 (osism/ansible-collection-services#115)
- actions/setup-python v1 → v2 (osism/ansible-collection-services#116)
- molecule 3.2.1 → 3.2.2 (osism/ansible-collection-services#135)

## [v0.2.0] - 2020-12-28

### Added
- Per-role docker registry variables for adminer, cephclient, openstackclient, patchman, phpmyadmin, pulp, ucs, zabbix, and openstack_health_monitor (osism/ansible-collection-services#83)
- Per-service docker registry variables for manager role (ara_server, awx, mariadb, netbox, nginx, postgres, redis, vault) (osism/ansible-collection-services#87)
- CEPH variable to AWX environment file (osism/ansible-collection-services#88)
- AWX mail address configuration (osism/ansible-collection-services#91)
- AWX inventory volume (osism/ansible-collection-services#92)
- AWX client service and configuration (osism/ansible-collection-services#93)
- osism-awx wrapper script (osism/ansible-collection-services#96)
- osism-state wrapper script (osism/ansible-collection-services#98)
- Configurable AWX settings via `awx_configuration` variable (osism/ansible-collection-services#102)
- deploy_private_key support for manager role (osism/ansible-collection-services#105)
- Wait for apt lock before package installations to prevent concurrent dpkg access issues (osism/ansible-collection-services#106)

### Changed
- Enforce quay.io registry for openstackclient and cephclient images (osism/ansible-collection-services#89)
- Use `sleep infinity` instead of shell loop in openstackclient container (osism/ansible-collection-services#90)
- Use quay.io registry for patchman image (osism/ansible-collection-services#101)
- Update default ara-server tag from 1.5.3 to 1.5.4 (osism/ansible-collection-services#104)
- Move `become: true` to top of tasks in manager role (osism/ansible-collection-services#96)
- Improved apt lock wait to also check `lock-frontend` and run with `become: true` (osism/ansible-collection-services#107)
- Refactored installation tasks into separate `install-Debian.yml` files for auditd, chrony, cockpit, hddtemp, patchman_client, rng, rsyslog, and smartd roles (osism/ansible-collection-services#108)
- Replaced generic `package` module with `apt` module in chrony, cockpit, docker, manager, and patchman_client roles (osism/ansible-collection-services#106)

### Fixed
- YAML lint issues across multiple roles (truthy values, update_cache, enabled) (osism/ansible-collection-services#86)
- AWX client image tag variable reference (osism/ansible-collection-services#94)
- Missing awxclient.env file in AWX client container (osism/ansible-collection-services#95)
- Trailing comma in AWX settings template (osism/ansible-collection-services#103)
- Auditd no longer removes osas-auditd-rhel7.rules file (osism/ansible-collection-services#97)

### Removed
- Gilt configuration files (.information.yml, gilt.yml) (osism/ansible-collection-services#84)
- Content-Security-Policy headers from AWX nginx configuration (osism/ansible-collection-services#100)

### Dependencies
- molecule 3.2.0 → 3.2.1 (osism/ansible-collection-services#85)

## [v0.1.0] - 2020-12-19

### Added
- Initial project structure with Ansible collection `osism.services`, including CI workflows, molecule test infrastructure, and Apache 2.0 license
- Adminer role for database management UI via Docker Compose (osism/ansible-collection-services#24)
- Auditd role with CI workflow, molecule tests, and Neo23x0 audit rules (osism/ansible-collection-services#5)
- Cephclient role with container and package install support, wrapper scripts, and bash completion (osism/ansible-collection-services#23)
- Chrony role for NTP time synchronization (osism/ansible-collection-services#19)
- Cockpit role with client and server support, including systemd socket configuration and machine discovery (osism/ansible-collection-services#9)
- Docker role imported from ansible-docker with support for storage configuration, Kata runtime, and Open Policy Agent policies (osism/ansible-collection-services#55)
- Falco role with package installation, repository configuration, service management, and kernel module loading/persistence (osism/ansible-collection-services#2)
- Hddtemp, rng, and smartd roles migrated from osism.commons (osism/ansible-collection-services#28)
- Keycloak role with PostgreSQL backend and Docker Compose deployment (osism/ansible-collection-services#30)
- Manager role (`osism.services.manager`) with support for ARA, AWX, Netbox, Vault, Redis, and PostgreSQL services (osism/ansible-collection-services#56)
- Molecule test framework with Docker-based testing support (osism/ansible-collection-services#73)
- Netdata role with client/server streaming support and package-based installation (osism/ansible-collection-services#22)
- OpenStack client role with container and package install support, wrapper scripts, and bash completion (osism/ansible-collection-services#23)
- OpenStack Health Monitor role (`osism.services.openstack_health_monitor`) with container-based deployment and cronjob support (osism/ansible-collection-services#60)
- osquery role with Debian package installation, repository configuration, and service management (osism/ansible-collection-services#3)
- Patchman server and patchman client roles for patch management (osism/ansible-collection-services#20)
- phpMyAdmin role with Docker Compose deployment (osism/ansible-collection-services#10)
- Pulp role for content management via Docker Compose (osism/ansible-collection-services#25)
- rsyslog role with configuration management and fluentd forwarding support (osism/ansible-collection-services#4)
- UCS (Univention Corporate Server) role via Docker Compose (osism/ansible-collection-services#26)
- Zabbix server role with docker-compose deployment (server, web, MariaDB) (osism/ansible-collection-services#21)
- Zabbix agent role with package-based installation, repository configuration, and extension support (osism/ansible-collection-services#21)
- Configurable `zabbix_cachesize` and `zabbix_startpollers` parameters for the Zabbix role (osism/ansible-collection-services#58)
- Configurable paths for `clouds.yml` and `secure.yml` in openstack_health_monitor role (osism/ansible-collection-services#61)
- Configurable `OS_CLOUD` setting in openstack_health_monitor role (osism/ansible-collection-services#61)
- Persistent data volume for openstack_health_monitor container (osism/ansible-collection-services#62)
- Configurable `ADDJHVOLSIZE`, `ADDVMVOLSIZE`, and `DATADIR` parameters in openstack_health_monitor role (osism/ansible-collection-services#62)
- Configurable arguments parameter for openstack_health_monitor cron job (osism/ansible-collection-services#62)
- Top-level gilt.yml file for generic file synchronization (osism/ansible-collection-services#17)
- GitHub Actions workflows for testing the rng and chrony roles (osism/ansible-collection-services#74, osism/ansible-collection-services#75)

### Changed
- Simplify molecule prepare playbooks to only update package cache instead of full upgrade and reboot (osism/ansible-collection-services#6)
- Moved `become: true` to the top of tasks across all roles for consistent task formatting (osism/ansible-collection-services#18)
- Removed ansible-lint from molecule requirements as linting was moved to GitHub workflows (osism/ansible-collection-services#27)
- Keycloak: add PROXY_ADDRESS_FORWARDING=true to environment configuration (osism/ansible-collection-services#43)
- Manager role now uses quay.io as default registry for ansible images instead of docker.io (osism/ansible-collection-services#59)
- Manager role updated default kolla-ansible tag from `train` to `victoria` (osism/ansible-collection-services#59)
- Manager role updated default ara-server tag from `1.4.0` to `1.5.3` (osism/ansible-collection-services#59)
- Manager role updated default postgres tag from `12-alpine` to `13-alpine` (osism/ansible-collection-services#59)
- Manager update script now uses Ansible 2.10, `--no-cache-dir` for pip, and installs via `ansible-galaxy collection` instead of role install (osism/ansible-collection-services#78)
- Use role-scoped `openstack_health_monitor_docker_registry` instead of global `docker_registry` variable (osism/ansible-collection-services#62)
- Use `entrypoint` instead of `command` for crond in openstack_health_monitor container (osism/ansible-collection-services#62)
- Adjust default cronjob schedule for openstack_health_monitor to run every 10 minutes (osism/ansible-collection-services#62)
- Rename openstack_health_monitor volume from `logs` to `data` (osism/ansible-collection-services#63)
- Replace `yes`/`no` with `true`/`false` for boolean values in docker, cockpit, and netdata roles (osism/ansible-collection-services#64, osism/ansible-collection-services#65, osism/ansible-collection-services#66)
- Rename and clean up GitHub Actions workflows, add yamllint rules (osism/ansible-collection-services#67)
- Default Docker version updated from 19.03.12 to 20.10.0 (osism/ansible-collection-services#69, osism/ansible-collection-services#79)
- Default docker registry switched from `index.docker.io` to `quay.io` for cephclient and openstackclient (osism/ansible-collection-services#80)
- OpenStack client version updated from ussuri to victoria (osism/ansible-collection-services#80)
- ARA server image now uses `docker_registry_ansible` instead of `docker_registry_service` (osism/ansible-collection-services#80)
- Publish collection workflow enabled and reworked to trigger on version tags with a dedicated playbook (osism/ansible-collection-services#82)
- Collection version set to 0.1.0 (osism/ansible-collection-services#82)
- Updated README with test status badge column and missing roles (osism/ansible-collection-services#37, osism/ansible-collection-services#57, osism/ansible-collection-services#73)
- Disable test workflows due to timeout issues (osism/ansible-collection-services#15)

### Fixed
- Fix ansible-lint E208 warnings by adding missing file mode parameters to copy and template tasks (osism/ansible-collection-services#16)
- Keycloak: fix container port mapping from 8000 to 8080 (osism/ansible-collection-services#31)
- Add missing `user` parameter to openstack_health_monitor cron job (osism/ansible-collection-services#62)

### Removed
- Sysdig role, moved to osism.commons (osism/ansible-collection-services#8)
- Ansible lint GitHub Actions workflow (osism/ansible-collection-services#67)
- Old molecule test configurations for auditd, cockpit, falco, osquery, and phpmyadmin roles (osism/ansible-collection-services#68)
- Encrypted clouds.yml.gpg file and related .gitignore entries (osism/ansible-collection-services#71)
- Legacy `.information.yml`, `README.md`, and `gilt.yml` files from multiple roles (osism/ansible-collection-services#72)
- Disabled GitHub workflow files for auditd, cockpit, falco, osquery, phpmyadmin, and rsyslog tests (osism/ansible-collection-services#76)

### Dependencies
- molecule 3.0.6 → 3.2.0 (osism/ansible-collection-services#13, osism/ansible-collection-services#29, osism/ansible-collection-services#44, osism/ansible-collection-services#45, osism/ansible-collection-services#46, osism/ansible-collection-services#47, osism/ansible-collection-services#48, osism/ansible-collection-services#54)
- molecule-openstack 0.1 → 0.2 (osism/ansible-collection-services#50)
- openstacksdk 0.48.0 → 0.52.0 (osism/ansible-collection-services#35, osism/ansible-collection-services#36, osism/ansible-collection-services#51, osism/ansible-collection-services#53)
- paramiko 2.7.1 → 2.7.2 (osism/ansible-collection-services#32)
- testinfra 5.2.2 → 6.0.0 (osism/ansible-collection-services#33, osism/ansible-collection-services#34, osism/ansible-collection-services#52)

