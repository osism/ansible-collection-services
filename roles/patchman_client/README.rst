This ansible role install Patchman-client.
The Patchman-client manage the list of packages for the Patchman server.
Patchman-client can also be used to inspect the version of a package on
a certain host.

**Role Variables**

.. zuul:rolevar:: patchman_client_cron_day
   :default: *

Day-parameter for the Patchman-client cronjob.

.. zuul:rolevar:: patchman_client_cron_hour
   :default: 0

Hour-Parameter for the Patchman-client cronjob.

.. zuul:rolevar:: patchman_client_cron_minute
   :default: 3

Minute-parameter for the Patchman-client cronjob.

.. zuul:rolevar:: patchman_client_cron_user
   :default: {{ operator_user | default('dragon') }}

User that should hold the cronjobs for Patchman-client.

.. zuul:rolevar:: patchman_client_curl_options
   :default: --insecure --connect-timeout 60 --max-time 300

Settings for curl.

.. zuul:rolevar:: patchman_client_report
   :default: 0

# FIX ME

.. zuul:rolevar:: patchman_client_tags
   :default: Server

# FIX ME

.. zuul:rolevar:: patchman_client_host
   :default: localhost

The host where Patchman-client will be reachable.

.. zuul:rolevar:: patchman_client_port
   :default: 8150

Port which Patchman-client will use for connections from outside.

.. zuul:rolevar:: patchman_client_server_url
   :default: http://{{ patchman_client_host }}:{{ patchman_client_port }}

The url under which Patchman server is reachable.

.. zuul:rolevar:: patchman_client_update_statfile
   :default: /tmp/patchman-client.stat

File to safe the last execution time of Patchman-client.

.. zuul:rolevar:: patchman_client_update
   :default: true

Enables the update funktion from Patchman-client.

.. zuul:rolevar:: patchman_client_update_force
   :default: false

Forces the update run to be executed.

.. zuul:rolevar:: patchman_client_update_valid_time
   :default: 86400

Defines the intervall for how long an update is considerd as valid.
