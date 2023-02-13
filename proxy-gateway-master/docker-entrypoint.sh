#!/bin/bash

cd /usr/srv/genesis_proxy_gateway/src &&
python3 manage.py migrate &&
python3 manage.py auto_create_super_user &&
uvicorn gpg_api.asgi:application --host 0.0.0.0 --port 8000