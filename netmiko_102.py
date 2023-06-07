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
print("Entering enable mode...")
connection.enable()

print("Sending config from a file")
connection.send_config_from_file("data_serialization\\netmiko_files\ospf.txt")


print("Closing connection")
connection.disconnect()