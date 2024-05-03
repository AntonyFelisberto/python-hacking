from socket import *

servidor = "127.0.0.1"  #endereço do servidor
port = 43210

obj_socket = socket(AF_INET,SOCK_DGRAM)
obj_socket.connect((servidor,port))
saida = ""

while saida!="X":
    msg = input("sua mensagem: ")
    obj_socket.sendto(msg.encode(),(servidor,port))
    dados,origem = obj_socket.recvfrom(65535)
    print("resposta do servidor",dados.decode())
    saida = input("digite X para sair ").upper()

obj_socket.close()