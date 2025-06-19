# modules/customers.py - Imports
import streamlit as st
import sqlite3

# modules/customers.py - get_all_customers function
import sqlite3 # Import sqlite3 again for clarity in this cell

def get_all_customers():
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers

# modules/customers.py - add_customer function
import sqlite3 # Import sqlite3 again for clarity in this cell
import streamlit as st # Import streamlit for st.success/st.error

def add_customer(name, mobile, address):
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, mobile, address) VALUES (?, ?, ?)", (name, mobile, address))
        conn.commit()
        # The st.success here might be better placed in the UI function that calls this
        # st.success(f"✅ {name} সফলভাবে যুক্ত হয়েছে")
    except Exception as e:
        st.error(f"Error adding customer: {e}")
    conn.close()

# modules/customers.py - add_customer_ui function
import streamlit as st # Import streamlit for UI elements
# Assuming add_customer is available (defined in another cell or imported)
# from .customers import add_customer # Example if using relative imports

def add_customer_ui():
    st.subheader("👥 নতুন কাস্টমার যুক্ত করুন")
    name = st.text_input("নাম")
    mobile = st.text_input("মোবাইল নম্বর")
    address = st.text_area("ঠিকানা")

    if st.button("➕ অ্যাড করো"):
        # Call the add_customer function
        add_customer(name, mobile, address)
        st.success(f"✅ {name} সফলভাবে যুক্ত হয়েছে") # Display success message here

# modules/customers.py - customer_ui function
import streamlit as st # Import streamlit for UI elements
# Assuming get_all_customers and add_customer_ui are available
# from .customers import get_all_customers, add_customer_ui # Example if using relative imports

def customer_ui():
    st.title("👥 কাস্টমার")
    add_customer_ui() # Include the add customer UI
    st.subheader("📋 কাস্টমার তালিকা")
    customers = get_all_customers()

    if customers:
        for customer in customers:
            # Assuming customer structure is (id, name, mobile, address)
            st.write(f"নাম: {customer[1]}, মোবাইল: {customer[2]}, ঠিকানা: {customer[3]}")
    else:
        st.write("কোন কাস্টমার পাওয়া যায়নি।")