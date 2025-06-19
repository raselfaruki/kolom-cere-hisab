# modules/reminder.py
from datetime import datetime

def calculate_interest(due_date_str, total_amount):
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta_days = (today - due_date).days
        if delta_days <= 0:
            return 0
        daily_rate = 0.19 / 365
        return round(total_amount * daily_rate * delta_days, 2)
    except Exception:
        return 0
