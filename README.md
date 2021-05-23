Prerequisites

install the latest vagrant and virtual box. You can download from the respective websites or install using something like brew

brew cask install virtualbox vagrant

Running the VM
Run:

vagrant up

Testing Docker on the VM

Login to the VM using vagrant ssh
check to see if docker is running by using ps -ef | grep docker. If it isnt you might need to reboot the vm


# Start the docker-compose 
docker-compose up -d

# PYTHON SCRIPT TO START AND STOP EC2 INSTANCE
START and STOP EC2 Instance

# Start EC2 instance
python3 start_stop_ec2.py -u

# Stop EC2 instance
python3 start_stop_ec2.py -d

Requirements:
# install boto3

pip install boto3 botocore

or 

pip3 install boto3 botocore

EC2 Instance ID
Enter your EC2 ID in a file with the name instance_id.txt and save this file in your Users/home folder:

/home/[username]/instance_id.txt // Linux

AWS Credentials
Check your AWS Credentials in your home/users folder:

Linux:
/home/[username]/.aws

If you have not installed your aws use the command below

aws configure

Enter

your AWS Access Key ID and
your AWS Secret Access Key.
As default region name enter your Availability Zone (AZ) and
use "json" as default output format.