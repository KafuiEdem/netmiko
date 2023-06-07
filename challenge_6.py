"""
Challenge #6
Change the solution from the previous challenge so that the script will prompt for both the user that authenticates and the enable passwords securely (use getpass module).
Run the script in the terminal (you can not run it in PyCharm).
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

#sending command to the remote device
int_brief = connection.send_command("sh ip int br")

if ">" in connection.find_prompt():
    connection.enable()

show_run = connection.send_command("show run")

#connecting the remote device hostname
hostname = connection.find_prompt()
hostname = hostname[0:-1]

#storing the output of the show command
output = [show_run,int_brief]

#getting the date
now = datetime.now()
year = now.year
month = now.month
time_s = now.strftime("%H-%M-%S")
day = now.day

filename = f"{hostname}_{year}_{month}_{day}-{time_s}"

for i in output:

    with open(f"data_serialization\\netmiko_files\{filename}_{i[len(output)]}.txt","w") as f:
        f.write(i)
    

print(f"Closing the remote connection {device['host']}")
connection.disconnect()