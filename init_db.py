# init_db.py
import sqlite3
import os


def add_customer(name, mobile, address):
    conn = sqlite3.connect("db/hisab.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO customers (name, mobile, address) VALUES (?, ?, ?)", (name, mobile, address))
    conn.commit()
    conn.close()

st.subheader("👥 নতুন কাস্টমার যুক্ত করুন")
name = st.text_input("নাম")
mobile = st.text_input("মোবাইল নম্বর")
address = st.text_area("ঠিকানা")

if st.button("➕ অ্যাড করো"):
    add_customer(name, mobile, address)
    st.success(f"✅ {name} সফলভাবে যুক্ত হয়েছে")


os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/kolom.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cur.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'kolom123')")
conn.commit()
conn.close()
print("✅ ডেটাবেজ প্রস্তুত")

# init_db.py → ইনভয়েস টেবিল
cursor.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    product TEXT,
    qty INTEGER,
    rate REAL,
    total REAL,
    invoice_date TEXT,
    due_date TEXT,
    paid INTEGER DEFAULT 0
)
""")

