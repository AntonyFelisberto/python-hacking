import nmap

target_address = "192.168.0.51"

port_start = 75
port_end = 100

scanner = nmap.PortScanner()
print(f"scanning {target_address}")

for port in range(port_start, port_end + 1):
    result = scanner.scan(target_address,str(port))
    port_status = result["scan"][target_address]["tcp"][port]["state"]
    print(f"\tPort: {port} is {port_status}")