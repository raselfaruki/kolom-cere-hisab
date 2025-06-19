# modules/invoice.py - Imports
import streamlit as st
import sqlite3
from datetime import date
# Assuming calculate_interest is imported in the main app or available globally
# from interest_utils import calculate_interest

# modules/invoice.py - get_all_invoices function
import sqlite3 # Import for clarity

def get_all_invoices():
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices")
    invoices = cursor.fetchall()
    conn.close()
    return invoices

# modules/invoice.py - add_invoice function
import streamlit as st # Import for clarity
import sqlite3 # Import for clarity
from datetime import date # Import for clarity

def add_invoice(customer, product, qty, rate, total, invoice_date, due_date):
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO invoices (customer, product, qty, rate, total, invoice_date, due_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (customer, product, qty, rate, total, invoice_date, due_date))
        conn.commit()
        st.success("✅ ইনভয়েস সফলভাবে যুক্ত হয়েছে")
    except Exception as e:
        st.error(f"Error adding invoice: {e}")
    conn.close()

# modules/invoice.py - mark_paid function
import streamlit as st # Import for clarity
import sqlite3 # Import for clarity

def mark_paid(invoice_id, paid_amount):
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    try:
        # Assuming marking paid means setting the 'paid' column to 1
        # In a real app, you might have a separate payments table
        cursor.execute("UPDATE invoices SET paid = 1 WHERE id = ?", (invoice_id,))
        conn.commit()
        st.success(f"📬 ইনভয়েস #{invoice_id} পরিশোধ হয়েছে")
    except Exception as e:
        st.error(f"Error marking invoice paid: {e}")
    conn.close()

# modules/invoice.py - invoice_ui function
import streamlit as st # Import for clarity
from datetime import date # Import for clarity
# Assuming get_all_invoices, add_invoice, mark_paid, and calculate_interest are available
# from .invoice import get_all_invoices, add_invoice, mark_paid
# from interest_utils import calculate_interest


def invoice_ui():
    st.title("🧾 ইনভয়েস")

    st.subheader("➕ নতুন ইনভয়েস তৈরি করুন")
    # You would likely need to fetch lists of customers and products here
    # Example placeholders:
    customer = st.text_input("কাস্টমার নাম")
    product = st.text_input("প্রোডাক্ট নাম") # Consider using a selectbox with available products
    qty = st.number_input("পরিমাণ", min_value=1, value=1)
    rate = st.number_input("রেট", min_value=0.0, value=0.0)
    total = qty * rate
    st.write(f"মোট: {total}৳")

    invoice_date = st.date_input("📅 ইনভয়েস তারিখ নির্বাচন করুন", value=date.today())
    due_date = st.date_input("📅 ডিউ তারিখ নির্বাচন করুন", value=date.today()) # You might want a default based on terms


    if st.button("✅ ইনভয়েস অ্যাড করো"):
        add_invoice(customer, product, qty, rate, total, invoice_date.isoformat(), due_date.isoformat())

    st.subheader("📋 ইনভয়েস তালিকা")
    invoices = get_all_invoices()

    if invoices:
        # Assuming invoice structure is (id, customer, product, qty, rate, total, invoice_date, due_date, paid)
        for inv in invoices:
            inv_id, customer, product, qty, rate, total, invoice_date_str, due_date_str, paid = inv
            due_date = date.fromisoformat(due_date_str)
            invoice_date = date.fromisoformat(invoice_date_str)

            interest = calculate_interest(due_date, total) # Assuming calculate_interest is available
            grand_total = total + interest

            st.write(f"---")
            st.write(f"ইনভয়েস আইডি: #{inv_id}")
            st.write(f"কাস্টমার: {customer}")
            st.write(f"প্রোডাক্ট: {product} (পরিমাণ: {qty}, রেট: {rate}৳)")
            st.write(f"ইনভয়েস তারিখ: {invoice_date}")
            st.write(f"ডিউ তারিখ: {due_date}")
            st.write(f"মূল টাকা: {total}৳")
            st.write(f"সুদ: {interest}৳")
            st.write(f"মোট টাকা: {grand_total}৳")
            st.write(f"পরিশোধিত: {'হ্যাঁ' if paid else 'না'}")

            if paid == 0 and st.button(f"✅ বকেয়া পরিশোধ #{inv_id}"):
                 mark_paid(inv_id, grand_total) # In a real app, you'd handle the actual payment amount
                 st.experimental_rerun() # Rerun to update the list after payment

    else:
        st.write("কোন ইনভয়েস পাওয়া যায়নি।")