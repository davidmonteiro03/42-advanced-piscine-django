#!/bin/bash
venv_name='local_lib'
log_file='path-pip-install.log'
program_name='my_program.py'
git_repo_link='https://github.com/jaraco/path.git'

python3 -m venv "$venv_name"
source "$venv_name/bin/activate"

echo "--------- Pip version ---------"
python3 -m pip --version

echo "--- Installing the package ----"
python3 -m pip install --log "$log_file" --force-reinstall "git+$git_repo_link"

echo "---- Running my_program.py ----"
python3 "$program_name"
