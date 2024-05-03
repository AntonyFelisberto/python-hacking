from ftplib import *

ftp = FTP('ftp.ibiblio.org')    #utilizando dominio aberto para testes
print(ftp.getwelcome())
ftp.quit()