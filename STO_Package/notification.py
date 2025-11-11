from database import load_tasks

def notify_user_tasks(user):
    tasks = [t for t in load_tasks() if t["username"] == user and t["status"].lower() != "sudah"]
    print(f"\nAnda memiliki {len(tasks)} tugas yang belum dikerjakan.")