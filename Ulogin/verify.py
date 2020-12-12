import pyAesCrypt
import os
class Verify():
    def __init__(self):
        self.bufferSize = 64*1024

    def verifyLogin(self,userName,userPassword):
        try:
            pyAesCrypt.decryptFile(userName+".db.crypt",userName+".db",userPassword,self.bufferSize)
        except:
            return False
        else:
            os.remove(userName+".db")
            return True