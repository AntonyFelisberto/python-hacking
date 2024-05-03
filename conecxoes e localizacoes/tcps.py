from socket import *

servidor = "127.0.0.1"  #endereço do servidor
port = 43210

obj_socket = socket(AF_INET,SOCK_STREAM)
obj_socket.bind((servidor,port))
obj_socket.listen(2)    #quantidade de clientes que a aplicação necessita

print("aguardando")

while True:
    con,cliente = obj_socket.accept()   #retorna uma tupla ao conectar com um cliente, fica travado aqui até receber uma conect
    print("conectado ",cliente)
    while True:
        msg = str(con.recv(1024))   #quantidade e mensagem que voce recebeu
        print("recebendo: ", msg)
        msg_enviada = b"ola cliente"
        con.send(msg_enviada)
        break
    con.close()