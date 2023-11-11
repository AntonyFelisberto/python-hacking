import ssl,socket

def modelo_um():
    host = "https://medium.com/labhacker"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockSSL = ssl.wrap_socket(sock)
    sockSSL.connect((host,443))
    sockSSL.send("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n"%host)
    print(sockSSL.recv(1024))

def modelo_dois():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(("www.google.com",80))
    mysock.send(b"HEAD / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        print(data)

    mysock.close()

modelo_dois()