import socket

resp = 'S'
while resp == "S":
    url = input("digite uma url: ")
    ip = socket.gethostbyname(url)
    print("o ip da url é "+ip)
    resp = input("digite S para continuar: ").upper()