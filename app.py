import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.hero {
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.product-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    height: 280px;
}
.product-card p {
    color: #4b5563;
    font-size: 15px;
    line-height: 1.5;
}
.product-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 20px 35px rgba(139,92,246,0.3);
}x  
.product-name {
    font-size: 20px;
    font-weight: bold;
    color: #333;
}

.price {
    color: #16a34a;
    font-size: 22px;
    font-weight: bold;
}

.category {
    background-color: #e0e7ff;
    padding: 4px 10px;
    border-radius: 10px;
    display: inline-block;
    margin-bottom: 10px;
    color: #4338ca;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",  
        "price": 2999,
        "description": "Premium noise-cancelling headphones with 40-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, notifications, and health metrics in real-time.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Comfortable lightweight shoes designed for daily running.",
        "category": "Fashion"
    },
    {
        "name": "Backpack",
        "price": 1499,
        "description": "Durable backpack with multiple compartments for work and travel.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 2599,
        "description": "Brew fresh coffee at home with one-touch operation.",
        "category": "Home"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 1999,
        "description": "Portable speaker with rich sound and waterproof design.",
        "category": "Electronics"
    }
]

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Choose Category",
    categories
)

# Shopping Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

cart_items = 3
cart_total = 8497

st.sidebar.write(f"Items: {cart_items}")
st.sidebar.write(f"Total: ₹{cart_total:,}")

# --------------------------------------------------
# Homepage Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛒 Welcome to MiniStore</h1>
    <p>Your one-stop destination for quality products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.header("Discover Amazing Products")

st.write(
    """
    Browse our carefully selected collection of electronics,
    fashion items, accessories, and home essentials.
    """
)
c1, c2, c3, c4 = st.columns(4)

c1.metric("🛍 Products", "6")
c2.metric("📂 Categories", "4")
c3.metric("👥 Customers", "5K+")
c4.metric("⭐ Rating", "4.9")

st.success("🔥 FLASH SALE: Up to 40% OFF on Electronics Today!")

# --------------------------------------------------
# Filter Products
# --------------------------------------------------
search = st.text_input(
    "🔍 Search Products",
    placeholder="Search products..."
)
if selected_category == "All":
    filtered_products = products
else:
        filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]
if search:
    filtered_products = [
        p for p in filtered_products
        if search.lower() in p["name"].lower()
    ]

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.subheader("⭐ Featured Products")

# Create responsive layout with columns
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="">
            <div class="category">{product['category']}</div>
            <div class="product-name">{product['name']}</div>
            <br>
            <div class="price">₹{product['price']:,}</div>
            <p>{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <hr>
    <p>© 2026 MiniStore | Demo E-Commerce Website Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)