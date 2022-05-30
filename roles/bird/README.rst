Role for setting up Bird. Bird is an dynamical IP routing daemon.

**Role Variables**

.. zuul:rolevar:: bird_package_name
   :default: bird

The package which is required for Bird.

.. zuul:rolevar:: bird_service_name
   :default: bird

Service name for Bird.

.. zuul:rolevar:: bird_sysctl

.. code-block:: yaml

   - name: net.ipv4.ip_forward
     value: 1
   - name: net.ipv4.conf.all.send_redirects
     value: 0
   - name: net.ipv4.conf.all.accept_redirects
     value: 0
   - name: net.ipv4.fib_multipath_hash_policy
     value: 1
   - name: net.ipv4.conf.default.ignore_routes_with_linkdown
     value: 1
   - name: net.ipv4.conf.all.rp_filter
     value: 2

Sysctl parameters for Bird. The required kernel parameters for Bird.

.. zuul:rolevar:: bird_cidr
   :default: 10.12.0.0/16

The network for the Bird.

.. zuul:rolevar:: bird_leaf_interfaces

Management interface which communicate with the BFD
(Bidirectional Forwarding Detection).

.. zuul:rolevar:: bird_neighbor_as
   :default: 65000

The private number for the Autonom System. This declares the number for
the BGP-network.

.. zuul:rolevar:: bird_keepalive_time
   :default: 1

Keepalive time for BGP (Border Gateway Protocol).

.. zuul:rolevar:: bird_leaf_bfd
   :default: no

Disables the BGP protocol.

.. zuul:rolevar:: bird_leaf_hold_time
   :default: 3

Time which the BGP will wait for to declare the neighborship as down.

.. zuul:rolevar:: bird_bfd_idle_tx_interval
   :default: 200

Optimization for the BFD protocol.

.. zuul:rolevar:: bird_bfd_min_rx_interval
   :default: 20

Optimization for the BFD protocol.

.. zuul:rolevar:: bird_bfd_min_tx_interval
   :default: 20

Optimization for the BFD protocol.

.. zuul:rolevar:: bird_bfd_multiplier
   :default: 3

Sets the amount of not received hello packets by a neighbor.
The amount defines the threshhold for an interface to be declared down.
