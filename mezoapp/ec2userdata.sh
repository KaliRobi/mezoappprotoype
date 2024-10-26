#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo mkdir -p /var/www/mezoappproto
cd /var/www/mezoappproto
sudo git clone https://github.com/KaliRobi/mezoappsingle.git
sudo apt install -y python3.12-venv
sudo python3.12 -m venv venv
source venv/bin/activate
sudo chown -R ubuntu:ubuntu /var/www/mezoappproto/venv
sudo pip install -r mezoappsingle/requirements.txt
cd mezoappsingle/mezoapp/
sudo ufw allow 8000
python3.12 manage.py migrate
python3.12 manage.py runserver 0.0.0.0:8000