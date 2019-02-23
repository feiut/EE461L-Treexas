#!/bin/bash

#This script simply runs all three commands one after the other. This makes migrations quicker (not so much typing). To run just type the command ./migration_script.sh

python3 manage.py makemigrations
python3 manage.py makemigrations plantsite
python3 manage.py migrate

