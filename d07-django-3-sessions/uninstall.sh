#!/bin/bash
deactivate                                             > /dev/null 2>&1 || true
rm -rfv virtualenv                                     > /dev/null 2>&1 || true
find * -type d -name 'migrations'  -exec rm -rfv {} \; > /dev/null 2>&1 || true
find * -type d -name '__pycache__' -exec rm -rfv {} \; > /dev/null 2>&1 || true
find * -type f -name '*.sqlite3'   -exec rm -rfv {} \; > /dev/null 2>&1 || true
