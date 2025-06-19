# modules/customers.py
import streamlit as st
import sqlite3, os

DB_PATH = os.path.join("db", "kolom.db")

def customer_ui():
    st.subheader("👥 কাস্টমার মডিউল")

    name = st.text_input("নাম")
    mobile = st.text_input("মোবাইল")
    address = st.text_area("ঠিকানা")

    if st.button("💾 সংরক্ষণ"):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                mobile TEXT,
                address TEXT
            )
        """)
        cur.execute("INSERT INTO customers (name, mobile, address) VALUES (?, ?, ?)",
                    (name, mobile, address))
        conn.commit()
        conn.close()
        st.success("✅ কাস্টমার যোগ হয়েছে")
