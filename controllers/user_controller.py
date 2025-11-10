
akun_list = []

def login(username, password):
     for akun in akun_list:
        if akun.username == username and akun.password == password:
            print(f"Selamat datang, {username}!")
            return akun 
        print("Username atau password salah.")
        return None

def register(anu):
    if anu.username in (a["username"] for a in akun_list):
        print("Username sudah terdaftar.")
        return
    akun_list.append(anu)
    print(f"Akun {anu.username} berhasil dibuat.")
    print(akun_list)