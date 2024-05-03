source_message = input("say the message to encrypt and decrypt: ")
source_message = source_message.lower()
final_message = ""

for letter in source_message:
    ascii_num = ord(letter)
    if ascii_num >= 97 and ascii_num <= 122:
        new_ascii = ascii_num + 13
        if new_ascii >= 122:
            new_ascii = new_ascii - 26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)

print("message covered")
print(final_message)