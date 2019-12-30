FROM python:3.8

WORKDIR /app

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .
