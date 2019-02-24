#!/bin/bash

#This combines the collection of static items,  Synchronizes them to our plant bucket, and deploy the apps.

python3 manage.py collectstatic
gsutil rsync -R static/ gs://plantbucket2/static
gcloud app deploy
