import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

PRODUCT_CATALOG = """
MiniStore Products:

1. Wireless Headphones
   Price: ₹2,999
   Features: Noise cancellation, 40-hour battery life

2. Smart Watch
   Price: ₹4,999
   Features: Fitness tracking, notifications, health monitoring

3. Running Shoes
   Price: ₹3,499
   Features: Lightweight, daily running comfort

4. Backpack
   Price: ₹1,499
   Features: Durable, travel and work friendly

5. Coffee Maker
   Price: ₹2,599
   Features: One-touch brewing

6. Bluetooth Speaker
   Price: ₹1,999
   Features: Waterproof, portable, rich sound
"""

SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

You only answer questions related to:
- Products
- Orders
- Delivery
- Refunds
- Returns
- Payments
- Order Tracking

Product Information:
{PRODUCT_CATALOG}

Rules:
1. Only answer MiniStore related questions.
2. Politely refuse unrelated questions.
3. Be professional and helpful.
4. Use the product catalog when answering.
5. Never invent products.
"""

st.title("💬 MiniStore Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Ask about products, delivery, refunds, returns..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.3
    )

    assistant_reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )