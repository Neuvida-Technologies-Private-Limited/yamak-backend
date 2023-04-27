FROM python:3.9.2-slim-buster

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# update system and some dependent packages
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev libssl-dev gcc \
  libmagic-dev libpcre3 libpcre3-dev supervisor

# gather requirements and prerequisites
# take advantage of layer caching
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt;
RUN pip install -Iv uwsgi==2.0.18

# remove downloaded packages which was installed
RUN rm -rf /var/lib/apt/lists/*

# supervisor setup
COPY /conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# nginx setup
COPY conf/nginx.sh /app/conf/nginx.sh
RUN bash /app/conf/nginx.sh
RUN rm /etc/nginx/conf.d/default.conf

# setup app folder and copy the app
COPY . /app/
WORKDIR /app

# copy app entry and start to other directory
COPY conf/entry.sh /
COPY conf/start.sh /

# permission for script execution
RUN chmod +x /entry.sh
RUN chmod +x /start.sh

# uwsgi setup
COPY /conf/uwsgi.ini /etc/uwsgi/uwsgi.ini

ENTRYPOINT ["/entry.sh"]
USER root
CMD ["/start.sh"]
