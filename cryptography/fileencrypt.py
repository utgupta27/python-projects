from cryptography.fernet import Fernet

def writekey():
    key=Fernet.generate_key()
    with open("key.key","wb") as target:
        target.write(key)

def loadKey():
    return open("key.key","rb").read()

def encryptfile(filename,key):
    f=Fernet(key)
    with open(filename,"rb") as target:
        fileData = target.read()
        encrypteddata = f.encrypt(fileData)
    with open(filename,"wb") as target:
        target.write(encrypteddata)

def decryptfile(filename,key):
    f=Fernet(key)
    with open(filename,"rb") as target:
        encrypteddata = target.read()
        fileData = f.decrypt(encrypteddata)
    with open(filename,"wb") as target:
        target.write(fileData)

def driver():
    #comment out the statements to do the particular task

    # writeKey()
    # key=loadKey()
    # encryptfile("data.txt",key)
    # decryptfile("data.txt",key)

if __name__ == "__main__":
    driver()