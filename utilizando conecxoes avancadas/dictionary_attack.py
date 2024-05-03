import crypt
import os

def test_password(hash_password,algorithm_salt,plaintext):
    crypted_password = crypt.crypt(plaintext,algorithm_salt)
    if hash_password == crypted_password:
        return True
    return False

def read_dictionary(dictionary_file):
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "\\" + dictionary_file,"r")
    message = f.read()
    return message

password_dict = read_dictionary("arquivos\\files\\arquivos.txt")
hash_password = input("say the hash password: ")
algorithm_salt = input("say the algorithm salt: ")

for password in password_dict.splitlines():
    result = test_password(hash_password,algorithm_salt,str(password))
    if result:
        print(f"Match found {password}")
        break