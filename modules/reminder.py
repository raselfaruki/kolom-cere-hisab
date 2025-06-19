# reminder.py - Imports
import sqlite3
from datetime import date, timedelta
# Assuming whatsapp_utils is available for sending messages

# reminder.py - get_overdue_invoices function
import sqlite3 # Import for clarity
from datetime import date # Import for clarity

def get_overdue_invoices():
    conn = sqlite3.connect("db/hisab.db")
    cursor = conn.cursor()
    today = date.today().isoformat()
    cursor.execute("SELECT * FROM invoices WHERE due_date < ? AND paid = 0", (today,))
    overdue_invoices = cursor.fetchall()
    conn.close()
    return overdue_invoices

# reminder.py - send_reminders function
import sqlite3 # Import for clarity
from datetime import date, timedelta # Import for clarity
# Assuming whatsapp_utils is available for sending messages

def send_reminders():
    overdue_list = get_overdue_invoices()

    if overdue_list:
        print(f"Found {len(overdue_list)} overdue invoices.")
        for inv in overdue_list:
            # Assuming invoice structure is (id, customer, product, qty, rate, total, invoice_date, due_date, paid)
            inv_id, customer, product, qty, rate, total, invoice_date_str, due_date_str, paid = inv
            due_date = date.fromisoformat(due_date_str)

            # You would typically get customer contact info here, maybe from the customers table
            # For demonstration, just printing a message
            message = f"Reminder for {customer}: Invoice #{inv_id} ({total}৳) was due on {due_date}. Please arrange payment."
            print(message)
            # uncomment the line below if you have a whatsapp_utils module with send_whatsapp_message function
            # send_whatsapp_message(customer_mobile_number, message) # Need customer mobile and send function

    else:
        print("No overdue invoices found.")

# Example of how you might trigger reminders (e.g., with a scheduler)
# send_reminders()