#!/bin/bash

cd /usr/srv/gen_task/src &&
python3 manage.py migrate &&
python3 manage.py auto_create_super_user &&
uvicorn gen_task_api.asgi:application --host 0.0.0.0 --port 8000