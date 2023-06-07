"""
Challenge #8
Create a Python script that connects to a Cisco Router using SSH and Netmiko. 
The script should create an ACL (access control list) by executing the following 3 commands:
access-list 101 permit tcp any any eq 80
access-list 101 permit tcp any any eq 443
access-list 101 deny ip any any
Note: Try to execute the commands by a single method call.
Are you stuck? Do you want to see the solution to this exer
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

#connecting to the remote device
print(f"Connecting to host {device['host']}")
connection = ConnectHandler(**device)

commands = ["access-list 101 permit tcp any any eq 80","access-list 101 permit tcp any any eq 443","access-list 101 deny ip any any"]

if ">" in connection.find_prompt():
    connection.enable()

if not connection.check_config_mode():
    connection.config_mode()

for command in commands:
    output = connection.send_config_set(command)
    print(output)
