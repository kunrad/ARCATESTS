#!/bin/bash

#update the centos server
yum upgrade -y
yum --enablerepo=extras install epel-release -y

#install docker 
yum install docker-io -y
chkconfig docker on
printf '\nDocker Installed Successfully'

#add a vagrant user to the docker group
sudo groupadd docker
sudo usermod -a -G docker vagrant

#install docker compose

sudo yum install python-pip -y
sudo pip install docker-compose 
printf '\nDocker-Compose Installed Successfully'

#reboot the system
/sbin/reboot
