#!/bin/sh
set -e

# python manage.py collectstatic --no-input

# inspired by https://www.tigersandtacos.dev/posts/django-with-sqlite3-made-durable-with-litestream-and-caddy/
# if the db file doesn't exist we get it from the REPLICA_URL

# Restore the database if it does not already exist.
if [ -f $DB_NAME ]; then
	echo "Database already exists, skipping restore"
else
	echo "No database found, restoring from replica if exists"
	litestream restore -v -if-replica-exists /code/db/prod.sqlite3
fi

python manage.py migrate
#python manage.py collectstatic --no-input --clear

litestream replicate --exec="gunicorn --workers=2 --bind=0.0.0.0:8000 pat.wsgi"
