# 📑 Document API Service

## Development

## Building

### Environment

See `.env.example` file

### Requirements

### Docker

Create _gen_dev_ network

`docker network create gen_dev`

**1. Launch APP**

_JOIN TO PROJECT ROOT_

 `docker-compose -f docker-compose.dev.yml up --build -d postgres`

 `docker-compose -f docker-compose.dev.yml up --build document_api`

**2. First launch**

_JOIN TO PROJECT ROOT_

**_For enter to container at first, look at all containers_**

2.1 `docker ps`

2.2 Find _your_ container, its look like `genesis-api_document_api_1`, copy his _CONTAINER ID_

2.3 `docker exec -it CONTAINER ID bash`

**_Or you can do it same using Docker GUI_**

_In container_

2.4 `cd src && python manage.py createsuperuser`

2.5 Create admin user (_recommended_ **root : root**)

\*\*Gratz, now u have acc

## Deploy
