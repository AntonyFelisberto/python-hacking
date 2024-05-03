from socket import *

servidor = "127.0.0.1"  #endereço do servidor
port = 43210

obj_socket = socket(AF_INET,SOCK_STREAM)
obj_socket.bind((servidor,port))
obj_socket.listen(2)    #quantidade de clientes que a aplicação necessita

msg = bytes(input("Digite algo: "),"utf-8")
obj_socket = socket(AF_INET,SOCK_STREAM)
obj_socket.connect((servidor,port))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("recebemos ",resposta)
obj_socket.close()