from Settings.storage import load_data, save_data

def buat_akun():
    data = load_data()
    user = input("Username baru: ")
    if user in data['akun']:
        print("Username telah terdaftar!\n")
        return
    
    pw = input("Password baru: ")
    data['akun'][user] = save_data(data)
    print("Akun berhasil dibuat!\n")
    return user

def login():
    data = load_data()
    user = input("Username: ")
    pw = input("Password: ")
    if user in data['akun'] and data['akun'][user]['password'] == pw:
        print(f"Selamat datang {user} di Smart Task Organizer!\n")
        return user
    else:
        print("Username atau password anda salah!\n")
        return