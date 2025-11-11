from database import load_tasks
import datetime

def stats_for_user(username):
    tasks = [t for t in load_tasks() if t["username"] == username]
    total = len(tasks)
    selesai = sum(1 for t in tasks if t["status"].lower() == "sudah")
    belum = total - selesai
    pct_selesai = f"{(selesai/total*100):.1f}%" if total > 0 else "0%"
    # by level
    mudah = sum(1 for t in tasks if t["level"].lower() == "mudah")
    sedang = sum(1 for t in tasks if t["level"].lower() == "sedang")
    sulit = sum(1 for t in tasks if t["level"].lower() == "sulit")
    # nearest deadline
    nearest = None
    for t in tasks:
        try:
            d = datetime.datetime.strptime(t["deadline"], "%Y-%m-%d").date()
            if nearest is None or d < nearest[0]:
                nearest = (d, t["judul"])
        except:
            pass
    print("\n=== Statistik Akun ===")
    print(f"Username: {username}")
    print(f"Total tugas: {total}")
    print(f"Selesai: {selesai} ({pct_selesai})")
    print(f"Belum selesai: {belum}")
    print("\nBerdasarkan tingkat kesulitan:")
    print(f"- Mudah: {mudah}")
    print(f"- Sedang: {sedang}")
    print(f"- Sulit: {sulit}")
    if nearest:
        print(f"\nDeadline terdekat: \"{nearest[1]}\" ({nearest[0].isoformat()})")
    else:
        print("\nTidak ada deadline terdeteksi.")