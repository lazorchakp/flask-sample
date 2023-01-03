#!/bin/sh

apt-get update
apt-get install -y gcc make automake autoconf python3-dev python3-pip
pip -r /home/site/wwwroot/requirements.txt