import crypt

def test_password(hash_password,algorithm_salt,plaintext):
    crypted_password = crypt.crypt(plaintext,algorithm_salt)
    if hash_password == crypted_password:
        return True
    return False

hash_password = ""
algorithm_salt = ""

for password in range(100000):
    result = test_password(hash_password,algorithm_salt,str(password))
    if result:
        print(f"Match found {password}")
        break