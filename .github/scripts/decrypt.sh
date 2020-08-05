#!/usr/bin/env bash

mkdir -p $HOME/.config/openstack
gpg --quiet --batch --yes --decrypt --passphrase="$MOLECULE_SECRET_PASSPHRASE" \
  --output $HOME/.config/openstack/clouds.yml .clouds.yml.gpg
