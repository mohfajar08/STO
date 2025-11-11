from utility import welcome_screen, main_menu
from notification import notify_user_tasks
from account import login, register_account
import os

if __name__ == "__main__":
    o = os.name
    match os.name:
        case "nt" : os.system("cls")

def main():
    welcome_screen()
    while True:
        print("\nPilih Menu:")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        cmd = input("Pilih (1-3): ")
        if cmd == "1":
            register_account()
        elif  cmd == "2":
            user = login()
            if user:
               notify_user_tasks(user)
            main_menu(user)
        elif cmd == "3":
            print("Keluar program. Bye.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
