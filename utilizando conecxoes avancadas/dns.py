import socket
import dns.resolver

dominio = input("Alvo: ")
brute = {"ns1","ns2","ns3","ns4","www","ftp","intranet","mail"}

for nome in brute:
    DNS = nome + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass

dominio = input("Alvo: ")
with open("bruteforce.txt","r") as arquivo:
    bruteforce = arquivo.readlines()

for nome in bruteforce:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass

dominio = input("Alvo: ")
registros = ["AAAA","A","MX","NS"]
for registro in registros:
    resultado = dns.resolver.query(dominio,registro,raise_on_no_answer=False)
    if resultado.rrset is not None:
        print(resultado.rrset)