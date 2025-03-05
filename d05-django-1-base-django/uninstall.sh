#!/bin/bash
deactivate 2>/dev/null || true
rm -rfv virtualenv 2>/dev/null || true
find * -type d -name 'migrations' -exec rm -rfv {} \; 2>/dev/null || true
find * -type d -name '__pycache__' -exec rm -rfv {} \; 2>/dev/null || true
find * -type f -name '*.sqlite3' -exec rm -rfv {} \; 2>/dev/null || true
