#!/bin/sh

apt-get install -y gcc make automake autoconf python3-dev python3-pip
pip install -r /home/site/wwwroot/requirements.txt
which flask
cd /home/site/wwwroot
flask --app app run --port 8000
