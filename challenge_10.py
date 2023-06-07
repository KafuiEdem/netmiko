"""
Challenge #10
Create a Python script that connects to a Cisco Router using SSH and Netmiko and executes all the commands from this file.
Note: Try to execute the commands by a single method call.
"""

from netmiko import ConnectHandler

#getting the device
device = {
    "host":"192.168.123.2",
    "username":"edem",
    "secret":"cisco",
    "password":"cisco",
    "verbose":True,
    "device_type":"cisco_ios"
}


connection = ConnectHandler(**device)

if ">" in connection.find_prompt():
    connection.enable()

if not connection.check_config_mode():
    connection.config_mode()

file = connection.send_config_from_file("data_serialization\\netmiko_files\\rip.txt")

print(file)
connection.disconnect()