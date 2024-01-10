# Ansible collection osism.services

Documentation: https://osism.github.io/docs/guides/configuration-guides/services/

The following Ansible roles are included in this collection.

| Rolename                 | Molecule Unit Test                                                                                                                       |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| adminer                  | [adminer.py](molecule/delegated/tests/adminer.py)                                                                                        |
| auditd                   | [auditd.py](molecule/delegated/tests/auditd.py)                                                                                          |
| bird                     | [bird.py](molecule/delegated/tests/bird.py)                                                                                              |
| cephclient               | [container.py](molecule/delegated/tests/cephclient/container.py), [package.py](molecule/delegated/tests/cephclient/package.py)           |
| cgit                     | [cgit.py](molecule/delegated/tests/cgit.py)                                                                                              |
| chrony                   | [main.py](molecule/delegated/tests/chrony/main.py), [debian.py](molecule/delegated/tests/chrony/debian.py)                               |
| clamav                   | [clamav.py](molecule/delegated/tests/clamav.py)                                                                                          |
| containerd               | [containerd.py](molecule/delegated/tests/containerd.py)                                                                                  |
| dnsdist                  | [dnsdist.py](molecule/delegated/tests/dnsdist.py)                                                                                        |
| docker                   | [docker.py](molecule/delegated/tests/docker.py)                                                                                          |
| fail2ban                 | [fail2ban.py](molecule/delegated/tests/fail2ban.py)                                                                                      |
| falco                    | [falco.py](molecule/delegated/tests/falco.py)                                                                                            |
| frr                      | [frr.py](molecule/delegated/tests/frr.py)                                                                                                |
| hddtemp                  | [debian.py](molecule/delegated/tests/hddtemp/debian.py), [redhat.py](molecule/delegated/tests/hddtemp/redhat.py)                         |
| homer                    | [homer.py](molecule/delegated/tests/homer.py)                                                                                            |
| journald                 | [journald.py](molecule/delegated/tests/journald.py)                                                                                      |
| keycloak                 | [keycloak.py](molecule/delegated/tests/keycloak.py)                                                                                      |
| lldpd                    | [lldpd.py](molecule/delegated/tests/lldpd.py)                                                                                            |
| manager                  | [manager.py](molecule/delegated/tests/manager.py)                                                                                        |
| metering                 | [metering.py](molecule/delegated/tests/metering.py)                                                                                      |
| netbox                   | [netbox.py](molecule/delegated/tests/netbox.py)                                                                                          |
| netdata                  | [netdata.py](molecule/delegated/tests/netdata.py)                                                                                        |
| nexus                    | [nexus.py](molecule/delegated/tests/nexus.py)                                                                                            |
| openldap                 | [openldap.py](molecule/delegated/tests/openldap.py)                                                                                      |
| openstack_health_monitor | [openstack_health_monitor.py](molecule/delegated/tests/openstack_health_monitor.py)                                                      |
| openstackclient          | [container.py](molecule/delegated/tests/openstackclient/container.py), [package.py](molecule/delegated/tests/openstackclient/package.py) |
| osquery                  | [osquery.py](molecule/delegated/tests/osquery.py)                                                                                        |
| phpmyadmin               | [phpmyadmin.py](molecule/delegated/tests/phpmyadmin.py)                                                                                  |
| rng                      | [rng.py](molecule/delegated/tests/rng.py)                                                                                                |
| rsyslog                  | [rsyslog.py](molecule/delegated/tests/rsyslog.py)                                                                                        |
| scaphandre               | [scaphandre.py](molecule/delegated/tests/scaphandre.py)                                                                                  |
| smartd                   | [smartd.py](molecule/delegated/tests/smartd.py)                                                                                          |
| squid                    | [squid.py](molecule/delegated/tests/squid.py)                                                                                            |
| tang                     |                                                                                                                                          |
| thanos_sidecar           | [thanos_sidecar.py](molecule/delegated/tests/thanos_sidecar.py)                                                                          |
| traefik                  | [traefik.py](molecule/delegated/tests/traefik.py)                                                                                        |
| tuned                    | [tuned.py](molecule/delegated/tests/tuned.py)                                                                                            |
| virtualbmc               | [virtualbmc.py](molecule/delegated/tests/virtualbmc.py)                                                                                  |
| wireguard                | [wireguard.py](molecule/delegated/tests/wireguard.py)                                                                                    |
| zuul                     |                                                                                                                                          |
