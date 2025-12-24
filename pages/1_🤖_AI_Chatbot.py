import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Chatbot - Shah's AI World",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Chatbot Assistant")

st.markdown("""
### Interactive AI Conversation

Chat with various AI models powered by OpenRouter. Enter your API key and select a model to get started.
""")

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

    # Model selection dropdown
    model_options = {
        "DeepSeek V3.2": "deepseek/deepseek-v3.2",
        "Google Gemini 2.5 Flash": "google/gemini-2.5-flash",
        "Claude Sonnet 4": "anthropic/claude-sonnet-4",
    }

    selected_model_name = st.selectbox(
        "Select Model",
        options=list(model_options.keys()),
        help="Choose an AI model for the conversation"
    )

    selected_model = model_options[selected_model_name]

    st.caption(f"Model ID: `{selected_model}`")

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Check for API key
if not api_key:
    st.warning("👈 Please enter your OpenRouter API key in the sidebar to start chatting.")
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

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True,
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

            # Stream the response
            response_text = ""
            response_placeholder = st.empty()

            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    # Clean up unwanted tokens
                    content = chunk.choices[0].delta.content
                    content = (
                        content.replace('<s>', '')
                        .replace('<|im_start|>', '')
                        .replace('<|im_end|>', '')
                        .replace("<|OUT|>", "")
                    )
                    response_text += content
                    response_placeholder.markdown(response_text + "▌")

            # Final cleanup of response text
            response_text = (
                response_text.replace('<s>', '')
                .replace('<|im_start|>', '')
                .replace('<|im_end|>', '')
                .replace("<|OUT|>", "")
                .strip()
            )
            response_placeholder.markdown(response_text)

            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API key and try again.")
