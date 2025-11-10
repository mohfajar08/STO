import re

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
    

# "database" untuk menyimpan task
database_task = []

def buat_task_baru():
    print("=== Buat Task Baru ===")

    # Validasi ID
    while True:
        id = input("Masukkan ID (huruf/angka saja): ")
        if re.fullmatch(r"[A-Za-z0-9]+", id):
            break
        else:
            print("❌ ID hanya boleh berisi huruf dan angka!")

    # Judul bebas tapi tidak boleh kosong
    while True:
        judul = input("Masukkan judul task: ")
        if judul.strip() != "":
            break
        else:
            print("❌ Judul tidak boleh kosong!")

    # Deskripsi opsional
    deskripsi = input("Masukkan deskripsi (opsional): ")

    # Validasi tingkat kesulitan
    while True:
        kesulitan = input("Masukkan kesulitan (Mudah/Sedang/Sulit): ")
        if kesulitan.lower() in ["mudah", "sedang", "sulit"]:
            break
        else:
            print("❌ Pilih hanya: Mudah / Sedang / Sulit")

    # Validasi deadline format YYYY-MM-DD
    while True:
        deadline = input("Masukkan deadline (contoh 2025-11-15): ")
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", deadline):
            break
        else:
            print("❌ Format harus YYYY-MM-DD!")

    # Simpan data ke database_task
    task_baru = [id, judul, deskripsi, kesulitan, deadline]
    database_task.append(task_baru)

    # Output
    print("\n✅ Task berhasil ditambahkan!")
    print("Detail task:")
    print(f"- ID: {id}")
    print(f"- Judul: {judul}")
    print(f"- Deskripsi: {deskripsi}")
    print(f"- Kesulitan: {kesulitan}")
    print(f"- Deadline: {deadline}")

# Contoh jalankan program
# buat_task_baru()
