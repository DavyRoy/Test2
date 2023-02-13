# dependency install
FROM node:16-alpine as develop-stage
WORKDIR /app
COPY ./package*.json ./
RUN yarn add global @quasar/cli @vue/cli @vue/cli-init
COPY . .
RUN yarn
# FROM node:16-alpine as test-stage

# build app
FROM node:16-alpine as build-stage
ENV VUE_APP_PROXY_URI=${VUE_APP_PROXY_URI}
ENV VUE_APP_ROUTER_MODE=${VUE_APP_ROUTER_MODE}
ENV NODE_ENV=${NODE_ENV}
ENV VUE_APP_PORT=${VUE_APP_PORT}
ENV MODE=${MODE}
ENV DEBUGGING=${DEBUGGING}
WORKDIR /app
COPY --from=develop-stage /app .
RUN yarn build

# deploy stage
FROM nginx:alpine as deploy-stage
RUN rm -rf /usr/share/nginx/html/*
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html
COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./.nginx/spa.conf /etc/nginx/conf.d/

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
