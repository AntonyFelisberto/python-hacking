from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    print(f"Key :{key.decode()}")
    
def encrypt(plain_text,key):
    plain_text = plain_text.encode()
    key = key.encode()
    cipher_text = Fernet(key).encrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(plain_text,key):
    plain_text = plain_text.encode()
    key = key.encode()
    cipher_text = Fernet(key).decrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

enc_key = ""
method = input("choose one method: Create Key(c),Encrypt(e), decrypt(d): ")
method = method[0].lower()

if method == "c":
    create_key()
elif method == "e":
    plain_text = input("message to encrypt: ")
    enc_key = input("encryption key: ")
    cipher_text = encrypt(plain_text,enc_key)
    print(cipher_text)
elif method == "d":
    plain_text = input("message to encrypt: ")
    enc_key = input("encryption key: ")
    plain_text = decrypt(plain_text,enc_key)
    print(plain_text)
else:
    print("wrong choice")

