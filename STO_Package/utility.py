import sys
from database import ensure_files
from delete_task import delete_task, restore_task
from task import add_task 
from statistik import stats_for_user
from view import view_deleted_for_user, view_tasks_for_user, search_task_by_title
from edit import edit_task

def welcome_screen():
    ensure_files()
    print("======================================")
    print("   SMART TASK ORGANIZER (Sederhana)   ")
    print("======================================")
    
def main_menu(username):
    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Statistik Akun")
        print("2. Lihat Daftar Task Aktif")
        print("3. Cari Task berdasarkan Judul")
        print("4. Lihat Daftar Task yang Dihapus (Sampah)")
        print("5. Logout / Ganti Akun")
        choice = input("Pilih (1-5): ").strip()
        if choice == "1":
            stats_for_user(username)
        elif choice == "2":
            view_tasks_for_user(username)
            menu_task(username)
        elif choice == "3":
            search_task_by_title(username)
            menu_task(username)
        elif choice == "4":
            view_deleted_for_user(username)
            menu_task(username)
        elif choice == "5":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")
            
def menu_task(username):
    while True:
        print("\n--- Menu Task ---")
        print("1. Membuat Task Baru")
        print("2. Mengubah Task")
        print("3. Menghapus Task")
        print("4. Mengembalikan Task dari Sampah")
        print("5. Kembali")
        choice = input("Pilih (1-5): ").strip()
        
        if choice == "1":
            add_task(username)
        elif choice == "2":
            edit_task(username)
        elif choice == "3":
            delete_task(username)
        elif choice == "4":
            restore_task(username)
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid.")
