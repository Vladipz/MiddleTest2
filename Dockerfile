FROM python:3.11.4-slim-buster

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENV PORT=8000
EXPOSE $PORT

RUN python manage.py migrate

ENV DJANGO_SUPERUSER_USERNAME=admin1
ENV DJANGO_SUPERUSER_EMAIL=admin1@gmail.com

RUN python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL

CMD python manage.py runserver 0.0.0.0:$PORT
