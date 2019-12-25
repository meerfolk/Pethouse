FROM python:3.7-slim-buster

RUN pip install pipenv

RUN mkdir /src

WORKDIR /src

COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock

RUN pipenv install
