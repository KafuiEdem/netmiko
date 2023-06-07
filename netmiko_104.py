from netmiko import ConnectHandler
import threading
import time

start = time.time()
def backup(device):
    #getting the connection
    connection = ConnectHandler(**device)
    print(f"Connecting to {device['host']}")
    connection.enable()

    output = connection.send_command("show run")

    #getting the device hostname
    hostname = connection.find_prompt()
    hostname = hostname[0:-1]
    with open(f"data_serialization\\netmiko_files\{hostname}-backup.txt","w") as backup:
        backup.write(output)
    
    print(f"Closing connection to {device['host']}")
    connection.disconnect()
    print("#"*30)


with open("data_serialization\\netmiko_files\devices.txt") as f:
    devices = f.read().splitlines()

device_list = list()

thread = list()
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
    th = threading.Thread(target=backup,args=(cisco_device,))
    thread.append(th)

for th in thread:
    th.start()

for th in thread:
    th.join()

end = time.time()
print(f"Excutiong time {end-start}")