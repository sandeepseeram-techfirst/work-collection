FROM nginx/unit:1.17.0-php7.3

COPY config.json /docker-entrypoint.d/
COPY api/ /www/api/

RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    nano \
    php7.3-curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8080