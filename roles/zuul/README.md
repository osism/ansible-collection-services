zuul
====

Ansible role to set up zuul on a single-node installation with docker-compose.

Requirements
------------

docker.io
docker-compose

Role Variables
--------------

Please look into the defaults file. The content would be too complex to display it here in a clear manner.
If you are not familiar with zuul you should have at the "Quick-Start" from zuul-ci.org before using this role.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - name: setup zuul playbook
      hosts: zuul.osism.com
      roles:
         - name: setup zuul role
           role: zuul

Troubleshooting
---------------

**Your git repos are not displayed?**
Have you thought of naming your repos with the prefix of your organization? *release* should be *osism/release* for example.

**Your git repos are using the wrong branch?** 
For *config-projects* you set this value in the tenant-configuration with the *load-branch* stanza.
For *untrusted-projects* you set this value in the config-projects *project* sections AND in EVERY *untrusted-project*.
Each *project* section needs to have the *default-branch* stanza.

**Your logs are not displayed in the web-UI?**
Check, if the IP of the logfile server is really correct. In combination with GitHub there is a bug which keeps the GitHub App posting to the old IP even if the webhook IP was changed. Current workaround: Delete the old GitHub App and create a new one.

License
-------

Apache License 2.0

Author Information
------------------

Created by Tim Beermann in behalf of OSISM GmbH.
