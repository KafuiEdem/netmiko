"""
Challenge #1
Create a Python script that connects to a Cisco Router using SSH and Netmiko. 
The script should execute the show arp command in order to display the ARP table.
Print out the output of the command.
"""
from netmiko import ConnectHandler

cisco_device = {

    "host":"192.168.123.2",
    "port":"22",
    "username":"edem",
    "password":"cisco",
    "secret":"cisco",
    "device_type":"cisco_ios",
    "verbose":True
}

connection = ConnectHandler(**cisco_device)
print(f"Connecting to {cisco_device['host']}")
#entering into the enable mode
prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()
    output = connection.send_command("sh run")
    mode = connection.check_config_mode()
    print(output)
    print(mode)
#closing the connection
connection.disconnect()