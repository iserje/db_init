FROM public.ecr.aws/bitnami/python:latest
LABEL maintainer="Serge Ivanov serje@homtial.com"

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app
COPY requirements.txt /app

RUN apt-get update \
    && apt-get install -y python3-psycopg2 \
    && apt-get install -y --reinstall libpq-dev \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

ENTRYPOINT []
CMD ["python", "db.py"]