FROM node:latest
COPY ./client client
WORKDIR ./client
RUN npm install && npm run buildDev

FROM nginx:latest
COPY ./static /etc/nginx/html/static
COPY --from=0 /client/dist/bundle.js /etc/nginx/html/static/bundle.js
COPY ./ngnix.development.conf /etc/nginx/nginx.conf
