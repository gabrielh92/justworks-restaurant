FROM python:3.10.9-bullseye AS builder
LABEL maintainer "Gabriel Hruskovec <gabrielh92@gmail.com"

RUN mkdir /server

WORKDIR /server
COPY requirements.txt /server
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY src /server

ENV FLASK_APP=server.py
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0

ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

EXPOSE 8080
CMD [ "uvicorn", "src.server:server", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080" ]
