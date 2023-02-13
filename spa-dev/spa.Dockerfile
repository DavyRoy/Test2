FROM ${GB_REGISTRY}/node:16-alpine as develop-stage
WORKDIR /app
COPY ./package*.json ./
RUN yarn add global @quasar/cli @vue/cli @vue/cli-init
COPY . .
RUN yarn

# build app
FROM ${GB_REGISTRY}/node:16-alpine as build-stage
ENV VUE_APP_ROUTER_MODE="${VUE_APP_ROUTER_MODE}"
ENV VUE_APP_PROXY_URI="${VUE_APP_PROXY_URI}"
ENV DEBUGGING=${DEBUGGING}
ENV MODE="${MODE}"
ENV NODE_ENV="${NODE_ENV}"

WORKDIR /app
COPY --from=develop-stage /app .
RUN yarn build

# build stage
FROM ${GB_REGISTRY}/nginx:alpine as deploy-stage
RUN rm -rf /usr/share/nginx/html/*
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html
COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./.nginx/spa.conf /etc/nginx/conf.d/

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
