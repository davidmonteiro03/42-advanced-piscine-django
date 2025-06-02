#!/bin/bash

runcmd()
{
	echo -ne "$1... "
	shift
	$* > /dev/null 2>&1 && echo -e "\e[38;2;0;150;0mOK\e[0m" || echo -e "\e[38;2;150;0;0mFAILED\e[0m"
}

runcmd "Saving users" python3 manage.py dumpdata auth.user --output=account/users.json
runcmd "Saving chat rooms" python3 manage.py dumpdata chat.room --output=chat/rooms.json
