# init_db.py - Imports
import sqlite3
import os

# init_db.py - initialize_database function
import sqlite3 # Import for clarity
import os # Import for clarity

def initialize_database():
    os.makedirs("db", exist_ok=True)

    # Initialize kolom.db (for users)
    conn_kolom = sqlite3.connect("db/kolom.db")
    cur_kolom = conn_kolom.cursor()
    cur_kolom.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur_kolom.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'kolom123')")
    conn_kolom.commit()
    conn_kolom.close()
    print("✅ kolom.db ডেটাবেজ প্রস্তুত (Users)")

    # Initialize hisab.db (for customers and invoices)
    conn_hisab = sqlite3.connect("db/hisab.db")
    cur_hisab = conn_hisab.cursor()
    cur_hisab.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        address TEXT
    )
    ''')
    cur_hisab.execute('''
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
    ''')
    conn_hisab.commit()
    conn_hisab.close()
    print("✅ hisab.db ডেটাবেজ প্রস্তুত (Customers, Invoices)")

    # Initialize products.db (assuming a separate one as suggested in auth.py)
    conn_products = sqlite3.connect("db/products.db")
    cur_products = conn_products.cursor()
    cur_products.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        price REAL,
        buy_price REAL
    )
    ''')
    conn_products.commit()
    conn_products.close()
    print("✅ products.db ডেটাবেজ প্রস্তুত (Products)")

# init_db.py - Call initialize_database function
# Assuming initialize_database function is defined in a previous cell

initialize_database()