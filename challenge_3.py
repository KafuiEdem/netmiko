"""
    Challenge #3
Create a Python script that connects to a Cisco Router using SSH and Netmiko. 
The script should get the prompt, process it and then print the hostname part.
"""
from netmiko import ConnectHandler

device = {
    "host":"192.168.123.2",
    "username":"edem",
    "port":"22",
    "secret":"cisco",
    "password":"cisco",
    "device_type":"cisco_ios",
    "verbose":True,
}

#connecting to the remote device
print(f"Connecting to {device['host']}")
connection = ConnectHandler(**device)
prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()
username = connection.find_prompt()
username = username[0:-1]
print(f"The hostname for the {device['host']} is {username}")

connection.disconnect()
