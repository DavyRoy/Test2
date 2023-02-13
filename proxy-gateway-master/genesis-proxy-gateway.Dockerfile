FROM ${GB_REGISTRY}/python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

COPY src src

RUN rm -rf src/gpg_api/settings/.env \
    && groupadd -g 1000 app_user \
    && useradd -u 1000 -g app_user app_user \
    && chown -R app_user:app_user /app

WORKDIR /app/src
