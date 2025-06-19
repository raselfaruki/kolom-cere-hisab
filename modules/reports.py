# modules/reports.py - Imports
import streamlit as st
import sqlite3
import pandas as pd

# modules/reports.py - get_sales_report_data function
import sqlite3 # Import for clarity
import pandas as pd # Import for clarity

def get_sales_report_data():
    conn = sqlite3.connect("db/hisab.db")
    # Join invoices and products tables if needed for detailed reports
    # For a simple sales report, we can just use invoices
    query = "SELECT * FROM invoices"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# modules/reports.py - reports_ui function
import streamlit as st # Import for clarity
import pandas as pd # Import for clarity
# Assuming get_sales_report_data is available
# from .reports import get_sales_report_data

def reports_ui():
    st.title("📊 রিপোর্ট")

    st.subheader("বিক্রয় রিপোর্ট")
    sales_data = get_sales_report_data()

    if not sales_data.empty:
        st.write("মোট ইনভয়েসের সংখ্যা:", sales_data.shape[0])
        st.write("মোট বিক্রয়:", sales_data['total'].sum(), "৳")
        st.write("পরিশোধিত ইনভয়েস:", sales_data[sales_data['paid'] == 1].shape[0])
        st.write("বকেয়া ইনভয়েস:", sales_data[sales_data['paid'] == 0].shape[0])

        st.dataframe(sales_data)

        # Example: Simple plot of sales over time
        sales_data['invoice_date'] = pd.to_datetime(sales_data['invoice_date'])
        sales_over_time = sales_data.groupby(sales_data['invoice_date'].dt.to_period('M'))['total'].sum().reset_index()
        sales_over_time['invoice_date'] = sales_over_time['invoice_date'].astype(str)

        st.subheader("মাসিক বিক্রয় গ্রাফ")
        st.line_chart(sales_over_time.set_index('invoice_date'))

    else:
        st.write("কোন বিক্রয় ডেটা পাওয়া যায়নি।")