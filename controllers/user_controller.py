
akun_list = []

def login(username, password):
        for akun in akun_list:
            if akun.username == username and akun.password == password:
                return akun 
        return None

def register(user):
    if user.username in (a.username for a in akun_list):
        print("Username sudah terdaftar.")
        return
    elif user.password == "" or user.username == "":
        print("Password / username tidak boleh kosong.")
        return
    akun_list.append(user)
    print(f"Akun {user.username} berhasil dibuat.")