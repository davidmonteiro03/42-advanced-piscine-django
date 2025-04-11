#!/bin/bash

runcmd()
{
	$* > /dev/null 2>&1 || true
}

runcmd deactivate
runcmd rm -rfv virtualenv
runcmd find * -type d -name 'migrations'  -exec rm -rfv {} \;
runcmd find * -type d -name '__pycache__' -exec rm -rfv {} \;
runcmd find * -type f -name '*.sqlite3'   -exec rm -rfv {} \;
