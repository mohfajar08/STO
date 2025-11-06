import json
import os
from datetime import datetime

DATA_FILE = "data.json"
BACKUP_FILE = "data_backup.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"accounts": {}, "tasks": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def backup_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as src, open(BACKUP_FILE, "w") as dst:
            dst.write(src.read())

def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r") as src, open(DATA_FILE, "w") as dst:
            dst.write(src.read())
        print("Data berhasil direstore dari backup.")
    else:
        print("File backup tidak ditemukan.")