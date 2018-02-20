FROM ubuntu:17.10

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update \
 && apt-get -y install \
      python3.6 python3.6-venv \
      nginx uwsgi uwsgi-plugin-python3

WORKDIR /srv

RUN python3.6 -m venv venv
COPY requirements-base.txt requirements-prod.txt ./
RUN venv/bin/pip install -r requirements-prod.txt

COPY . .

RUN cp deploy/nginx.conf /etc/nginx/sites-enabled/default \
 && cp deploy/mime.types /etc/nginx/

ENV DJANGO_SETTINGS_MODULE demoproject.settings_prod

CMD service nginx start \
 && exec uwsgi \
      --plugin python3 \
      --socket /tmp/uwsgi.sock \
      --threads 2 \
      --uid www-data \
      --gid www-data \
      --venv /srv/venv \
      --wsgi demoproject.wsgi:application \
      --attach-daemon2 'cmd=venv/bin/celery -A demoproject worker -l info -c 1 -B --scheduler django_celery_beat.schedulers:DatabaseScheduler' \
      --reload-mercy 120
