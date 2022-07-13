This role configures options for journald.

**Role Variables**

.. zuul:rolevar:: journald_SystemMaxUse
   :default: 2000M

Control how many disk space journald can use.

.. zuul:rolevar:: journald_SystemKeepFree
   :default: 1000M

Configure how many disk space journald have to leave free.

.. zuul:rolevar:: journald_SystemMaxFileSize
   :default: 100M

This defines how large individual journald files may become.

.. zuul:rolevar:: journald_RuntimeMaxUse
   :default: 2000M

Control how many disk space journal can use.

.. zuul:rolevar:: journald_RuntimeKeepFree
   :default: 1000M

Configure how many disk space journald have to leave free.

.. zuul:rolevar:: journald_RuntimeMaxFileSize
   :default: 100M

This defines how large individual journald files may become.

.. zuul:rolevar:: journald_service_name
   :default: systemd-journald

Name from the journald service to deal with it.
