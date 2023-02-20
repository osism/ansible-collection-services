Troubleshooting
---------------

Your git repos are not displayed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Have you thought of naming your repos with the prefix of your organization? `release` should be `osism/release` for example.

Your git repos are using the wrong branch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For `config-projects` you set this value in the tenant-configuration with the `load-branch` stanza.
For `untrusted-projects` you set this value in the config-projects `project` sections AND in EVERY `untrusted-project`.
Each `project` section needs to have the `default-branch` stanza.

Your logs are not displayed in the web-UI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check, if the IP of the logfile server is really correct. In combination with GitHub there is a
bug which keeps the GitHub App posting to the old IP even if the webhook IP was changed. Current
workaround: Delete the old GitHub App and create a new one.
