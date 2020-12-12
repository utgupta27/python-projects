import os
from database import UserBase
class menu():
    def _getDetails(self):
        self._userName = input("Enter your UserName: ")
        self._userPassword = input("Enter your Password: ")

    def _getData(self):
        self.siteName = input("Enter the Name of Website: ")
        self.siteUserName = input("Enter the Website Username : ")
        self.sitePassword = input("Enter tha website Password: ")

    def _mainMenu(self):
        while True:
            os.system('clear')    
            print("""
        *********MAIN MENU**********
            1. Login (Existing User)
            2. Create New Account
            3. Exit""")
            choice = input("Enter Your choice : ")
            if choice == "1":
                self._loginMenu()
            elif choice == "2":
                self._createMenu()
            elif choice =="3":
                break

    def showAllPassMenu(self):
        while True:
            os.system('clear')
            UserBase().showAllPassword(self._userName,self._userPassword)
            print("""
            2. Go back to previous menu""")
            ch = int(input("Enter Your Choice: "))
            if ch == 2:
                break

    def addMenu(self):
        while True:
            os.system('clear')
            print("""
            ## Password Added Successfully ##
            1. Add More Password
            2. Go back to previous menu""")
            ch = int(input("Enter Your Choice: "))
            if ch == 1:
                self._getData()
                UserBase().addEntry(self._userName,self._userPassword,self.siteName,self.siteUserName,self.sitePassword)
            elif ch == 2:
                break

    def _loginSubMenu(self):
        while True:
            os.system('clear')
            print("\t**********"+self._userName+"*********")
            print("""
            1. Show All Passwords
            2. Add New Password
            3. Remove New Password
            4. Change Master Password
            5. Delete Account
            6. Logout\n""")
            choice= int(input("Enter Your Choice : "))
            if choice == 1:
                self.showAllPassMenu()
            elif choice == 2:
                self._getData()
                self.addMenu()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("## Logging Out ##")
                print("Press Enter to Continue...")
                input("")
                break

    def _loginMenu(self):
        self._getDetails()
        if UserBase().verify(self._userName,self._userPassword) == True:
            self._loginSubMenu()
        else :
            print("\n## Incorrect Credentials ##")
            print("Press Enter to go back to Main Menu...")
            input(" ")

    def _createMenu(self):
        while True:
            os.system('clear')
            print("""
        *********NEW USER**********
            1.Enter New Credentials
            2.Back to Main Menu""")
            choice =  int(input("Enter Your Choice :"))
            if choice == 1:
                self._getDetails()
                UserBase().createUserAccount(self._userName,self._userPassword)
            elif choice==2:
                break        

if __name__ == "__main__":
    menuobj = menu()
    menuobj._mainMenu()