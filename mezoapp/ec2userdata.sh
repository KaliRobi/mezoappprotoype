#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y python3.10 python3-pip git
sudo mkdir -p /var/www/mezoappproto
cd /var/www/mezoappproto
git clone https://github.com/KaliRobi/mezoappsingle.git
python3.10 -m venv venv
source venv/bin/activate
pip install -r mezoappsingle/requirements.txt
cd mezoappsingle/mezoapp/
python manage.py migrate
python manage.py runserver 0.0.0.0:8000