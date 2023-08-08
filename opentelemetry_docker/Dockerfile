# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0
 
FROM python:3.10-slim-bullseye as base
#omitted for clarity
 
FROM base as runtime
WORKDIR /usr/src/app/
COPY --from=builder /reqs /usr/local
COPY --from=grpc-builder /usr/src/app/ .
COPY ./src/recommendationservice/ ./
 
# the ‘opentelemetry-bootstrap’ agent is declared in requirements.txt
RUN opentelemetry-bootstrap -a install
 
# call opentelemetry-instrument before calling python to run it
EXPOSE ${RECOMMENDATION_SERVICE_PORT}
ENTRYPOINT [ "opentelemetry-instrument", "python", "recommendation_server.py" ]