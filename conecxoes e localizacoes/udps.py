from socket import *

servidor = "127.0.0.1"  #endereço do servidor
port = 43210

obj_socket = socket(AF_INET,SOCK_DGRAM)
obj_socket.bind((servidor,port))
print("Servidor pronto")

while True:
    dados,origem = obj_socket.recvfrom(65535)
    print("origem ",origem)
    print("dados ",dados.decode())
    resposta = input("Digite a resposta ")
    obj_socket.sendto(resposta.encode(),origem)

obj_socket.close()