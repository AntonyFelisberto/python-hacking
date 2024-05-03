import os
import platform

print(platform.system())
print(os.system("ping"))

ip = "127.0.0.1"

ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
exit_code = os.system(ping_cmd)
print(exit_code)

os.system("ping -c 1 -w 2 192.168.0.1 > /dev/null 2>&1")

for octet in range(254):
    ip = f"192.168.0.{octet+1}"
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -c 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    exit_code = os.system(ping_cmd)
    print(f"{ip}: {exit_code}")