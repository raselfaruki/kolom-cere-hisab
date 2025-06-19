# app_streamlit.py
import streamlit as st
from modules.invoice import invoice_ui
from modules.products import product_ui
from modules.customers import customer_ui
from modules.reports import report_ui

st.set_page_config("কলম ছাড়া হিসাব", layout="wide")


st.markdown("🔐 **লাইসেন্স যাচাই করুন**")


from modules.auth import validate_user, validate_license_key  # make sure this is imported

if "auth" not in st.session_state:
    st.session_state.auth = False
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    username = st.text_input("👤 ইউজারনেম")
    license_key = st.text_input("🔑 লাইসেন্স কী")
    if st.button("লগইন"):
        if validate_license_key(username, license_key):
            st.success("✅ সফলভাবে লগইন হয়েছেন!")
            st.session_state.authenticated = True
        else:
            st.error("❌ ইউজারনেম বা লাইসেন্স কী ভুল!")

if st.session_state.authenticated:
    st.subheader("🧾 ইনভয়েস তৈরি করুন")
    customer = st.text_input("👥 কাস্টমার নাম")
    products = get_all_products()
    product_names = [p[0] for p in products]

from datetime import date, timedelta

due_date = st.date_input("📅 ডিউ তারিখ নির্বাচন করুন", value=date.today() + timedelta(days=21))



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



# প্রতিটি ইনভয়েসের জন্য
for inv in invoice_list:
    due = inv["due_date"]
    total = inv["total"]
    paid = inv["paid"]

    if paid == 0:
        interest = calculate_interest(due, total)
        total_with_interest = total + interest
        st.write(f"🧾 {inv['customer']} ➤ মূল: {total}৳ | সুদ: {interest}৳ | মোট: {total_with_interest}৳ | ডিউ: {due}")



if paid == 0:
    interest = calculate_interest(due, total)
    total_with_interest = total + interest
    st.write(f"🧾 {inv['customer']} ➤ মূল: {total}৳ | সুদ: {interest}৳ | মোট: {total_with_interest}৳ | ডিউ: {due}")


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

# পেমেন্টের সময়
if st.button("✅ বকেয়া পরিশোধ"):
    # বর্তমান তারিখ > due_date হলে সুদ ধরা হবে
    interest = calculate_interest(invoice['due_date'], invoice['total'])
    grand_total = invoice['total'] + interest

    mark_paid(invoice_id, grand_total)  # ডেটাবেজে paid = 1 সেট করুন
    st.success(f"📬 মোট {grand_total}৳ আদায় হয়েছে (সুদসহ)")

