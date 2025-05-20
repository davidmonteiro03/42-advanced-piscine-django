#!/bin/bash

runcmd()
{
	echo -ne "$1... "
	shift
	$* > /dev/null 2>&1 && echo -e "\e[38;2;0;150;0mOK\e[0m" || echo -e "\e[38;2;150;0;0mFAILED\e[0m"
}

runcmd "Creating database and redis containers"         docker-compose up --build -d
runcmd "Creating virtual environment"                   python3 -m venv virtualenv
runcmd "Activating virtual environment"                 . virtualenv/bin/activate
runcmd "Upgrading pip package installer"                python3 -m pip install --upgrade pip
runcmd "Installing packages from requirements.txt file" python3 -m pip install --force-reinstall -r requirements.txt
