"""
Challenge #2
Change the solution from the previous challenge so that the Python script reads the IP address of the device, 
the port, the username, and the password from a file.
The file contains the login information on a single line in the format: IP:PORT:USERNAME:PASSWORD:ENABLE_PASSWORD
Example: 10.1.1.10:22:u1:cisco:cisco
"""
from netmiko import ConnectHandler

#reading information for file

with open("data_serialization\\netmiko_files\credentials.txt","r") as f:
    credentail = f.read().splitlines()

#connecting to the network device
device = {
    "host":credentail[0],
    "username":credentail[1],
    "password":credentail[2],
    "port":credentail[3],
    "secret":credentail[4],
    "device_type":"cisco_ios",
    "verbose":True,
}
#connecting to the ssh device
connection = ConnectHandler(**device)

print(f"Connecting to device {device['host']}")

connection.enable()
prompt = connection.find_prompt()
username = prompt[0:-1]

print(f"Connected to cisco rotuer with hostname {username}")

connection.disconnect()