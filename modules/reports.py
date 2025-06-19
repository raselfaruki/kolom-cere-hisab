# modules/reports.py
import streamlit as st
import sqlite3, os
import matplotlib.pyplot as plt

DB_PATH = os.path.join("db", "kolom.db")

def report_ui():
    st.subheader("📈 মাসিক সেলস রিপোর্ট")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT date, total FROM invoices")
    rows = cur.fetchall()
    conn.close()

    data = {}
    for date_str, total in rows:
        month = date_str[:7]
        data[month] = data.get(month, 0) + total

    if data:
        months = list(data.keys())
        totals = list(data.values())
        fig, ax = plt.subplots()
        ax.bar(months, totals)
        ax.set_title("মাসভিত্তিক বিক্রি")
        st.pyplot(fig)
    else:
        st.warning("❗ রিপোর্ট করার মতো কোনো ইনভয়েস নেই")
