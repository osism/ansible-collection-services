#!/usr/bin/env bash

docker build -t zabbix-agent-extension-mysql .
docker run -v $PWD:/data --rm --entrypoint cp zabbix-agent-extension-mysql .out/zabbix-agent-extension-mysql /data
docker rmi zabbix-agent-extension-mysql
