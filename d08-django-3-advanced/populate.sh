#!/bin/bash

runcmd()
{
	echo -ne "$1... "
	shift
	$* > /dev/null 2>&1 && echo -e "\e[38;2;0;150;0mOK\e[0m" || echo -e "\e[38;2;150;0;0mFAILED\e[0m"
}

runcmd "Creating users"       python3 manage.py loaddata control/users.json
runcmd "Creating articles"    python3 manage.py loaddata control/articles.json
runcmd "Creating favourites"  python3 manage.py loaddata control/favourites.json
runcmd "Setting up passwords" python3 manage.py shell < control/setup_pws.py
