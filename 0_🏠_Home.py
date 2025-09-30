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
    .feature-card {
        padding: 20px;
        border-radius: 8px;
        background: #f0f2f6;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    <div class="welcome-box">
        <h2>Welcome to the AI Playground! 🚀</h2>
        <p>Explore cutting-edge AI applications and interactive demos</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.header("🎯 What You'll Find Here")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🤖 AI Models
    - Language Models
    - Computer Vision
    - Audio Processing
    - Multi-modal AI
    """)

with col2:
    st.markdown("""
    ### 🛠️ Interactive Tools
    - Text Generation
    - Image Analysis
    - Data Visualization
    - Custom AI Solutions
    """)

st.markdown("---")

st.header("🚀 Coming Soon")

upcoming_features = [
    "💬 AI Chatbot Assistant",
    "🎨 Text-to-Image Generator",
    "📊 Data Analysis Tool",
    "🔊 Speech Recognition",
    "📝 Document Summarizer",
    "🌐 Language Translator"
]

cols = st.columns(3)
for i, feature in enumerate(upcoming_features):
    with cols[i % 3]:
        st.info(feature)

st.markdown("---")

st.subheader("📌 About This Platform")
st.markdown("""
This platform showcases various AI-powered applications and tools.
Each app is designed to demonstrate different aspects of artificial intelligence,
making complex AI concepts accessible and interactive.

**Built with:** Streamlit, Python, and various AI frameworks
""")

footer = """
<div style='text-align: center; padding: 20px; color: #666;'>
    <p>Made with ❤️ by Shah | Powered by AI</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)