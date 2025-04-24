#!/bin/bash

python3 manage.py clearsessions
python3 manage.py test control
