#!/usr/bin/env sh

# abort is any error happens
set -e

# run migration if any
python manage.py migrate

# setup nginx
cp /app/conf/nginx.conf /etc/nginx/nginx.conf
printf "" > /etc/nginx/conf.d/default.conf

# explicitly installed python packages and uwsgi Python packages to PYTHONPATH
if [ -n "$ALPINEPYTHON" ] ; then
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/$ALPINEPYTHON/site-packages:/usr/lib/$ALPINEPYTHON/site-packages
fi
exec "$@"
