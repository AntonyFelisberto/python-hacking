import requests
import hashlib

def check_ihavebeenpawned(sha_prefix):
    pwnd_dict = {}
    request_uri = "https://api.pwnedpasswords.com/range/"+sha_prefix
    r = requests.get(request_uri)
    pwnd_list = r.text.split("\r\n")
    for pwnd_pass in pwnd_list:
        pwnd_hash = pwnd_pass.split(":")
        pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]
    return pwnd_dict

password = input("What is the password: ")
sha_password = hashlib.sha1(password.encode()).hexdigest()
sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:].upper()
pwnd_dict = check_ihavebeenpawned(sha_prefix)

if sha_prefix in pwnd_dict.keys():
    print(f"password has been compromised {pwnd_dict[sha_postfix]} times")
else:
    print("password has not been compromised")