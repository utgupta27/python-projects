import sqlite3
import os
from encrypt import Encrypt
class UserBase(): 

    def getdir(self):
        return os.getcwd()

    def verify(self,userName,userPassword):
        try:
            Encrypt().decryptdata(userName,userPassword)
        except:
            return False
        else:
            path = self.getdir() + '/'+ userName + '.db'
            os.remove(path)
            return True

    def createUserAccount(self,userName,userPassword):
        path = self.getdir() + '/'+ userName + '.db'
        sqlite3.connect(userName+'.db')
        Encrypt().encryptdata(userName,userPassword)
        os.remove(path)

    def  ShowAllPassword(self):
        """
        docstring
        """
        pass

    def displaySearchedPassword(self):
        """
        docstring
        """
        pass
        


