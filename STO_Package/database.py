import os

AKUN_FILE = "akun.txt"
TASK_FILE = "task.txt"
TRASH_FILE = "trash.txt"

def ensure_files():
    for fn in (AKUN_FILE, TASK_FILE, TRASH_FILE):
        if not os.path.exists(fn):
            open(fn, "a", encoding="utf-8").close()

def read_lines(filename):
    ensure_files()
    with open(filename, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip() != ""]
    return lines

def append_line(filename, line):
    ensure_files()
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line.rstrip("\n") + "\n")

def write_lines(filename, lines):
    ensure_files()
    with open(filename, "w", encoding="utf-8") as f:
        for ln in lines:
            f.write(ln.rstrip("\n") + "\n")
            
# -------------------------
# Tasks
# -------------------------
def parse_task_line(ln):
    # id|username|judul|deskripsi|level|deadline|status
    parts = ln.split("|")
    if len(parts) < 7:
        return None
    return {
        "id": parts[0],
        "username": parts[1],
        "judul": parts[2],
        "deskripsi": parts[3],
        "level": parts[4],
        "deadline": parts[5],
        "status": parts[6]
    }

def compose_task_line(t):
    return "|".join([
        str(t["id"]),
        t["username"],
        t["judul"],
        t["deskripsi"],
        t["level"],
        t["deadline"],
        t["status"]
    ])

def load_tasks():
    lines = read_lines(TASK_FILE)
    tasks = []
    for ln in lines:
        t = parse_task_line(ln)
        if t:
            tasks.append(t)
    return tasks

def load_trash():
    lines = read_lines(TRASH_FILE)
    tasks = []
    for ln in lines:
        t = parse_task_line(ln)
        if t:
            tasks.append(t)
    return tasks

def save_tasks(tasks):
    write_lines(TASK_FILE, [compose_task_line(t) for t in tasks])

def save_trash(tasks):
    write_lines(TRASH_FILE, [compose_task_line(t) for t in tasks])

def next_task_id():
    tasks = load_tasks() + load_trash()
    max_id = 0
    for t in tasks:
        try:
            iid = int(t["id"])
            if iid > max_id:
                max_id = iid
        except:
            pass
    return str(max_id + 1)