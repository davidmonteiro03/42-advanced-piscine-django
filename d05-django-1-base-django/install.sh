#!/bin/bash
python3 -m venv virtualenv
source virtualenv/bin/activate
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
python manage.py migrate
