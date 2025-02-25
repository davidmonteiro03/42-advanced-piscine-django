#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m venv helloworld_env
source helloworld_env/bin/activate
python3 -m pip install --upgrade --force-reinstall -r requirement.txt
