import streamlit as st

st.set_page_config(
    page_title="Home - Shah's AI World",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌟 Welcome to Shah's AI World! 🌟")

st.markdown("""
<style>
    .welcome-box {
        padding: 30px;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin: 20px 0;
    }
    .app-card {
        padding: 20px;
        border-radius: 10px;
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        margin: 10px 0;
        height: 100%;
    }
    .app-card h3 {
        margin-top: 0;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    <div class="welcome-box">
        <h2>Your Personal AI Playground! 🚀</h2>
        <p>Powerful AI tools at your fingertips - no coding required</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.header("🎯 Explore Our AI Apps")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 💬 AI Chatbot

    Chat with cutting-edge language models!

    **Features:**
    - Multiple AI models (DeepSeek, Gemini, Claude)
    - Streaming responses
    - Conversation history

    *Perfect for Q&A, brainstorming, and creative tasks*
    """)
    st.page_link("pages/1_🤖_AI_Chatbot.py", label="Launch Chatbot →", icon="🤖")

with col2:
    st.markdown("""
    ### 📊 Diagram Generator

    Transform ideas into professional diagrams!

    **Create:**
    - Architecture & sequence diagrams
    - Flowcharts & ERDs
    - Class diagrams

    *Describe in plain English, get Mermaid diagrams*
    """)
    st.page_link("pages/2_📊_Diagram_Generator.py", label="Launch Diagram Generator →", icon="📊")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### 🎭 Personality Bot

    Chat with AI that has character!

    **5 Personalities:**
    - 🎩 Business Pro • ✨ Creative Writer
    - 💻 Tech Expert • 🤗 Friendly Companion
    - 🎓 Academic Scholar

    *Each adapts style & expertise to your needs*
    """)
    st.page_link("pages/3_🎭_Personality_Bot.py", label="Launch Personality Bot →", icon="🎭")

with col4:
    st.markdown("""
    ### 🌐 AI Translator

    Intelligent translation with context!

    **Features:**
    - Auto language detection
    - 20+ languages supported
    - Cultural notes & idioms
    - Alternative translations

    *More than translation - understand the culture*
    """)
    st.page_link("pages/4_🌐_Translator.py", label="Launch Translator →", icon="🌐")

st.markdown("---")

st.header("🚀 Coming Soon")

upcoming_features = [
    ("🔊 Speech Recognition", "Convert speech to text with AI"),
    ("📝 Document Summarizer", "Get key insights from long documents"),
    ("📊 Data Analysis Tool", "Upload CSV & get AI-powered insights"),
]

cols = st.columns(3)
for i, (feature, desc) in enumerate(upcoming_features):
    with cols[i]:
        st.info(f"**{feature}**\n\n{desc}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 Getting Started")
    st.markdown("""
    All apps use **OpenRouter** for AI capabilities.

    1. Get your free API key at [openrouter.ai/keys](https://openrouter.ai/keys)
    2. Choose an app from the sidebar
    3. Paste your API key and start exploring!

    *Free tier includes access to powerful models like DeepSeek*
    """)

with col2:
    st.subheader("📌 About This Platform")
    st.markdown("""
    Shah's AI World showcases interactive AI applications
    that make powerful AI accessible to everyone.

    **Built with:**
    - Streamlit for the UI
    - OpenRouter for multi-model AI access
    - Mermaid.js for diagram rendering
    - Docker for deployment
    """)

footer = """
<div style='text-align: center; padding: 20px; color: #666;'>
    <p>Made with ❤️ by Shah | Powered by AI</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
