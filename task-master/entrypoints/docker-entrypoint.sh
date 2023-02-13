#!/bin/bash

# Migrate
python3 /usr/srv/gen-task/src/manage.py migrate

#Create superuser
python3 usr/srv/gen-task/src/manage.py auto_create_super_user

# Run as usual
cd src && uvicorn gen-task.asgi:application --host 0.0.0.0 --port 8000
