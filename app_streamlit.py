# app_streamlit.py
import streamlit as st
from modules.auth import validate_user
from modules.invoice import invoice_ui
from modules.products import product_ui
from modules.customers import customer_ui
from modules.reports import report_ui

st.set_page_config("কলম ছাড়া হিসাব", layout="wide")

if "auth" not in st.session_state:
    st.session_state.auth = False

def login_page():
    st.title("✒️ কলম ছাড়া হিসাব - লগইন")
    user = st.text_input("👤 ইউজারনেম")
    pwd = st.text_input("🔐 পাসওয়ার্ড", type="password")
    if st.button("🚪 প্রবেশ করুন"):
        if validate_user(user, pwd):
            st.session_state.auth = True
            st.session_state.username = user
            st.success("✅ লগইন সফল!")
        else:
            st.error("❌ ইউজার/পাসওয়ার্ড ভুল")

def dashboard():
    st.sidebar.title("📋 মেনু")
    choice = st.sidebar.selectbox("নির্বাচন করুন", ["ড্যাশবোর্ড", "ইনভয়েস", "প্রোডাক্ট", "কাস্টমার", "রিপোর্ট"])

    st.title("✒️ কলম ছাড়া হিসাব")

    if choice == "ড্যাশবোর্ড":
        st.success(f"👋 স্বাগতম, {st.session_state.username}!")
    elif choice == "ইনভয়েস":
        invoice_ui()
    elif choice == "প্রোডাক্ট":
        product_ui()
    elif choice == "কাস্টমার":
        customer_ui()
    elif choice == "রিপোর্ট":
        report_ui()

if st.session_state.auth:
    dashboard()
else:
    login_page()
