!/bin/bash

if [ -f /tmp/userlist ]
then
	for i in $(cat /tmp/userlist)
	do
		if [ -f /usr/bin/pwgen ]
		then
			PASSWORD=$(pwgen -1 -s 16)
		else
			PASSWORD=$(cat /dev/urandom | tr -dc "passwordNSR!@#$%0-9" | fold -w 9 | head -1)
		fi
		echo $PASSWORD
		pass=$(perl -e 'print crypt($ARGV[0], "password")' $PASSWORD)
		useradd -m -p "$pass" "$i" 
		echo "$i --------- $PASSWORD" >>/tmp/userlist-created
	done
else
	echo "File /tmp/userlist not found"
fi
chmod 0600 /tmp/userlist-created
