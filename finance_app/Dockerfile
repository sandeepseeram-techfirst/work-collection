FROM nginx/unit:1.17.0-php7.3

COPY config.json /docker-entrypoint.d/
COPY files/ /www/files/

RUN apt-get update && apt-get install -yq --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8080