#!/bin/bash
set -x 
set -e
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
ENV=$1
CMD=$2
cd $SCRIPT_PATH
./docker_run.sh DEFAULT "python3 /django_server/manage.py test /django_server/"

if [ -z "$1" ]
then
    ENV=DEFAULT
fi
container_name=dm_server_$ENV
cd ..
docker build . -f Dockerfiles/Dockerfile --tag dm_server
if [ false != $(docker inspect -f '{{.State.Running}}' $container_name) ]
then
    docker kill $container_name
    docker rm $container_name
fi
docker run --network=host -d -e DM_ENV=$ENV --name $container_name -v /tmp/dm_server:/var/log/django_server dm_server $2
