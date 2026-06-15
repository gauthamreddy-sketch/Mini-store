import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero {
    background: linear-gradient(135deg,#6366f1,#8b5cf6);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 10px 30px rgba(99,102,241,0.3);
}

.product-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: all 0.3s ease;
    min-height: 260px;
}

.product-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 15px 35px rgba(139,92,246,0.3);
}

.product-name {
    font-size: 22px;
    font-weight: bold;
    color: #111827;
}

.price {
    color: #16a34a;
    font-size: 26px;
    font-weight: bold;
}

.category {
    display: inline-block;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    padding: 6px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
    font-size: 13px;
}

.product-card p {
    color: #4b5563;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

products = [
    {"name":"🎧 Wireless Headphones","price":2999,"category":"Electronics","description":"Premium noise-cancelling headphones with 40-hour battery life."},
    {"name":"⌚ Smart Watch","price":4999,"category":"Electronics","description":"Track fitness, notifications and health metrics."},
    {"name":"👟 Running Shoes","price":3499,"category":"Fashion","description":"Comfortable lightweight shoes for everyday running."},
    {"name":"🎒 Backpack","price":1499,"category":"Accessories","description":"Durable backpack with multiple compartments."},
    {"name":"☕ Coffee Maker","price":2599,"category":"Home","description":"Brew fresh coffee with one-touch operation."},
    {"name":"🔊 Bluetooth Speaker","price":1999,"category":"Electronics","description":"Portable speaker with rich sound and waterproof design."}
]

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(list(set([p["category"] for p in products])))

selected_category = st.sidebar.selectbox(
    "Choose Category",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")
st.sidebar.write("Items: 3")
st.sidebar.write("Total: ₹8,497")

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div class="hero">
<h1>🛒 Welcome to MiniStore</h1>
<p>Your one-stop destination for quality products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

st.info("🚚 Free Delivery Above ₹2,999 | 🔒 Secure Checkout | ⭐ Rated 4.9/5")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("✨ Discover Amazing Products")

st.write(
    "Browse our collection of electronics, fashion, accessories and home essentials."
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("🛍 Products","6")
c2.metric("📂 Categories","4")
c3.metric("👥 Customers","5K+")
c4.metric("⭐ Rating","4.9")

st.success("🔥 FLASH SALE: Up to 40% OFF on Electronics Today!")

# --------------------------------------------------
# SEARCH
# --------------------------------------------------

search = st.text_input(
    "🔍 Search Products",
    placeholder="Search products..."
)

# --------------------------------------------------
# FILTER
# --------------------------------------------------

if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

if search:
    filtered_products = [
        p for p in filtered_products
        if search.lower() in p["name"].lower()
    ]

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

st.subheader("⭐ Featured Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="category">{product['category']}</div>
            <div class="product-name">{product['name']}</div>
            <br>
            <div class="price">₹{product['price']:,}</div>
            <p>{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)
st.page_link(
    "pages/1_Support_Chatbot.py",
    label="💬 Open Support Chatbot",
    icon="💬"
)
st.markdown("""
<style>
.support-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #7C3AED;
    color: white;
    padding: 12px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 9999;
}
</style>

<a href="/Support_Chatbot" target="_self" class="support-btn">
💬 Support
</a>
""", unsafe_allow_html=True)
# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
<hr>
<p>🛍 MiniStore • Quality Products • Fast Delivery • Secure Shopping</p>
<p>© 2026 MiniStore</p>
</div>
""", unsafe_allow_html=True)