import streamlit as st

st.set_page_config(
    page_title="Image Generator - Shah's AI World",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Text-to-Image Generator")

st.markdown("""
### Create Images from Text Descriptions

Transform your ideas into visual art using AI-powered image generation.
""")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Input")
    prompt = st.text_area(
        "Describe your image:",
        placeholder="e.g., A futuristic city at sunset with flying cars",
        height=100,
        disabled=True
    )

    col1_1, col1_2 = st.columns(2)
    with col1_1:
        style = st.selectbox(
            "Art Style:",
            ["Realistic", "Anime", "Oil Painting", "Digital Art", "3D Render"],
            disabled=True
        )

    with col1_2:
        size = st.selectbox(
            "Image Size:",
            ["512x512", "768x768", "1024x1024"],
            disabled=True
        )

    generate_btn = st.button("🎨 Generate Image", disabled=True, type="primary")

with col2:
    st.subheader("Settings")
    st.slider("Quality", 1, 10, 7, disabled=True)
    st.slider("Creativity", 1, 10, 5, disabled=True)
    st.number_input("Seed (for reproducibility)", value=42, disabled=True)

st.info("🚧 This feature is coming soon! Image generation capabilities will be added.")

st.markdown("---")
st.subheader("Gallery Preview")
st.caption("Examples of what you'll be able to create:")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🖼️ **Landscape Art**")
    st.text("Beautiful scenic views")

with col2:
    st.markdown("🎭 **Character Design**")
    st.text("Unique character concepts")

with col3:
    st.markdown("🏛️ **Architecture**")
    st.text("Futuristic buildings")