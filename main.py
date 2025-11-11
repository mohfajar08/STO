import os
import sys
import utility
from controllers.user_controller import register,login

# if __name__ == "__main__":
#     o = os.name
#     match os.name:
#         case "nt" : os.system("cls")

utility.greeting_prompt("Welcome !!!")
while True:
    chooseMenuAcc = utility.account_menu()
    # os.system("cls")
    match chooseMenuAcc:
        case "1":
            user = utility.create_account_prompt()
            register(user)
            continue
        case "2":
            username,password = utility.log_account_prompt()
            infoLogin = login(username,password)
            if infoLogin is None:
                continue
        case "3": 
            utility.exit_prompt()
            sys.exit(0)
        case _:
            print("Invalid")
            continue
        
    utility.greeting_prompt("Main Program")

    i = 0
    print(f"Anda memiliki {i} task yang belum dikerjakan")
    while True:
        chooseMenuView = utility.view_menu()
        match chooseMenuView:
            case "1":
                print("Lihat Statistik Akun")
                continue
            case "2":
                print("Melihat daftar tugas (view)")
                continue
            case "3": 
                print("Mencari task berdasarkan Judul")
                continue
            case "4":
                print("Melihat daftar task yang dihapus")
                continue
            case "5":
                break
            case _:
                print("Invalid")
                continue