An ansible role for installation and configuration of wireguard. Sets
up VPN service for a set of local users.

**Role Variables**

.. zuul:rolevar:: wireguard_users

List of users that will be configured for access. Each item is a dict with keys::

  - name: Name of the user
  - key: The public wireguard key of the user
  - ip: The IP address assigned to the user

.. zuul:rolevar:: wireguard_mtu
   :default: 1360

Maximum Transfer Unit for wireguard. The default should allow connections to work
through most consumer and cloud networks.

.. zuul:rolevar:: wireguard_server_address
   :default: 192.168.48.254/24

The VPN server address.

.. zuul:rolevar:: wireguard_listen_port
   :default: 51820

The port on which the wireguard server is listening.

.. zuul:rolevar:: wireguard_server_public_address
   :default: WIREGUARD_PUBLIC_IP_ADDRESS

The public IP address of the wireguard server that clients can connect to.

.. zuul:rolevar:: wireguard_create_client_config
   :default: false

Whether to create client config files. Assumes the user names to be local
on the server and their home directory to be `/home/user.name`.
