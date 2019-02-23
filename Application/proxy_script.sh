#!/bin/bash

#This is a script to easily start the cloud proxy server. Just call it like this ./proxy_script.sh 'password'    password where password is you root/sudo password

PASSWORD="$1"

if [ -n "$PASSWORD" ]
	then
sudo /etc/init.d/mysql stop $PASSWORD
./cloud_sql_proxy -instances="plantdatabase-51026:us-central1:mysql-plant-database"=tcp:3306
else
	echo Please type in your SUdo password. example: ./proxy_script.sh password
fi
