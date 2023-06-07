"""
Challenge #7
Create a Python script that connects to a Cisco Router using SSH and Netmiko. 
The script should create a user and then save the running configuration of the router.
To create a user execute: username admin secret topsecret command in the global configuration mode.
"""
from netmiko import ConnectHandler
from datetime import datetime
import time
from getpass import getpass

password = getpass("Enter password:")
secret = getpass("Enter secret")

device = {
    "host":"192.168.123.2",
    "username":"edem",
    "secret":secret,
    "port":"22",
    "password":password,
    "device_type":"cisco_ios",
    "verbose":True
}
#connecting to the remote device
print(f"Connecting to the remote device {device['host']}")
connection = ConnectHandler(**device)
if ">" in connection.find_prompt():
    connection.enable()
if not connection.check_config_mode():
    connection.config_mode()
connection.send_command("username admin secret topsecret")
connection.exit_config_mode()
output = connection.send_command("sh run")

#get the hostname

hostname = connection.find_prompt()
hostname = hostname[0:-1]
# writing the configs to file
with open(f"data_serialization\\netmiko_files\{hostname}-runing_config.txt","w") as f:
    f.write(output)
print("closing the connection")
print(hostname)
connection.disconnect()