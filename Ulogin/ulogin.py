import os
from verify import Verify
from database import UserBase
from encrypt import Encrypt

class Ulogin():
    
    def getDetails(self):
        self.userName = input("Enter Your Username : ")
        self.userPassword = input("Enter yout Password : ")

    def loginMenu(self):
        while True:
            os.system('cls')
            print("""
            *****Login Menu*****
                1.Show All Passwords
                2.Add Password
                3.Change Password
                4.Delete PAssword
                5.Logout
            """)
            choice=int(input("Enter Your Choice: "))
            if choice==1:
                pass
                # showAllPassword()
            elif choice==2:
                pass
                # addPassword()
            elif choice==3:
                pass
                # changePassword()
            elif choice==4:
                pass
                # deletePassword()
            elif choice==5:
                print("Logging out ...")
                # do everything before logging out
                # clear cache and encrypt all the decrypted data
                break

    def createMenu(self):
        while True:
            os.system('cls')
            print("""
            *****Create User Account*****
                1.Enter Credentials
                2.Goto previous Menu
            """)
            choice=int(input("Enter Your Choice: "))
            if choice==1:
                self.getDetails()
                obj = UserBase()
                obj.connectDatabase(self.userName)
                # create an encrypted database 
                encryptobj=Encrypt()
                encryptobj.encryptdata(self.userName,self.userPassword)
                print("Account created.\ngoto previous menu\nand login Again ...")
                input(" ")
            elif choice==2:
                break
            
    def changeCredentialsMenu(self):
        while True:
            os.system('cls')
            print("""
            *****Change Credentials*****
                1.
                2.go back to prevoius menu
            """)
            choice=int(input("Enter Your Choice: "))
            if choice==1:
                pass
            elif choice==2:
                break

    def deleteAccountMenu(self):
        while True:
            print("""
            *****Delete Account*****
                1.
                2.go back to prevoius menu
            """)
            choice=int(input("Enter Your Choice: "))
            if choice==1:
                pass
            elif choice==2:
                break


    def mainMenu(self):
        while True:
            os.system('cls')
            print("""
            *******MAIN MENU*******
                1.Login
                2.Create Account
                3.Change Credentials
                4.Delete Account
                5.Exit
            """)
            choice = int(input('Enter your choice: '))
            if choice==1:
                self.getDetails()
                v=Verify()
                if v.verifyLogin(self.userName,self.userPassword):
                    self.loginMenu()
                else:
                    print("Incorrect Credentials...")
                    input("Press Enter to Continue...")
            elif choice==2:
                self.createMenu()
            elif choice==3:
                self.changeCredentialsMenu()
            elif choice==4:
                self.deleteAccountMenu()
            elif choice==5:
                break

            
if __name__ == "__main__":
    obj=Ulogin()
    obj.mainMenu()