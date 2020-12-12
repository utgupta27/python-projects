import sqlite3
import os
from encrypt import Encrypt


class UserBase(): 

    def getdir(self):
        return os.getcwd()

    def removeTemp(self,userName):
        path = self.getdir() + '/'+ userName + '.db'
        os.remove(path)

    def removeOldDatabase(self,userName):
        path = self.getdir() + '/'+ userName + '.db.crypt'
        os.remove(path)


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
        # create a table inside tha database brfore encrypting it
        conn = sqlite3.connect(userName+'.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE USER(SITE CHAR(50),USERNAME CHAR(50),PASSWORD CHAR(50))''')
        conn.commit()
        conn.close()
        Encrypt().encryptdata(userName,userPassword)
        self.removeTemp(userName)

    def showAllPassword(self,userName,userPassword):
        Encrypt().decryptdata(userName,userPassword)
        self.removeOldDatabase(userName)
        conn = sqlite3.connect(userName+'.db')
        cursor = conn.cursor()
        query = "SELECT * FROM USER"
        result = cursor.execute(query)
        # result = cursor.fetchall()
        print("Website\t  \t\tUser ID \t \t\tPassword \n")
        for i in result:
            print(i[0],end='')
            print("\t->\t",end='')
            print(i[1],end='')
            print("\t->\t",end='')
            print(i[2],end='\n')
        conn.commit()
        conn.close()
        Encrypt().encryptdata(userName,userPassword)
        self.removeTemp(userName)

    def displaySearchedPassword(self):
        pass
        
    def addEntry(self,userName,userPassword,site,id,password):
        Encrypt().decryptdata(userName,userPassword)
        self.removeOldDatabase(userName)
        conn = sqlite3.connect(userName+'.db')
        cursor = conn.cursor()
        query = "INSERT INTO USER(SITE,USERNAME,PASSWORD) VALUES('"+site+"','"+id+"','"+password+"');"
        cursor.execute(query)
        conn.commit()
        conn.close()
        Encrypt().encryptdata(userName,userPassword)
        self.removeTemp(userName)
        
