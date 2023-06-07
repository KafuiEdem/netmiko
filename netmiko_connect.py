from netmiko import Netmiko,ConnectHandler
from getpass import getpass

# connection = Netmiko(host="192.168.123.2",port="22",username="edem",password="cisco",device_type="cisco_ios")
# secret = getpass("Enter secret")
cisco_device = {
    "host":"192.168.123.2",
    "port":"22",
    "username":"edem",
    "password":"cisco",
    "device_type":"cisco_ios",
    "secret":"cisco",
    "verbose":True
    }
connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

if ">" in prompt:
    connection.enable()
print(prompt)
output = connection.send_command("show run")
print(output)

if not connection.check_config_mode():
    connection.config_mode()
connection.send_command("username u3 sec cisco")
connection.exit_config_mode()

connection.disconnect()