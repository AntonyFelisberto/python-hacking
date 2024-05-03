import platform
import os
from datetime import datetime

def import_addresses():
    lines = []
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "\\files\\addresses.txt","r")
    for line in f:
        line = line.strip()
        lines.append(line)
    return lines

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "\\pinger.log", "a")
    f.write(message)
    f.close()

def ping_address(ip_address):
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -c 1 -w 2 {ip_address} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip_address} > /dev/null 2>&1"

    exit_code = os.system(ping_cmd)
    print(f"{ip}: {exit_code}")

ip_addresses = import_addresses()

for ip in ip_addresses:
    exit_code = ping_address(ip)

    if exit_code == 0:
        write_log(f"{ip} is online")
        print(f"{ip} is online")
    else:
        write_log(f"{ip} is offline")
        print(f"{ip} is offline")