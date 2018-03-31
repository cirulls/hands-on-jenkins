#!/bin/bash

hostname='localhost'
port=$1

status_code=$(curl --write-out %{http_code} ${hostname}:${port})

if [ $status_code == 200 ];
then
	echo "PASS: ${hostname}:${port} is reachable"
else
	echo "FAIL: ${hostname}:${port} is unreachable"
    exit 1
fi
