from database import load_trash, load_tasks

def search_task_by_title(username):
    q = input("Masukkan Judul Task yang ingin dicari: ").strip().lower()
    if q == "":
        print("Query kosong.")
        return
    tasks = load_tasks()
    found = [t for t in tasks if t["username"] == username and q in t["judul"].lower()]
    if not found:
        print("Task tidak ditemukan.")
        return
    print("\nHasil Pencarian:")
    for t in found:
        print(f"{t['id']} | {t['judul']} | {t['deskripsi']} | {t['level']} | {t['deadline']} | {t['status']}")

def view_deleted_for_user(username):
    tasks = load_trash()
    user_tasks = [t for t in tasks if t["username"] == username]
    if not user_tasks:
        print("\nTidak ada task yang dihapus.")
        return
    print("\nDaftar tugas (sampah):")
    print("Id | Judul | Deskripsi | Level | Deadline | Status")
    for t in user_tasks:
        print(f"{t['id']} | {t['judul']} | {t['deskripsi']} | {t['level']} | {t['deadline']} | {t['status']}")

def find_task_by_id_for_user(username, tid):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == str(tid) and t["username"] == username:
            return t
    return None

def view_tasks_for_user(username, include_deleted=False):
    tasks = load_tasks()
    user_tasks = [t for t in tasks if t["username"] == username]
    if not user_tasks:
        print("\nTidak ada task.")
        return
    print("\nDaftar tugas yang belum/aktif:")
    print("Id | Judul | Deskripsi | Level | Deadline | Status")
    for t in user_tasks:
        print(f"{t['id']} | {t['judul']} | {t['deskripsi']} | {t['level']} | {t['deadline']} | {t['status']}")