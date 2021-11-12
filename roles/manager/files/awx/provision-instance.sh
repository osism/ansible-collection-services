#!/usr/bin/env bash

echo 'from django.conf import settings; x = settings.AWX_TASK_ENV; x["HOME"] = "/var/lib/awx"; settings.AWX_TASK_ENV = x' | awx-manage shell
awx-manage provision_instance --hostname=$(hostname) --node_type=control
awx-manage register_queue --queuename=tower --instance_percent=100 --hostnames=$(hostname)
