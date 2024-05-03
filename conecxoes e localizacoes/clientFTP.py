from ftplib import *

ftp = FTP('ftp.ibiblio.org')    #utilizando dominio aberto para testes
print(ftp.getwelcome())
usuario = input("digite o usuario: ")   #deixe vazio para continuar
senha = input("digite a senha: ")   #deixe vazio para continuar
ftp.login(usuario,senha)
print("diretorio atual ",ftp.pwd())
ftp.cwd("pub")  #diretorio que qr acessar
print("diretorio corrente ",ftp.pwd())
print(ftp.retrlines("LIST"))
ftp.quit()