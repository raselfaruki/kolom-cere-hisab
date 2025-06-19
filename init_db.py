# init_db.py
import sqlite3
import os

os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/kolom.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cur.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'kolom123')")
conn.commit()
conn.close()
print("✅ ডেটাবেজ প্রস্তুত")
