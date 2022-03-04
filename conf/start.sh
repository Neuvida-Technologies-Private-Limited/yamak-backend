#! /usr/bin/env sh

# abort is any error happens
set -e

# start supervisor with nginx -> uwsgi -> app
exec /usr/bin/supervisord
