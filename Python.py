import streamlit as st
from datetime import datetime

# Configure the wishing card
st.set_page_config(page_title="Digital Wishing Card", page_icon="💌")

# Custom styling
st.markdown("""
<style>
    .wish-card {
        border: 2px solid #FF69B4;
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        background-color: #FFF0F5;
    }
    .message {font-size: 18px; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

# Header
st.title("💌 Wishing Card for [Name]")
st.subheader("Leave your heartfelt message below")

# Message input
with st.form("wish_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Message (max 140 characters)", max_chars=140)
    emoji = st.selectbox("Add an emoji", ["❤️", "🎉", "🎁", "🌟", "🥂", "✨"])
    submitted = st.form_submit_button("Add Your Wish 💖")

# Store messages in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Handle submission
if submitted and message:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    wish = {
        "name": name if name else "Anonymous",
        "message": message,
        "emoji": emoji,
        "timestamp": timestamp
    }
    st.session_state.messages.append(wish)
    st.balloons()
    st.success("Thank you for your wish! 🌸")

# Display messages
st.header("Messages from Well-Wishers")
for msg in reversed(st.session_state.messages):  # Show newest first
    st.markdown(f"""
    <div class="wish-card">
        <div class="message">
            {msg['emoji']} {msg['message']}
        </div>
        <div style="color: #FF69B4; text-align: right;">
            ~ {msg['name']} ({msg['timestamp']})
        </div>
    </div>
    """, unsafe_allow_html=True)

# Empty state
if not st.session_state.messages:
    st.info("No wishes yet - be the first to leave one! 💬")
