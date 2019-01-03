#!/bin/bash

set -x
set -e

SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)

cd $SCRIPT_PATH
cd ..
cd django_server
python3 -Wd manage.py test --noinput -v 2 $@
