import os
from database import UserBase
class menu():
    def _getDetails(self):
        self._userName = input("Enter your UserName: ")
        self._userPassword = input("Enter your Password: ")

    def _mainMenu(self):
        while True:
            os.system('cls')    
            print("""
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
            os.system('cls')
            # call show all Password function to display aal the passwords 
            print("""
            2. Go back to previous menu""")
            ch = int(input("Enter Your Choice: "))
            if ch == 2:
                break


    def _loginSubMenu(self):
        while True:
            os.system('cls')
            print("""
            1. Show All Passwords
            2. Add New Password
            3. Remove New Password
            4. Change Master Password
            5. Delete Account
            6. Logout""")
            choice= int(input("Enter Your Choice : "))
            if choice == 1:
                self.showAllPassMenu()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("Logging Out")
                print("Press Enter to Continue...")
                input("")
                break

    def _loginMenu(self):
        self._getDetails()
        if UserBase().verify(self._userName,self._userPassword) == True:
            self._loginSubMenu()
        else :
            print("Incorrect Credentials")
            print("Press Enter to go back to Main Menu")
            input(" ")

    def _createMenu(self):
        while True:
            os.system('cls')
            print("""
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