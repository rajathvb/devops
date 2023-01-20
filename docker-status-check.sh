#!/bin/bash

# The script checks if a container is running.
#   OK - running
#   CRITICAL - container is stopped
#   UNKNOWN - does not exist
date=$(date +"%Y-%m-%d %H:%M:%S")
file=/home/ubuntu/docker_containers.sh
while read line
do
#CONTAINER=$1
CONTAINER=$( echo "$line" )
RUNNING=$(sudo docker inspect --format="{{ .State.Running }}" $CONTAINER 2> /dev/null)

if [ $? -eq 1 ]; then
  echo "UNKNOWN - $CONTAINER does not exist."
   echo "$CONTAINER does not exist" | mailx -s "Test message" <mail_id>
fi
if [ "$RUNNING" == "false" ]; then
  echo "CRITICAL - $CONTAINER is not running"
   echo "$CONTAINER is stopped at" $date | mailx -s "Test message" <mail_id>
fi
 
STARTED=$(sudo docker inspect --format="{{ .State.StartedAt }}" $CONTAINER)
NAME=$(sudo docker inspect --format="{{ .Name }}" $CONTAINER)
#NETWORKMODE=$(sudo docker inspect --format="{{ .HostConfig.NetworkMode }}" $CONTAINER)
#NETWORK=$(sudo docker inspect --format="{{ .NetworkSettings.Networks."$NETWORKMODE".IPAddress }}" $CONTAINER)
echo "OK - $CONTAINER is running, StartedAt: $STARTED, Named: $NAME"
#echo "OK - $CONTAINER is running. IP: $NETWORK, StartedAt: $STARTED, Named: $NAME"
done < ${file}

file=telnet.sh
while read line
do
  ip=$( echo "$line" |cut -d ' ' -f 1 )
  port=$( echo "$line" |cut -d ' ' -f 2 )
  if  telnet  $ip $port </dev/null 2>&1 | grep -q Escape
  then
    echo "$ip $port Connected"
  elif  telnet  $ip $port </dev/null 2>&1 | grep -q refused
  then
    echo "$ip $port Refused"
  else
    echo "$ip $port Failed"
  fi
done < ${file}
