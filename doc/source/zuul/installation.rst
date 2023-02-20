Installation
============

Server preparation
------------------

Set up a server (VM) with Ubuntu Server 22.04 LTS and make
sure that these packages are installed::

    docker.io
    docker-compose
    python3-docker
    python3-openstackclient

Also configure your deploy user to be in the docker group and set up the
account for the zuul user. TCP-Ports 80 and 443 should be accessible
from the internet, port 22 for management via SSH will also often be
useful, but not required.

If you have an OpenStack tenant where you want to deploy the Zuul
server, you can download and adapt this example
playbook: :download:`deploy.yaml <playbooks/deploy.yaml>`

Define secrets
--------------

There need to be some secrets handed to the deployment, the suggested
method is to have a dedicated file that contains them, which will be
included in the example playbook below via a `vars_files` statement.
This allows you to easily protect all your secrets by applying
`ansible-vault encrypt` to that file. The contents of this file should
look like::

    ---
    zuul_auth_secret: secret used for zuul web auth
    webhook_token: token defined for github webhooks
    db_user_pass: DB password for the zuul user
    db_root_pass: DB root password

In addition you need to prepare some further data that needs to be
placed into a `files` directory in order to be consumed by the zuul
role. These are:

#. A `clouds.yaml` file for nodepool. This will be used by
   `nodepool-builder` to upload the newly created images and by
   `nodepool-launcher` to start instances running these images, these
   will then be handed over to Zuul as CI nodes.
#. An SSH private key in the file `nodepool` and the matching public
   key in `nodepool.pub`. These will be used by nodepool and zuul to
   access the CI nodes via SSH.
#. An SSL private key and certificate pasted together in a file
   named `server.crt`. This file will be used in the https setup by
   the webserver. The certificate should cover both `zuul_webserver_fqdn`
   and `zuul_logserver_fqdn`.

Github App setup
----------------

In order for zuul to be able to interact with repositories hosted on
github, you need to set up a github application. Follow the instructions
at https://zuul-ci.org/docs/zuul/latest/drivers/github.html#application
to do this. The webhook token to use is the one defined in the
pervious section. Use `github` in place of `<connection-name>` for the
Webhook URL in the app configuration. After the app has been created,
place the PEM files that you downloaded into a
directory named `pem-files`::

    $ mkdir -p pem-files
    $ cp ~/Downloads/my-org-zuul.*.private-key.pem pem-files/my-org-zuul.pem

Now add the information about your github app to `vars.yml`::

    github_app_id: 000000
    github_pem_name: my-org-zuul

Example Playbook
----------------

Save this file as `main.yaml`::

    ---
    - name: Set up zuul
      hosts: zuul.example.com
      vars_files:
        - vars.yml
      pre_tasks:
        - name: Create /etc/openstack/
          ansible.builtin.file:
            state: directory
            path: /etc/openstack
            owner: root
            group: root
            mode: 0755
          become: true

        - name: Deploy clouds.yaml file
          ansible.builtin.copy:
            src: clouds.yaml
            dest: /etc/openstack/clouds.yaml
            owner: root
            group: zuul
            mode: '0640'
          become: true

        - name: Create keypair in the cloud
          openstack.cloud.keypair:
            cloud: osism-ci
            name: osism-zuul
            public_key: "{{ lookup('file', 'nodepool.pub') }}"
          become: true

      roles:
        - name: Execute zuul role
          role: zuul
          vars:
            zuul_connections:
              github:
                driver: github
                webhook_token: "{{ webhook_token }}"
                app_id: "{{ github_app_id }}"
                app_key: "/etc/zuul/pem-files/{{ github_pem_name }}.pem"
              opendevorg:
                name: opendev
                driver: git
                baseurl: https://opendev.org
            zuul_tenants:
              - tenant:
                  name: my-tenant-name
                  source:
                    opendevorg:
                      untrusted-projects:
                        - zuul/zuul-jobs:
                            include:
                              - job
                    github:
                      config-projects:
                        - my-org/zuul_demo_config:
                            load-branch: main
                      untrusted-projects:
                        - my-org/zuul_demo_repo
          become: true

Create an `inventory` file containing the login information for your zuul
server, it might look like::

    zuul.example.com ansible_host=192.0.2.2 ansible_user=ubuntu

Then you can deploy your zuul server by running::

    ansible-playbook -i inventory main.yaml

This will deploy a simple zuul setup with sample example repos being
referenced. You can fork the example repos from the
https://github.com/osism tenant or just use them as a guide for how
to build your own.

For further information about how to tune this setup for
you specific environment, have a look at the sections covering
nodepool and tenant configuration.
