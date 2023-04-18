FROM python:3.8

RUN mkdir -p /opt/services/manga-backend

WORKDIR /opt/services/manga-backend

ADD requirements.txt /opt/services/manga-backend/

ADD . /opt/services/manga-backend/

RUN pip install -r requirements.txt