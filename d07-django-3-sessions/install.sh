#!/bin/bash
python3 -m venv virtualenv
source virtualenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --force-reinstall -r requirements.txt
python3 ex/manage.py makemigrations app
python3 ex/manage.py migrate
