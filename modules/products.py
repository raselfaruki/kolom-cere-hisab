# modules/products.py - Imports
import streamlit as st
import sqlite3

# modules/products.py - get_all_products function
import sqlite3 # Import for clarity

def get_all_products():
    conn = sqlite3.connect("db/products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

# modules/products.py - add_product function
import streamlit as st # Import for clarity
import sqlite3 # Import for clarity

def add_product(name, price, buy_price):
    conn = sqlite3.connect("db/products.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products (name, price, buy_price) VALUES (?, ?, ?)", (name, price, buy_price))
        conn.commit()
        st.success(f"✅ {name} সফলভাবে যুক্ত হয়েছে")
    except sqlite3.IntegrityError:
        st.error(f"❌ প্রোডাক্ট '{name}' আগে থেকেই আছে।")
    except Exception as e:
        st.error(f"Error adding product: {e}")
    conn.close()

# modules/products.py - product_ui function
import streamlit as st # Import for clarity
# Assuming get_all_products and add_product are available
# from .products import get_all_products, add_product # Example if using relative imports

def product_ui():
    st.title("📦 প্রোডাক্ট")

    st.subheader("➕ নতুন প্রোডাক্ট যুক্ত করুন")
    name = st.text_input("নাম")
    price = st.number_input("বিক্রয় মূল্য", min_value=0.0, value=0.0)
    buy_price = st.number_input("ক্রয় মূল্য", min_value=0.0, value=0.0)

    if st.button("➕ অ্যাড করো"):
        add_product(name, price, buy_price)

    st.subheader("📋 প্রোডাক্ট তালিকা")
    products = get_all_products()

    if products:
        for product in products:
            # Assuming product structure is (id, name, price, buy_price)
            st.write(f"নাম: {product[1]}, বিক্রয় মূল্য: {product[2]}৳, ক্রয় মূল্য: {product[3]}৳")
    else:
        st.write("কোন প্রোডাক্ট পাওয়া যায়নি।")