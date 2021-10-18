zuul
====

Ansible role to setup zuul on a single-node installation with docker-compose.

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

Enable debugging
----------------

If you don't know why something is not working as expected, you can enable logging by 
putting this content into a file called log.conf next to your zuul.conf:
```ini
[loggers]
keys=root,zuul

[handlers]
keys=console

[formatters]
keys=simple

[logger_root]
level=DEBUG
handlers=console

[logger_zuul]
level=DEBUG
handlers=console
qualname=zuul
propagate=0

[handler_console]
level=DEBUG
class=StreamHandler
formatter=simple
args=(sys.stdout,)

[handler_debug]
level=DEBUG
class=logging.handlers.TimedRotatingFileHandler
formatter=simple
args=('/var/log/zuul/debug.log', 'midnight', 1, 30,)

[handler_normal]
level=INFO
class=logging.handlers.TimedRotatingFileHandler
formatter=simple
args=('/var/log/zuul/zuul.log', 'midnight', 1, 30,)

[formatter_simple]
format=%(asctime)s %(levelname)s %(name)s: %(message)s
datefmt=
```

Enable this by extending your zuul.conf in the right places:
```
[gearman]
log_config=/etc/zuul/log.conf

[gearman_server]
log_config=/etc/zuul/log.conf

[zookeeper]
log_config=/etc/zuul/log.conf

[scheduler]
log_config=/etc/zuul/log.conf

[connection "githubzuulapp"]
log_config=/etc/zuul/log.conf

[executor]
log_config=/etc/zuul/log.conf
```

After a restart of the affected components you should now be able to see DEBUG messages in the container logs.

Troubleshooting
---------------

**Your pipelines are running but retry and fail?**
Try to SSH into your worker nodes. If this is not working, check the node from inside.
The *.ssh* folder and the *authorized_keys* file need to be owned by the user you are connecting with (mostlikely root).
Check if the *authorized_keys* file needs to contain the public key of the nodepool_launcher called *nodepool.pub*.
If you are wondering why this worker once and not any more, keep in mind that worker nodes are based on *docker build images*.
You need to trow it away before you redeploy, otherwise the pubkey of the initial deployment is used.

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
