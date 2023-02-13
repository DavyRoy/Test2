#!/bin/bash

cd /usr/srv/user-api/src &&
python3 manage.py migrate &&
python3 manage.py auto_create_super_user &&
python3 manage.py cache_users &&
uvicorn user_api_settings.asgi:application --host 0.0.0.0 --port 8000