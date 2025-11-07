from datetime import datetime #tggu buat notifikasi baru jalan
from Settings.storage import load_data, save_data

def add_tugas(username):
    data = load_data()
    print("=== TAMBAHKAN TUGAS ===")
    judul = input("Judul: ")
    desk = input("Deskripsi tugas: ")
    tingkat = input("Level kesulitan (mudah/sedang/sulit): ")
    deadline = input("Deadline (YYYY-MM-DD): ")

    tugas = {
        'judul': judul,
        'deskripsi': desk,
        'tingkat': tingkat,
        'deadline': deadline,
        'selesai': False
    }
    if username not in data['tugas']:
        data['tugas'][username] = []
    data['tugas'][username].append(tugas)
    save_data(data)
    print('Tugas berhasil ditambahkan!\n')


def view_tugas(username):
    data = load_data()
    tugas = data['tugas'].get(username, [])
    if not tugas:
        print("Tidak ada tugas tersedia!")
        return
    
    print("\n=== LIHAT DAFTAR TUGAS ===")
    print("1. Lihat seluruh tugas yang BELUM dikerjakan")
    print("2. Cari tugas berdasarkan nama")
    print("3. Lihat tugas yang SUDAH dikerjakan (tugas lampau)")
    pilihan = input("Pilih (1/2/3): ")

    if pilihan == "1":
        undone = [t for t in tugas if not t["selesai"]]
        if not undone:
            print("Semua tugas sudah dikerjakan!")
        else:
            print("\nTugas yang belum dikerjakan:")
            for i, t in enumerate(undone, 1):
                print(f"{i}. {t['judul']} ({t['tingkat']}) dengan batas waktu {t['deadline']} - Belum selesai")
    elif pilihan == "2":
        keyword = input("Masukkan nama tugas yang ingin dicari: ").lower()
        found = [t for t in tugas if keyword in t["judul"].lower()]
        if not found:
            print("Tidak ada tugas dengan nama tersebut.\n")
        else:
            print("Hasil pencarian: \n")
            for i, t in enumerate(found, 1):
                status = "Selesai" if t["selesai"] else "Belum selesai"
                print(f"{i}. {t['judul']} ({t['tingkat']}) dengan batas waktu {t['deadline']} - {status}")
    elif pilihan == "3":
        done = [t for t in tugas if t["selesai"]]
        if not done:
            print("Belum ada tugas yang diselesaikan.\n")
        else:
            print("\nTugas yang sudah dikerjakan: \n")
            for i, t in enumerate(done, 1):
                print(f"{i}. {t['judul']} ({t['tingkat']}) dengan batas waktu {t['deadline']} - Selesai")
    else:
        print("Pilihan tidak valid.\n")


def delete_tugas(username):
    data = load_data()
    tugas = data['tugas'].get(username, [])
    print("=== HAPUS TUGAS ===")

    if not tugas:
        print("Tidak ada tugas untuk dihapus.\n")
        return
    
    for i, t in enumerate(tugas, 1):
        status = "Selesai" if t['selesai'] else "Belum selesai"
        print(f"{i}. {t['jududl']} ({t['tingkat']}) dengan batas waktu {t['deadline']} - {status}")

    try:
        i = int(i("Masukkan nomor tugas yang ingin dihapus: \n")) - 1
        if 0 <= i < len(tugas):
            konfirmasi = input(f"Apakah anda yakin ingin menghapus {tugas['judul']}? (y/n): ")
            if konfirmasi == 'y':
                deleted = tugas.pop(i)
                save_data(data)
                print(f"Tugas {tugas['judul']} telah berhasil dihapus.\n")
            else:
                print(f"Penghapusan {tugas['judul']} dibatalkan.\n")
        else:
            print("Nomor tugas tidak ditemukan!\n")
            return
    except ValueError:
        print("Masukkan angka yang valid!\n")


def edit_tugas(username):
    data = load_data
    tugas = data['tugas'].get(username, [])
    print("=== EDIT/UPDATE TUGAS ===")

    if not tugas:
        print("Tidak ada tugas untuk diedit atau update.\n")
        return
    
    for i, t in enumerate(tugas, i):
        status = "Selesai" if t['selesai'] else "Belum selesai"
        print(f"{i}. {t['jududl']} ({t['tingkat']}) dengan batas waktu {t['deadline']} - {status}")

    try:
        i = int(i("Masukkan nomor tugas yang ingin diedit atau update: ")) - 1
        if 0 <= i < len(tugas):
            t = tugas[i]
            print(f"Mengedit tugas {t['judul']}.\n")
            judul_baru = input("Judul baru: ") or t['judul']
            desk_baru = input("Deskripsi baru: ") or t['deskripsi']
            tingkatan_baru = input("Tingkatan baru: ") or t['tingkat']
            deadline_baru = input("Deadline baru (YYYY-MM-DD): ") or t['deadline']

            status_baru = input(f"Apakah {t['judul']} telah dikerjakan? (y/n, biarkan kosong untuk tidak mengubah): ")
            if status_baru == 'y':
                status_selesai = True
            elif status_baru == 'n':
                status_selesai = False
            else:
                status_selesai = t['selesai']

            tugas[i] = {
                'judul': judul_baru,
                'deskripsi': desk_baru,
                'tingkat': tingkatan_baru,
                'deadline': deadline_baru,
                'selesai': status_selesai
            }
            save_data(data)
            print(f"Tugas {t['judul']} berhasil diperbarui!\n")
        else:
            print("Nomor tugas tidak ditemukan!\n")
            return
    except ValueError:
        print("Masukkan angka yang valid!\n")


def notifikasi(username):
    data = load_data
    tugas = data['tugas'].get(username, [])
    undone = [t for t in tugas if not t['selesai']]
    print(f"Anda memiliki {len(undone)} tugas yang belum dikerjakan!")


def statistik(username):
    data = load_data
    tugas = data['tugas'].get(username, [])
    print("=== STATISTIK TUGAS ===")

    if not tugas:
        print("Belum ada data untuk ditampilkan statistiknya.\n")
        return
    
    total = len(tugas)
    done = len(t for t in tugas if t['selesai'])
    undone = total - done

    diff_count = {
        'mudah': 0,
        'sedang': 0,
        'susah': 0
    }
    for t in tugas:
        level = t['tingkat'].lower()
        if level in diff_count:
            diff_count += 1

    persen_done = (done / total) * 100
    persen_undone = 100 - persen_done

    print(f"Username: {username}")
    print(f"Total: {total}")
    print(f"Tugas selesai: {done} ({persen_done:.0f}%)")
    print(f"Tugas belum selesai: {undone} ({persen_undone:.0f}%)")
    print("Berdasarkan tingkat kesulitan: ")
    # print(f"- Mudah: {diff_count['mudah']}")
    # print(f"- Sedang: {diff_count['sedang']}")
    # print(f"- Susah: {diff_count['susah']}")
    for level, count in diff_count.items():
        print(f"- {level.capitalize():<7}: {count}")

    try:
        upcoming = sorted(
            [t for t in tugas if not t['selesai']], key=lambda x: datetime.strptime(x['deadline'], "%Y-%m-$d")
        )
        if upcoming:
            print(f"Deadline terdekat: {upcoming[0]['judul']} ({upcoming[0]['deadline']})")
    except Exception:
        pass