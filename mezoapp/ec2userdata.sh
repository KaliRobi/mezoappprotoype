

sudo yum update -y
sudo yum install python3 python3-pip git -y
sudo mkdir -p /var/www/mezoappproto
cd /var/www/mezoappproto
git clone https://github.com/KaliRobi/mezoappprotoype.git

sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate

