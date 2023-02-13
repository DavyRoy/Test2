FROM python:3.10-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/srv/genesis_proxy_gateway

COPY requirements.txt .

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY src src

COPY docker-entrypoint.sh .

COPY ./wait-for-it.sh .

RUN python3 src/manage.py collectstatic

CMD cd src && uvicorn gpg_api.asgi:application --host 0.0.0.0 --port 8000
