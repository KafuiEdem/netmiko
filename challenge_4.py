"""
    Challenge #4
Create a Python script that connects to a Cisco Router using SSH and Netmiko. 
The script should execute the show ip int brief and show run commands.
"""
from netmiko import ConnectHandler

#getting a place holder for remote device connection
device = {
    "host":"192.168.123.2",
    "username":"edem",
    "secret":"cisco",
    "port":"22",
    "password":"cisco",
    "device_type":"cisco_ios",
    "verbose":True
}

#connecting to the remote device
print(f"Connecting to the remote device {device['host']}")
connection = ConnectHandler(**device)
int_brief = connection.send_command("sho ip int br")
#checking the current prompt
if ">" in connection.find_prompt():
    connection.enable()
show_run = connection.send_command("show run")

print("#"*60)
print(int_brief)
print("#"*60)
print(show_run)