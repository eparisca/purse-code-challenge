FROM python:3.9.6-alpine3.14

ARG APP_NAME
ENV APP_NAME ${APP_NAME}

RUN apk add --update \
 && apk add --no-cache bash postgresql-libs postgresql-dev libffi-dev openssl-dev \
 && apk add --no-cache --virtual build-dependencies build-base gcc musl-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "-m", "api" ]

EXPOSE 5000