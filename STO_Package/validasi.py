import datetime

def valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def normalize_level(s):
    s = s.strip().capitalize()
    if s in ("Mudah", "Sedang", "Sulit"):
        return s
    return None

def normalize_status(s):
    s = s.strip().capitalize()
    if s in ("Belum", "Sudah"):
        return s
    return None