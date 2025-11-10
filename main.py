import os
import sys
import utility
from controllers.user_controller import register,login 

if __name__ == "__main__":
    o = os.name
    match os.name:
        case "nt" : os.system("cls")

utility.greeting_prompt()
while True:
    chooseMenuAcc = utility.account_menu()
    os.system("cls")
    match chooseMenuAcc:
        case "1":
            user = utility.create_account_prompt()
            register(user)
        case "2":
            username,password = utility.log_account_prompt()
            login(username,password)
            break
        case "3": 
            utility.exit_prompt()
            sys.exit(0)
        case _:
            print("Invalid")
            continue
  