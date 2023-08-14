#!/bin/sh -e

python /app/manage.py migrate --no-input
python /app/manage.py createcachetable
python /app/manage.py collectstatic --no-input
python /app/manage.py test --no-input
python /app/manage.py makemigrations --check --dry-run --no-input
