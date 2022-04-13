FROM python:3.9.7-alpine3.13
RUN apk add --no-cache bash

RUN apk add build-base
RUN apk add --update musl-dev gcc libffi-dev python3-dev

RUN apk add --no-cache chromium
RUN apk add --no-cache chromium-chromedriver

RUN mkdir /app
WORKDIR /app

EXPOSE 10000

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT gunicorn -w 4 -b:10000 --logger-class "gunicorn_logger.CustomLogger" --access-logfile - app:app
