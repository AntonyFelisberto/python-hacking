import os

ip = "127.0.0.1"

ping_cmd = f"ping 127.0.0.1"
exit_code = os.system(ping_cmd)
print(exit_code)

ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
exit_code = os.system(ping_cmd)
print(exit_code)

os.system("ping -c 1 -w 2 192.168.0.1 > /dev/null 2>&1")