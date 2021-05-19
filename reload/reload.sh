#!/bin/bash

git pull origin master
python manage.py collectstatic
sudo systemctl restart nginx
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nginx -t