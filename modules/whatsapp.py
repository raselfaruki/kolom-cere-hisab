# modules/whatsapp.py
import urllib.parse

def get_whatsapp_link(number, message):
    number = number.replace("+88", "").replace(" ", "")
    text = urllib.parse.quote(message)
    return f"https://wa.me/88{number}?text={text}"
