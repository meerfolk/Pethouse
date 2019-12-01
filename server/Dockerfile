FROM python:3.7.0-alpine

RUN pip install pipenv

RUN mkdir /src

WORKDIR /src

COPY ./Pipfile Pipfile

RUN pipenv install
