# Ansible collection osism.services

Documentation: https://osism.github.io/docs/guides/configuration-guides/services/

The following Ansible roles are included in this collection.

| Rolename                 | Molecule Unit Test                                                                  | Ubuntu | CentOS |
|--------------------------|-------------------------------------------------------------------------------------|--------|--------|
| adminer                  | [adminer.py](molecule/delegated/tests/adminer.py)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| auditd                   | [auditd.py](molecule/delegated/tests/auditd.py)                                     |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| bird                     | [bird](molecule/delegated/tests/bird)                                               |   :ballot_box_with_check:  |   :negative_squared_cross_mark:  |
| cephclient               | [cephclient](molecule/delegated/tests/cephclient)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| cgit                     | [cgit.py](molecule/delegated/tests/cgit.py)                                         |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| chrony                   | [chrony](molecule/delegated/tests/chrony)                                           |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| clamav                   | [clamav](molecule/delegated/tests/clamav)                                           |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| cloudnative_pg           | N/A                                                                                 |   N/A  |   N/A  |
| containerd               | [containerd](molecule/delegated/tests/containerd)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| dnsdist                  | [dnsdist.py](molecule/delegated/tests/dnsdist.py)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| docker                   | [docker](molecule/delegated/tests/docker)                                           |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| fail2ban                 | [fail2ban.py](molecule/delegated/tests/fail2ban.py)                                 |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| falco                    | [falco](molecule/delegated/tests/falco)                                             |   :ballot_box_with_check:  |   :negative_squared_cross_mark:  |
| frr                      | [frr.py](molecule/delegated/tests/frr.py)                                           |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| hddtemp                  | [hddtemp](molecule/delegated/tests/hddtemp/)                                        |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| homer                    | [homer.py](molecule/delegated/tests/homer.py)                                       |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| journald                 | [journald.py](molecule/delegated/tests/journald.py)                                 |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| keycloak                 | N/A                                                                                 |   N/A  |   N/A  |
| lldpd                    | [lldpd.py](molecule/delegated/tests/lldpd.py)                                       |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| manager                  | [manager.py](molecule/delegated/tests/manager.py)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| metering                 | [metering.py](molecule/delegated/tests/metering.py)                                 |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| netbox                   | [netbox.py](molecule/delegated/tests/netbox.py)                                     |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| netdata                  | [netdata](molecule/delegated/tests/netdata)                                         |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| nexus                    | [nexus.py](molecule/delegated/tests/nexus.py)                                       |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| openstack_health_monitor | [openstack_health_monitor.py](molecule/delegated/tests/openstack_health_monitor.py) |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| openstackclient          | [openstackclient](molecule/delegated/tests/openstackclient)                         |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| osquery                  | [osquery](molecule/delegated/tests/osquery)                                         |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| phpmyadmin               | [phpmyadmin.py](molecule/delegated/tests/phpmyadmin.py)                             |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| rng                      | [rng.py](molecule/delegated/tests/rng.py)                                           |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| rook_operator            | N/A                                                                                 |   N/A  |   N/A  |
| rsyslog                  | [rsyslog.py](molecule/delegated/tests/rsyslog.py)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| scaphandre               | [scaphandre.py](molecule/delegated/tests/scaphandre.py)                             |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| smartd                   | [smartd.py](molecule/delegated/tests/smartd.py)                                     |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| squid                    | [squid.py](molecule/delegated/tests/squid.py)                                       |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| tang                     | N/A                                                                                 |   N/A  |   N/A  |
| thanos_sidecar           | [thanos_sidecar.py](molecule/delegated/tests/thanos_sidecar.py)                     |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| traefik                  | [traefik.py](molecule/delegated/tests/traefik.py)                                   |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| tuned                    | [tuned.py](molecule/delegated/tests/tuned.py)                                       |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| virtualbmc               | [virtualbmc.py](molecule/delegated/tests/virtualbmc.py)                             |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| wireguard                | [wireguard.py](molecule/delegated/tests/wireguard.py)                               |   :ballot_box_with_check:  |   :ballot_box_with_check:  |
| zuul                     | N/A                                                                                 |   N/A  |   N/A  |
