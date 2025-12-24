import streamlit as st
from openai import OpenAI
import json

st.set_page_config(
    page_title="Translator - Shah's AI World",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 AI Translator")

st.markdown("""
### Intelligent Translation with Cultural Context

Translate text between languages with automatic language detection, cultural notes, and alternative translations.
""")

# Available languages
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Turkish": "tr",
    "Polish": "pl",
    "Vietnamese": "vi",
    "Thai": "th",
    "Indonesian": "id",
    "Swedish": "sv",
    "Greek": "el",
}

# System prompt for translation
TRANSLATION_SYSTEM_PROMPT = """You are an expert multilingual translator with deep knowledge of cultural nuances and idiomatic expressions.

Your task is to:
1. DETECT the input language automatically
2. TRANSLATE the text to the target language specified by the user
3. Provide CULTURAL CONTEXT when relevant (idioms, formal/informal usage, regional variations)
4. Offer ALTERNATIVE TRANSLATIONS when there are multiple valid options
5. Rate your CONFIDENCE in the translation (High/Medium/Low)

IMPORTANT: Always respond in this exact JSON format:
{
    "detected_language": "Name of detected language",
    "confidence_detection": "High/Medium/Low",
    "original_text": "The original input text",
    "translated_text": "The main translation",
    "confidence_translation": "High/Medium/Low",
    "alternatives": ["Alternative translation 1", "Alternative translation 2"],
    "cultural_notes": "Any cultural context, idioms explained, regional variations, or usage notes. Leave empty string if not applicable.",
    "is_same_language": true/false
}

Rules:
- If the input language is the SAME as the target language, set "is_same_language" to true and provide the same text
- Always detect the language even if translation isn't needed
- For idioms and expressions, explain their meaning in the cultural notes
- Provide alternatives only when there are meaningfully different ways to express the same idea
- Be accurate and natural in translations - avoid literal word-for-word translation
- Consider formal vs informal register in your translations"""

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input(
        "OpenRouter API Key",
        type="password",
        placeholder="Enter your OpenRouter API key",
        help="Get your API key from https://openrouter.ai/keys"
    )

    st.markdown("---")

    # Model selection
    model_options = {
        "DeepSeek V3.2": "deepseek/deepseek-v3.2",
        "Google Gemini 2.5 Flash": "google/gemini-2.5-flash",
        "Claude Sonnet 4": "anthropic/claude-sonnet-4",
    }

    selected_model_name = st.selectbox(
        "Select Model",
        options=list(model_options.keys()),
        help="Choose an AI model"
    )

    selected_model = model_options[selected_model_name]
    st.caption(f"Model ID: `{selected_model}`")

    st.markdown("---")

    # Clear history button
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.translation_history = []
        st.rerun()

# Check for API key
if not api_key:
    st.warning("👈 Please enter your OpenRouter API key in the sidebar to start translating.")
    st.markdown("""
    **How to get an API key:**
    1. Go to [OpenRouter](https://openrouter.ai/)
    2. Sign up or log in
    3. Navigate to [API Keys](https://openrouter.ai/keys)
    4. Create a new key and paste it in the sidebar
    """)
    st.stop()

# Initialize OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "https://shahs-ai-world.hf.space",
        "X-Title": "Shah's AI World",
    }
)

# Initialize translation history
if "translation_history" not in st.session_state:
    st.session_state.translation_history = []

# Main translation interface
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Enter Text")
    input_text = st.text_area(
        "Type or paste text to translate:",
        placeholder="Enter text in any language...\n\nExamples:\n• Bonjour, comment allez-vous?\n• I love this weather\n• 今日は天気がいいですね",
        height=200,
        key="translation_input"
    )

    translate_btn = st.button("🌐 Translate", type="primary", use_container_width=True)

with col2:
    st.subheader("🎯 Translation")
    target_language = st.selectbox(
        "Translate to:",
        options=list(LANGUAGES.keys()),
        index=0,  # Default to English
        help="Select the language you want to translate to"
    )
    result_container = st.container()

# Process translation
if translate_btn and input_text:
    with result_container:
        with st.spinner("Translating..."):
            try:
                response = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": TRANSLATION_SYSTEM_PROMPT},
                        {"role": "user", "content": f"Translate the following text to {target_language}:\n\n{input_text}"}
                    ],
                    extra_headers={
                        "HTTP-Referer": "https://shahs-ai-world.hf.space",
                        "X-Title": "Shah's AI World"
                    },
                    extra_body={
                        "provider": {
                            "data_collection": "deny"
                        }
                    }
                )

                response_text = response.choices[0].message.content.strip()

                # Try to parse JSON response
                try:
                    # Clean up response if needed
                    if "```json" in response_text:
                        response_text = response_text.split("```json")[1].split("```")[0].strip()
                    elif "```" in response_text:
                        response_text = response_text.split("```")[1].split("```")[0].strip()

                    result = json.loads(response_text)

                    # Display results
                    st.markdown(f"**🔍 Detected Language:** {result.get('detected_language', 'Unknown')} ({result.get('confidence_detection', 'N/A')} confidence)")

                    st.markdown("---")

                    if result.get('is_same_language', False):
                        st.info("The input text is already in the target language.")
                        st.markdown(f"**📄 Text:** {result.get('original_text', input_text)}")
                    else:
                        st.markdown(f"### 🎯 Translation")
                        st.success(result.get('translated_text', 'Translation not available'))
                        st.caption(f"Confidence: {result.get('confidence_translation', 'N/A')}")

                    # Alternatives
                    alternatives = result.get('alternatives', [])
                    if alternatives and len(alternatives) > 0:
                        st.markdown("**🌟 Alternatives:**")
                        for alt in alternatives:
                            if alt:
                                st.markdown(f"• {alt}")

                    # Cultural notes
                    cultural_notes = result.get('cultural_notes', '')
                    if cultural_notes and cultural_notes.strip():
                        st.markdown("**💡 Cultural Notes:**")
                        st.info(cultural_notes)

                    # Add to history
                    st.session_state.translation_history.insert(0, {
                        "original": input_text,
                        "detected_lang": result.get('detected_language', 'Unknown'),
                        "target_lang": target_language,
                        "translation": result.get('translated_text', ''),
                        "alternatives": alternatives,
                        "cultural_notes": cultural_notes
                    })

                    # Keep only last 10 translations
                    st.session_state.translation_history = st.session_state.translation_history[:10]

                except json.JSONDecodeError:
                    # If JSON parsing fails, display raw response
                    st.markdown("### Translation Result")
                    st.write(response_text)

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key and try again.")

elif translate_btn and not input_text:
    with result_container:
        st.warning("Please enter text to translate.")

# Display placeholder when no translation yet
if not translate_btn:
    with result_container:
        st.markdown("""
        <div style='padding: 40px; text-align: center; color: #888; background: #f8f9fa; border-radius: 10px;'>
            <h3>Translation will appear here</h3>
            <p>Enter text on the left and click "Translate"</p>
        </div>
        """, unsafe_allow_html=True)

# Translation History
st.markdown("---")

if st.session_state.translation_history:
    with st.expander("📜 Translation History", expanded=False):
        for i, item in enumerate(st.session_state.translation_history):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{item['detected_lang']}:** {item['original'][:100]}{'...' if len(item['original']) > 100 else ''}")
            with col2:
                st.markdown(f"**{item['target_lang']}:** {item['translation'][:100]}{'...' if len(item['translation']) > 100 else ''}")
            if i < len(st.session_state.translation_history) - 1:
                st.divider()

# Quick language pairs
st.markdown("---")
with st.expander("🚀 Quick Translate Examples", expanded=len(st.session_state.translation_history) == 0):
    st.markdown("Click any example to try it:")

    examples = [
        ("Bonjour, comment allez-vous?", "French greeting"),
        ("I love this weather", "English casual"),
        ("Gracias por tu ayuda", "Spanish thanks"),
        ("Das Leben ist schön", "German phrase"),
        ("今日は天気がいいですね", "Japanese weather"),
        ("Ciao, come stai?", "Italian greeting"),
    ]

    cols = st.columns(3)
    for idx, (text, desc) in enumerate(examples):
        with cols[idx % 3]:
            if st.button(f"'{text[:20]}...' ({desc})", key=f"example_{idx}", use_container_width=True):
                st.session_state.translation_input = text
                st.rerun()

# Tips
with st.expander("💡 Translation Tips"):
    st.markdown("""
    - **Auto-Detection**: Just type in any language - the AI will detect it automatically
    - **Cultural Context**: The translator provides cultural notes for idioms and expressions
    - **Alternatives**: When multiple translations are valid, you'll see alternatives
    - **Formal vs Casual**: The AI considers register and formality in translations
    - **Best Results**: Provide complete sentences for more accurate translations
    """)
