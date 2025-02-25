#!/bin/bash
python3 -m pip install --upgrade pip

# Create a virtualenv on python3 named django_venv
python3 -m venv django_venv
source django_venv/bin/activate

# Install the requirement.txt file that you’ve created in the VirtualEnv
python3 -m pip install --upgrade --force-reinstall -r requirement.txt
