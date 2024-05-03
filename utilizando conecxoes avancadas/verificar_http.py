import requests

hosts = "https://medium.com/labhacker"
metodos = ["GET","POST","OPTIONS","PUT","DELETE","TRACE","CONNECT","HEAD","PATCH"]
for metodo in metodos:
    resposta = requests.request(metodo,hosts)
    print(metodo,resposta.reason)