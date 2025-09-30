import streamlit as st

st.set_page_config(
    page_title="AI Chatbot - Shah's AI World",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Chatbot Assistant")

st.markdown("""
### Interactive AI Conversation

This page will feature an AI-powered chatbot that can help with various tasks:
- Answer questions
- Generate creative content
- Provide coding assistance
- And much more!
""")

st.info("🚧 This feature is coming soon! Stay tuned for updates.")

chat_container = st.container()
with chat_container:
    st.markdown("#### Sample Chat Interface")

    messages = st.container()
    with messages:
        st.chat_message("assistant").write("Hello! I'm your AI assistant. How can I help you today?")
        st.chat_message("user").write("Can you explain what machine learning is?")
        st.chat_message("assistant").write("Machine learning is a subset of AI that enables computers to learn from data...")

    with st.container():
        user_input = st.text_input("Type your message here...", disabled=True)
        st.caption("Chat functionality will be enabled soon")