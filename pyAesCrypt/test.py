import pyAesCrypt
class encrypt():
    def __init__(self):
        self.bufferSize=64 * 1024

    def getDetails(self):
        self.userID = input("Enter your Username : ")
        self.userPassword = input("Enter Your Password : ")

    def encryptFile(self):
        pyAesCrypt.encryptFile(self.userID+".txt",self.userID+".txt.aes",self.userPassword,self.bufferSize)
    
    def decryptFile(self):
        pyAesCrypt.decryptFile(self.userID+".txt.aes",self.userID+".txt",self.userPassword,self.bufferSize)

def driver():
    enc = encrypt()
    enc.getDetails()
    enc.decryptFile()


if __name__ == "__main__":
    driver()