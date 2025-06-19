# modules/whatsapp.py
import urllib.parse

def get_whatsapp_link(number, message):
    number = number.replace("+88", "").replace(" ", "")
    text = urllib.parse.quote(message)
    return f"https://wa.me/88{number}?text={text}"

# UI অংশে
msg = f"প্রিয় {name}, আপনার ইনভয়েস বকেয়া রয়েছে। অনুগ্রহ করে {due_date}-এর মধ্যে পরিশোধ করুন।"
whatsapp_link = get_whatsapp_link(mobile, msg)
st.markdown(f"[📲 WhatsApp মেসেজ পাঠান]({whatsapp_link})", unsafe_allow_html=True)
