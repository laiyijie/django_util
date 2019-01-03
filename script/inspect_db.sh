#!/bin/bash
set -x
set -e

SYS=$(uname -s)
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
cd $SCRIPT_PATH
cd ../django_server
python3 manage.py  inspectdb --database=data > transfer/models.py
if [ $SYS == "Darwin" ];then
    sed -i '.bak' '/managed = False/d' transfer/models.py
else
    sed -i '/managed = False/d' transfer/models.py
fi
rm -f transfer/models.py.bak
rm -f transfer/migrations/0001_initial.py
python3 manage.py makemigrations

