from database import load_tasks, load_trash, save_tasks, save_trash, append_line, compose_task_line, TASK_FILE, TRASH_FILE

def delete_task(username):
    print("\n=== Menghapus Task ===")
    tid = input("Masukkan id task yang ingin dihapus: ").strip()
    tasks = load_tasks()
    deleted = None
    remaining = []
    for t in tasks:
        if t["id"] == tid and t["username"] == username:
            deleted = t
        else:
            remaining.append(t)
    if not deleted:
        print("Task tidak ditemukan atau bukan milik anda.")
        return
    # Pindah ke trash
    append_line(TRASH_FILE, compose_task_line(deleted))
    save_tasks(remaining)
    print("Task berhasil dihapus.")

def restore_task(username):
    print("\n=== Mengembalikan Task dari Sampah ===")
    tid = input("Masukkan id task yang ingin dikembalikan: ").strip()
    trash = load_trash()
    restored = None
    remaining = []
    for t in trash:
        if t["id"] == tid and t["username"] == username:
            restored = t
        else:
            remaining.append(t)
    if not restored:
        print("Task tidak ditemukan di sampah atau bukan milik anda.")
        return
    append_line(TASK_FILE, compose_task_line(restored))
    save_trash(remaining)
    print("Task berhasil dikembalikan.")