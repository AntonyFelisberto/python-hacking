import platform
import getpass
from datetime import datetime

print("maquina ",platform.node())
print("arquitetura ",platform.architecture())
print("sistema ",platform.system())
print("versao so ",platform.release())
print("processador ",platform.processor())
print("python ",platform.python_version())

print(datetime.now())
print(datetime.now().month)

print(getpass.getuser())
print(getpass.getpass("digite sua senha "))
user = getpass.getuser()
passw = getpass.getpass("digite sua senha ")