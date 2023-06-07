from netmiko import ConnectHandler

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
print("Entering the enable mode")

connection.enable()

command = ["int loopback 0","ip address 1.1.1.1 255.255.255.255","exit","username netmiko secret cisco"]

connection.send_config_set(command)
print(connection.find_prompt())
print("closing the connection")
connection.send_command("wri")
connection.disconnect()