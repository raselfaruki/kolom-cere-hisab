# app_streamlit.py
import streamlit as st
from modules.invoice import invoice_ui
from modules.products import product_ui
from modules.customers import customer_ui
from modules.reports import reports_ui
# whatsapp.py - Imports
import requests # Example using requests, replace with your API's method

# whatsapp.py - send_whatsapp_message function
import requests # Example using requests, replace with your API's method

def send_whatsapp_message(to_number, message):
    """
    Example function to send a WhatsApp message.
    Replace with actual API calls and authentication.
    """
    # Replace with your WhatsApp API endpoint and credentials
    api_url = "YOUR_WHATSAPP_API_ENDPOINT"
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET" # Or other authentication method

    payload = {
        "to": to_number,
        "body": message
    }

    headers = {
        "Authorization": f"Bearer {api_key}", # Example auth header
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        print("WhatsApp message sent successfully!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending WhatsApp message: {e}")
        return False

# Example usage (requires proper API setup and credentials)
# send_whatsapp_message("+1234567890", "Hello from your app!")
st.set_page_config("কলম ছাড়া হিসাব", layout="wide")


st.markdown("🔐 **লাইসেন্স যাচাই করুন**")


from modules.auth import validate_user, validate_license_key  # make sure this is imported

if "auth" not in st.session_state:
    st.session_state.auth = False
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# whatsapp.py - Imports
import requests # Example using requests, replace with your API's method

# whatsapp.py - send_whatsapp_message function
import requests # Example using requests, replace with your API's method

def send_whatsapp_message(to_number, message):
    """
    Example function to send a WhatsApp message.
    Replace with actual API calls and authentication.
    """
    # Replace with your WhatsApp API endpoint and credentials
    api_url = "YOUR_WHATSAPP_API_ENDPOINT"
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET" # Or other authentication method

    payload = {
        "to": to_number,
        "body": message
    }

    headers = {
        "Authorization": f"Bearer {api_key}", # Example auth header
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        print("WhatsApp message sent successfully!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending WhatsApp message: {e}")
        return False

# Example usage (requires proper API setup and credentials)
# send_whatsapp_message("+1234567890", "Hello from your app!")

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

from interest_utils import calculate_interest

# প্রতিটি ইনভয়েসের জন্য
from datetime import date

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

