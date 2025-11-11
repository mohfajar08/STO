import const
from models.user import User

WIDTH = 60
INNER = WIDTH - 6

def view_menu():
    line()
    print("View Menu")
    line()
    print('''1. Lihat Statistik Akun
2. Melihat daftar tugas (view)
3. Mencari task berdasarkan Judul
4. Melihat daftar task yang dihapus
5. Logout / ganti akun
''')
    viewMenu = input("Choose menu (1-5): ")
    line()
    return viewMenu

def greeting_prompt(title):
    line()
    center(title)
    line()
    center("Smart Task Organizer")
    line()
    space()
    
def exit_prompt():
    line()
    center("Thankyou for using Smart Task Organizer")
    line()
    
def account_menu():
    line()
    print("Account Menu")
    line()
    print('''1. Register
2. Login
3. Exit''')
    accountMenu = input("Choose menu (1-3): ")
    line()
    return accountMenu

def create_account_prompt():
    print("Input your Username & Password")
    username = input("New Username: ")
    password = input("New Password: ")
    user = User(username, password)
    return user

def log_account_prompt():
    while True:
        print("Input your Login Username & Password")
        username = input("Username: ")
        password = input("Password: ")
        return username, password

def line():
    print(const.H_SEPARATOR * WIDTH)
    
def center(text):
    t = str(text)[:INNER]
    pad = max(0, INNER - len(t))
    left = pad // 2
    right = pad - left
    print(const.V_SEPARATOR + (" " * left) + t + (" " * right) + const.V_SEPARATOR)

def line():
    print(const.H_SEPARATOR * WIDTH)
    
def space(n=1):
    for _ in range(max(1, n)):
        print()