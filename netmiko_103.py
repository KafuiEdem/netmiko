from netmiko import ConnectHandler

with open("data_serialization\\netmiko_files\devices.txt","r") as f:
    devices = f.read().splitlines()

device_list = list()

for ip in devices:

    cisco_device = {
        "host": ip,
        "port":"22",
        "username":"edem",
        "password":"cisco",
        "device_type":"cisco_ios",
        "secret":"cisco",
        "verbose":True
        }
    device_list.append(cisco_device)
#getting the connection

for device in device_list:
    connection = ConnectHandler(**device)
    print("Entering enable mode...")
    connection.enable()
    #taking file 
    file = input(f"Enter configuation file (use a valid path) for {device['host']}:")
    print(f"Sending configuration {file} to {device['host']}")
    connection.send_config_from_file(file)
    print("Closing connection")
    connection.disconnect()
    print("#"*30)