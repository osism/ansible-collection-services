#!/usr/bin/env bash

if [[ ! -z "$AWX_ADMIN_USER" ]] && [[ ! -z "$AWX_ADMIN_PASSWORD" ]]; then

  result=$(echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$AWX_ADMIN_USER').count()>0)" | awx-manage shell | tail -n 1)

  if [ $result == "False" ]; then

    echo "from django.contrib.auth.models import User; User.objects.create_superuser('$AWX_ADMIN_USER', '$AWX_ADMIN_MAILADDRESS', '$AWX_ADMIN_PASSWORD')" | awx-manage shell

  fi

fi
