# modules/invoice.py
import streamlit as st
from fpdf import FPDF
from datetime import date
import sqlite3, os

DB_PATH = os.path.join("db", "kolom.db")

def invoice_ui():
    st.subheader("🧾 নতুন ইনভয়েস")
    cust = st.text_input("👤 কাস্টমার নাম")
    prod_list = st.session_state.get("products", ["পেন্সিল", "খাতা"])
    
    product = st.selectbox("📦 প্রোডাক্ট", prod_list)
    qty = st.number_input("🔢 পরিমাণ", value=1, step=1)
    rate = st.number_input("💵 রেট", value=10.0)

    if "invoice_items" not in st.session_state:
        st.session_state.invoice_items = []

    if st.button("➕ লাইন যোগ করো"):
        total = qty * rate
        st.session_state.invoice_items.append((product, qty, rate, total))

    if st.session_state.invoice_items:
        st.table(st.session_state.invoice_items)
        grand_total = sum([row[3] for row in st.session_state.invoice_items])
        st.success(f"মোট: {grand_total:.2f}৳")
        if st.button("💾 ইনভয়েস সংরক্ষণ + PDF"):
            save_invoice(cust, st.session_state.invoice_items, grand_total)
            st.session_state.invoice_items = []

def save_invoice(cust, items, total):
    date_str = str(date.today())

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, customer TEXT, date TEXT, total REAL)")
    cur.execute("INSERT INTO invoices (customer, date, total) VALUES (?, ?, ?)", (cust, date_str, total))
    inv_id = cur.lastrowid

    cur.execute("""CREATE TABLE IF NOT EXISTS invoice_items (
        invoice_id INTEGER, product TEXT, qty INTEGER, rate REAL, total REAL
    )""")
    for row in items:
        cur.execute("INSERT INTO invoice_items VALUES (?, ?, ?, ?, ?)", (inv_id, *row))
    conn.commit()
    conn.close()

    generate_pdf(cust, items, total, date_str, inv_id)

def generate_pdf(customer, items, total, date_str, invoice_id):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(190, 10, "✒️ কলম ছাড়া হিসাব", ln=True, align='C')
    pdf.cell(190, 10, f"ইনভয়েস #{invoice_id} | তারিখ: {date_str}", ln=True)
    pdf.cell(190, 10, f"কাস্টমার: {customer}", ln=True)
    pdf.ln(5)

    pdf.cell(60, 8, "প্রোডাক্ট", 1)
    pdf.cell(30, 8, "পরিমাণ", 1)
    pdf.cell(40, 8, "রেট", 1)
    pdf.cell(40, 8, "মোট", 1, ln=True)

    for p, q, r, t in items:
        pdf.cell(60, 8, p, 1)
        pdf.cell(30, 8, str(q), 1)
        pdf.cell(40, 8, f"{r:.2f}", 1)
        pdf.cell(40, 8, f"{t:.2f}", 1, ln=True)

    pdf.ln(5)
    pdf.cell(190, 10, f"মোট: {total:.2f}৳", ln=True)
    filename = f"invoice_{invoice_id}.pdf"
    pdf.output(filename)
