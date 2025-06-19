# app_streamlit.py - Imports
import streamlit as st
from modules.invoice import invoice_ui
from modules.products import product_ui
from modules.customers import customer_ui
from modules.reports import reports_ui
from modules.auth import validate_user, validate_license_key

from datetime import date, timedelta

# app_streamlit.py - Streamlit Page Configuration
import streamlit as st # Import streamlit again for clarity in this cell

st.set_page_config("কলম ছাড়া হিসাব", layout="wide")

# app_streamlit.py - License Validation Section
import streamlit as st # Import streamlit again for clarity in this cell
from modules.auth import validate_license_key # Import necessary function

st.markdown("🔐 **লাইসেন্স যাচাই করুন**")

# Initialize session state variables for authentication
if "auth" not in st.session_state:
    st.session_state.auth = False
if "authenticated" not in st.session_state:

# License key validation UI
if not st.session_state.authenticated:
    username = st.text_input("👤 ইউজারনেম")
    license_key = st.text_input("🔑 লাইসেন্স কী")
    if st.button("লগইন"):
        if validate_license_key(username, license_key):
            st.success("✅ সফলভাবে লগইন হয়েছেন!")
            st.session_state.authenticated = True
        else:
            st.error("❌ ইউজারনেম বা লাইসেন্স কী ভুল!")    st.session_state.authenticated = False

# License key validation UI
if not st.session_state.authenticated:
    username = st.text_input("👤 ইউজারনেম")
    license_key = st.text_input("🔑 লাইসেন্স কী")
    if st.button("লগইন"):
        if validate_license_key(username, license_key):
            st.success("✅ সফলভাবে লগইন হয়েছেন!")
            st.session_state.authenticated = True
        else:
            st.error("❌ ইউজারনেম বা লাইসেন্স কী ভুল!")

# app_streamlit.py - Login Page Function
import streamlit as st # Import streamlit again for clarity in this cell
from modules.auth import validate_user # Import necessary function

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

# app_streamlit.py - Dashboard Function
import streamlit as st # Import streamlit again for clarity in this cell
# Import necessary UI functions and utility functions
from modules.invoice import invoice_ui
from modules.products import product_ui
from modules.customers import customer_ui
from modules.reports import reports_ui
from interest_utils import calculate_interest
from datetime import date

def dashboard():
    st.sidebar.title("📋 মেনু")
    # Sidebar for navigation
    choice = st.sidebar.selectbox("নির্বাচন করুন", ["ড্যাশবোর্ড", "ইনভয়েস", "প্রোডাক্ট", "কাস্টমার", "রিপোর্ট"])

    # Display different UI based on sidebar selection
    if choice == "ড্যাশবোর্ড":
        # Placeholder for dashboard content
        st.subheader("ড্যাশবোর্ড")
        st.success(f"👋 স্বাগতম, {st.session_state.username}!")
        # The overdue invoice display logic was originally outside functions, moved here.
        st.subheader("বकेয়া ইনভয়েস সমূহ")
        # This invoice_list is hardcoded, should likely come from a database
        invoice_list = [
            {"customer": "জন", "due_date": date.today(), "total": 1000, "paid": 0},
            {"customer": "সাবিনা", "due_date": date.today(), "total": 800, "paid": 1}
        ]
        for inv in invoice_list:
            due = inv["due_date"]
            total = inv["total"]
            paid = inv["paid"]
            if paid == 0:
                interest = calculate_interest(due, total)
                total_with_interest = total + interest
                st.write(f"🧾 {inv['customer']} ➤ মূল: {total}৳  সুদ: {interest}৳  মোট: {total_with_interest}৳  ডিউ: {due}")

    elif choice == "ইনভয়েস":
        invoice_ui()
    elif choice == "প্রোডাক্ট":
        product_ui()
    elif choice == "কাস্টমার":
        customer_ui()
    elif choice == "রিপোর্ট":
        reports_ui() # Corrected function call

# app_streamlit.py - Main Application Flow
import streamlit as st # Import streamlit again for clarity in this cell
# Assuming login_page and dashboard functions are defined in previous cells
# from .app_streamlit import login_page, dashboard # Example if using relative imports

# This controls whether to show the login page or the dashboard
if st.session_state.auth:
    dashboard()
    # Assuming the content for dashboard choices will be handled within the dashboard function
    # based on the selected choice in the sidebar.
    # The rendering of invoice_ui, product_ui, etc., should happen within the dashboard function.
else:
    login_page()

# app_streamlit.py - Payment Logic (Originally commented out and likely misplaced)
# import streamlit as st # Import streamlit again for clarity in this cell
# Assuming calculate_interest and mark_paid are available
# from interest_utils import calculate_interest
# from modules.invoice import mark_paid

# This part was outside the main app flow and seemed to rely on an 'invoice' variable
# which is not defined in this scope. If this is part of the invoice UI, it should
# be moved into modules/invoice.py or handled within the invoice_ui function.
# if st.button("✅ বকেয়া পরিশোধ"):
#     # বর্তমান তারিখ > due_date হলে সুদ ধরা হবে
#     interest = calculate_interest(invoice['due_date'], invoice['total'])
#     grand_total = invoice['total'] + interest

#     mark_paid(invoice_id, grand_total)  # ডেটাবেজে paid = 1 সেট করুন
#     st.success(f"📬 মোট {grand_total}৳ আদায় হয়েছে (সুদসহ)")