from datetime import date

def calculate_interest(due_date, total, daily_rate=0.01):
    """
    Simple interest calculation based on due date and total.
    - daily_rate is default 1% per day
    """
    today = date.today()
    days_overdue = (today - due_date).days
    if days_overdue > 0:
        return round(total * daily_rate * days_overdue, 2)
    return 0