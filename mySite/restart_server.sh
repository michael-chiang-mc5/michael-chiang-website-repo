#!/bin/bash

python manage.py collectstatic
pkill -f /home/michaelc/dev/michael-chiang-website-repo/venv/bin/gunicorn
# python manage.py migrate --run-syncdb
gunicorn mySite.wsgi --bind 127.0.0.1:8001 --daemon --log-file ~/dev/logs/michael-chiang-website.log --workers=1
