#!/usr/bin/env python3

"""
start ec2 server
python 3.7
version 1.5.0.
author: Duru Chibuike
"""


import os
import sys
import time
import argparse
import boto3.ec2
from botocore.exceptions import ClientError

VERSION = '1.5.0'
ec2 = boto3.client('ec2')

class Mem:
    """
    Global Class pattern
    Declare globals here
    """
    instance_id = ""

def read_credentials():
    """
    Read the users credntials file 'instance_id.txt'
    This file should be located in the users home folder
    :return: The EC@ instance id
    """
    home_dir = os.path.expanduser('~')
    credentials_file_path = os.path.join(home_dir, "instance_id.txt")
    try:
        with open(credentials_file_path, 'r') as f:
            credentials = [line.strip() for line in f]
            return credentials
    except FileNotFoundError as e:
            print("Error Message: {0}".format(e))

def parse_arguments():
    """
    The options the user can choose (up, down, version)
    return The chosen option
    """
    parser = argparse.ArgumentParser("start_stop_ec2.py: \
    Start and Stop your EC2 instance. \n")
    parser.add_argument(
        '-u', '--up', help="Start the EC2 instance", action='store_true')
    parser.add_argument('-d', '--down',
                        help= "Stop the EC2 instance", action='store_true')
    parser.add_argument('-v', '--version', help="Display the current version", action='store_true')
    args = parser.parse_args()
    return args

def evaluate(args):    
    """
    Evaluate the given arguments
    :param args: The users input
    """
    if args.up:
        start_ec2()
    elif args.down: 
        stop_ec2()
    elif arg.version:
        print()
        print('This is version {0},'.format(VERSION))
    else:
        print("Mission argument! Type '-h' for available arguments.")

def start_ec2():
    """
    This code is from Amazons EC2 example.
    Do a dryrun first to verify permission
    Try to start the EC2 instance
    """
    print("___________________")
    print("Try to start the EC2 instance.")
    print("___________________")

    try:
        print("Start dey run...")
        ec2.start_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise 
        # Dry run succeeded, run start_instance without dryrun
        #                 
    try:
        print("Start instance without dry run...")
        response = ec2.start_instance(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
        fetch_public_ip()
    except ClientError as e:
        print(e)

def stop_ec2():
    """
    This code is from Amazon's EC2 example.
    Do a dryrun first to verify permissions.
    Try to stop the EC2 instance.
    """
    print("------------------------------")
    print("Try to stop the EC2 instance.")
    print("------------------------------")

    try:
        ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


def fetch_public_ip():
    """
    Fetch the public IP that has been assigned to the EC2 instance.
    :return: Print the public IP to the console.
    """
    print()
    print("Waiting for public IPv4 address...")
    print()
    time.sleep(16)
    response = ec2.describe_instances()
    first_array = response["Reservations"]
    first_index = first_array[0]
    instances_dict = first_index["Instances"]
    instances_array = instances_dict[0]
    ip_address = instances_array["PublicIpAddress"]
    print()
    print("Public IPv4 address of the EC2 instance: {0}".format(ip_address))


def main():
    """
    The entry point of this program.
    """
    credentials = read_credentials()
    Mem.instance_id = credentials[0]
    args = parse_arguments()
    sys.stdout.write(str(evaluate(args)))
    print()


if __name__ == '__main__':
    main()