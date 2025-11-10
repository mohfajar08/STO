import re
from datetime import datetime

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
data_user = {}

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

database_task = []
data_user = {}
def edit_tasks(username):
    print("=== EDIT/UPDATE TASKS ===")
    if not data_user:
                print(f"User {username} tidak ditemukan.\n")
                return
    tugas = database_task

    if not tugas:
                print("Tidak ada tugas untuk diedit atau update.\n")
                return
    
    for i, t in enumerate(tugas, start=1):
                status = "Selesai" if t["selesai"] else "Belum selesai"
                print(f"{i}. {t['judul']} ({t['tingkat']}) - Deadline: {t['deadline']} - {status}")
    try:
        pilihan = int(input("\nMasukkan nomor tugas yang ingin diedit atau update: ")) - 1
        if 0 <= pilihan < len(tugas):
            t = tugas[pilihan]
            print(f"\nMengedit tugas '{t['judul']}'...\n")

            judul_baru = input("Judul baru: ").strip() or t["judul"]
            desk_baru = input("Deskripsi baru: ").strip() or t["deskripsi"]
            tingkat_baru = input("Tingkat baru: ").strip() or t["tingkat"]
            deadline_baru = input("Deadline baru (YYYY-MM-DD): ").strip() or t["deadline"]

            # Validasi format tanggal
            try:
                datetime.strptime(deadline_baru, "%Y-%m-%d")
            except ValueError:
                print("⚠ Format tanggal tidak valid, perubahan dibatalkan.\n")
                return

            status_baru = input("Apakah tugas anda telah dikerjakan? (y/n, kosong = tidak diubah): ").lower().strip()
            if status_baru == 'y':
                selesai_baru = True
            elif status_baru == 'n':
                selesai_baru = False
            else:
                selesai_baru = t['selesai']

            tugas[pilihan] = {
                'judul': judul_baru,
                'deskripsi': desk_baru,
                'tingkat': tingkat_baru,
                'deadline': deadline_baru,
                'selesai': selesai_baru
            }

            print(f"Tugas '{judul_baru}' berhasil diperbarui.\n")
        else:
            print("Nomor tugas tidak valid atau tidak ditemukan!\n")
    except ValueError:
        print("Masukkan angka yang valid!\n")