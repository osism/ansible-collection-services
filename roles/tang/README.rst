This ansible role install Tang.
Tang server for binding data to network presence.

**Role Variables**

.. zuul:rolevar:: tang_service_name
   :default: tangd
   
   The tang service and process name

.. zuul:rolevar:: systemd_destination
   :default: /lib/systemd/system

   The default systemd path

.. zuul:rolevar:: tang_port
   :default: 80

   The default port for tang is 80, which is normally reserved for webservices
