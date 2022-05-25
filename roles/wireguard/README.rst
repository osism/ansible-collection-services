An ansible role for installation and configuration wireguard.

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user that will own the client config.

.. zuul:rolevar:: operator_group
   :default: operator_user

The group that will own the client config.

.. zuul:rolevar:: wireguard_service_name
   :default: wg-quick@wg0.service

The name for the wireguard service.

.. zuul:rolevar:: wireguard_mtu
   :default: 1360

Maximum Transfer Unit for wireguard. Please look which MTU fits for your system.

.. zuul:rolevar:: wireguard_client_address
   :default: 192.168.48.4/24

The client address in the VPN.

.. zuul:rolevar:: wireguard_allowed_client_ips
   :default: 192.168.16.0/20, 192.168.48.0/20, 192.168.96.0/20, 192.168.112.0/20

Addresses which should be routed through the VPN.

.. zuul:rolevar:: wireguard_server_address
   :default: 192.168.48.5/20

The internal VPN server address.

.. zuul:rolevar:: wireguard_listen_port
   :default: 51820

The port on which the wireguard server is listening.

.. zuul:rolevar:: wireguard_allowed_server_ips
   :default: 192.168.48.0/20

The range of allowed client IP addresses.

.. zuul:rolevar:: wireguard_server_public_address
   :default: WIREGUARD_PUBLIC_IP_ADDRESS

The public IP address of the wireguard server.
