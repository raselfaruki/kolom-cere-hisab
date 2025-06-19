# modules/auth.py
import sqlite3

def validate_license_key(username, license_key):
    # Example logic; replace with your real validation logic
    return license_key == "ABC123" and username.strip() != ""

def add_buy_price_column():
    conn = sqlite3.connect("your_database.db")
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE products ADD COLUMN buy_price REAL")
    conn.commit()
    conn.close()

def validate_user(username, password):
    # Example logic — you can replace this with your real checks
    return username == "admin" and password == "secret"

