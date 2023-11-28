FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
