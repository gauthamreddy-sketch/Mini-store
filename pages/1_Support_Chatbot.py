import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about products, delivery, refunds, returns...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    user_text = prompt.lower()

    if "wireless headphones" in user_text:
        response = "🎧 Wireless Headphones cost ₹2,999 and include 40-hour battery life."

    elif "smart watch" in user_text:
        response = "⌚ Smart Watch costs ₹4,999 and tracks fitness and health metrics."

    elif "running shoes" in user_text:
        response = "👟 Running Shoes cost ₹3,499 and are designed for daily running."

    elif "backpack" in user_text:
        response = "🎒 Backpack costs ₹1,499 and is ideal for work and travel."

    elif "coffee maker" in user_text:
        response = "☕ Coffee Maker costs ₹2,599 with one-touch brewing."

    elif "bluetooth speaker" in user_text:
        response = "🔊 Bluetooth Speaker costs ₹1,999 and is waterproof."

    elif "delivery" in user_text:
        response = "🚚 Delivery usually takes 3–5 business days."

    elif "refund" in user_text:
        response = "💰 Refunds are processed within 5–7 business days."

    elif "return" in user_text:
        response = "📦 Products can be returned within 7 days of delivery."

    elif "payment" in user_text:
        response = "💳 We accept UPI, Credit Cards, Debit Cards and Net Banking."

    elif "order status" in user_text:
        response = "📍 Your order status can be tracked from your account dashboard."

    elif "product" in user_text:
        response = """
Available products:

🎧 Wireless Headphones - ₹2,999
⌚ Smart Watch - ₹4,999
👟 Running Shoes - ₹3,499
🎒 Backpack - ₹1,499
☕ Coffee Maker - ₹2,599
🔊 Bluetooth Speaker - ₹1,999
"""

    else:
        response = "🤖 I can help with products, delivery, refunds, returns, payments and order status."

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )