#!/bin/sh

python /src/manage.py migrate
python /src/manage.py loaddata dev
python /src/manage.py runserver 0.0.0.0:8080
