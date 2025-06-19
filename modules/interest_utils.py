# interest_utils.py - Imports
from datetime import date

# interest_utils.py - calculate_interest function
from datetime import date # Import for clarity

def calculate_interest(due_date, total_amount):
    """
    Calculates simple interest for overdue payments.
    Assuming a simple daily interest rate for demonstration.
    You might need to adjust the interest rate and calculation logic
    based on your specific requirements.
    """
    today = date.today()
    if today > due_date:
        days_overdue = (today - due_date).days
        # Example: 0.1% daily interest rate
        daily_interest_rate = 0.001
        interest = total_amount * daily_interest_rate * days_overdue
        return round(interest, 2) # Round to 2 decimal places
    else:
        return 0