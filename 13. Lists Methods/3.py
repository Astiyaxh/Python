def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for s in string:
        if s in alphabet:
            temp = (alphabet.index(s) + 2) % 26
            encrypted += alphabet[temp]
    return encrypted
            


print(encrypt_message("abc"))
print(encrypt_message("ksajdfzzioertuiwetlh"))
print(encrypt_message("Hello Guys wellcome to zoo"))
