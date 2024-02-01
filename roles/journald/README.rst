This role configures options for journald.

**Role Variables**

.. zuul:rolevar:: journald_system-max-use
   :default: 2000M

Control how many disk space journald can use.

.. zuul:rolevar:: journald_system-keep-free
   :default: 1000M

Configure how many disk space journald have to leave free.

.. zuul:rolevar:: journald_system-max-file-size
   :default: 100M

This defines how large individual journald files may become.

.. zuul:rolevar:: journald_runtime-max-use
   :default: 2000M

Control how many disk space journal can use.

.. zuul:rolevar:: journald_runtime-keep-free
   :default: 1000M

Configure how many disk space journald have to leave free.

.. zuul:rolevar:: journald_runtime-max-file-size
   :default: 100M

This defines how large individual journald files may become.

.. zuul:rolevar:: journald_service_name
   :default: systemd-journald

Name from the journald service to deal with it.
