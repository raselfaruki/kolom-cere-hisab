# modules/products.py
import streamlit as st
import sqlite3, os

DB_PATH = os.path.join("db", "kolom.db")

def product_ui():
    st.subheader("📦 প্রোডাক্ট মডিউল")

    name = st.text_input("নাম")
    category = st.text_input("ক্যাটাগরি")
    buy_price = st.number_input("ক্রয় মূল্য", value=0.0)
    sell_price = st.number_input("বিক্রয় মূল্য", value=0.0)

    if st.button("💾 প্রোডাক্ট সংরক্ষণ"):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                category TEXT,
                buy_price REAL,
                sell_price REAL
            )
        """)
        cur.execute("INSERT INTO products (name, category, buy_price, sell_price) VALUES (?, ?, ?, ?)",
                    (name, category, buy_price, sell_price))
        conn.commit()
        conn.close()
        st.success("✅ সংরক্ষিত")
