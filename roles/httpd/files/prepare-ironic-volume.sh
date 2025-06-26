#!/bin/sh

if [ ! -d "/var/lib/ironic/httpboot" ]; then
    addgroup -g 42422 ironic
    adduser -D -u 42422 -g ironic ironic
    mkdir -p /var/lib/ironic/httpboot
fi
