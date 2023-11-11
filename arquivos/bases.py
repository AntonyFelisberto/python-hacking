import base64

def encode_data(plain_text):
    plain_text = plain_text.encode()
    cipher_text = base64.b64encode(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text

def decode_data(cipher_text):
    plain_text = base64.b64decode(cipher_text)
    plain_text = plain_text.decode()
    return plain_text

method = input("do you wish to encode or decode (e/d): ")
message = input("say the message: ")

if method[0] == "e":
    print(encode_data(message))
elif method[0] == "d":
    print(decode_data(message))
else:
    print("wrong method")