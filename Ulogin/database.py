import sqlite3
class UserBase():
    
    def connectDatabase(self,databaseName):
        self.conn = sqlite3.connect(databaseName+'.db')
