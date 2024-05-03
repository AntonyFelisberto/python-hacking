import time

def python_two():
    import msfrpc
    
    client = msfrpc.Msfrpc({})
    client.login("msf","senha12345")
    sessao = client.call("console.create")
    comando = """use auxiliary/scanner/smb/smb_version
    set RHOSTS = 10.0.0.100
    exploit
    """

    client.call("console.write",[sessao["id"],comando])
    time.sleep(3)
    resultado = client.call("console.read",[sessao["id"]])

    while resultado["busy"]:
        resultado = client.call("console.read",[sessao["id"]])
        time.sleep(1)

    print(resultado["data"])
    client.call("console.destroy",[sessao["id"]])

def python_three():
    import xmlrpc.client  # The correct import for xmlrpc in Python 3

    # Metasploit RPC credentials
    rpc_host = "127.0.0.1"  # Replace with your Metasploit RPC host
    rpc_port = 55552  # Replace with your Metasploit RPC port
    rpc_user = "msf"  # Replace with your Metasploit RPC username
    rpc_pass = "senha12345"  # Replace with your Metasploit RPC password

    # Connect to Metasploit RPC
    client = xmlrpc.client.ServerProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:{rpc_port}/")

    # Create a new console
    console_id = client.console.create()["id"]

    # Run a Metasploit command
    command = """
    use auxiliary/scanner/smb/smb_version
    set RHOSTS 10.0.0.100
    exploit
    """

    # Write the command to the console
    client.console.write(console_id, command)

    # Wait for the command to complete (adjust sleep time as needed)
    time.sleep(3)

    # Read the output from the console
    resultado = client.console.read(console_id)

    while resultado["busy"]:
        resultado = client.console.read(console_id)
        time.sleep(1)

    print(resultado["data"])
    client.console.destroy(console_id)