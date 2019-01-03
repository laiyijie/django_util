#!/bin/bash
set -x
set -e

SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
ENV=$1
CMD=$2
if [ -z "$1" ]
then
    ENV=DEFAULT
fi
cd $SCRIPT_PATH
cd ..
docker build . -f Dockerfiles/Dockerfile --tag dm_server

docker run --network=host -it -e DEC_ENV=$ENV dm_server $2
