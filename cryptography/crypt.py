from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_Key():
    return open("key.key","rb").read()

write_key()
key=load_Key()
message="Utsav Gupta is my name".encode()
print(message)
f=Fernet(key)
encrypted= f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)

print(decrypted)