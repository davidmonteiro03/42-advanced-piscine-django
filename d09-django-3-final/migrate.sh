#!/bin/bash

runcmd()
{
	echo -ne "$1... "
	shift
	$* > /dev/null 2>&1 && echo -e "\e[38;2;0;150;0mOK\e[0m" || echo -e "\e[38;2;150;0;0mFAILED\e[0m"
}

runcmd "Making migrations"       python3 manage.py makemigrations account chat
runcmd "Applying migrations"     python3 manage.py migrate
runcmd "Collecting static files" python3 manage.py collectstatic --noinput
