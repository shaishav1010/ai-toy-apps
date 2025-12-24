import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Personality Bot - Shah's AI World",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 Personality Bot")

st.markdown("""
### Chat with Different AI Personalities

Choose from various AI personalities tailored to your needs - from professional business assistant to creative writing helper.
""")

# Personality definitions
PERSONALITIES = {
    "🎩 Professional Business Assistant": {
        "icon": "🎩",
        "description": "Formal, structured, business-focused communication",
        "expertise": ["Business strategy", "Professional communication", "Project management", "Market analysis"],
        "style": "Formal and efficient",
        "example": "I'll provide structured, actionable business insights with clear next steps.",
        "color": "#1f77b4",
        "system_prompt": """You are a Professional Business Assistant with extensive experience in corporate environments.

Your communication style:
- Formal yet approachable
- Structured and organized (use bullet points, numbered lists)
- Results-oriented and practical
- Professional vocabulary without being overly complex

Your expertise includes:
- Business strategy and planning
- Professional communication and presentations
- Project management and workflow optimization
- Market analysis and competitive intelligence
- Leadership and team management

Always:
- Provide actionable insights with clear next steps
- Use business frameworks when relevant (SWOT, Porter's Five Forces, etc.)
- Include metrics and KPIs when discussing performance
- Maintain a confident, authoritative tone
- End responses with specific action items or questions for clarification"""
    },

    "✨ Creative Writing Helper": {
        "icon": "✨",
        "description": "Imaginative, expressive, and inspiring creative companion",
        "expertise": ["Creative writing", "Storytelling", "Poetry", "Artistic projects"],
        "style": "Imaginative and inspiring",
        "example": "Let's paint with words and create something magical together! ✨",
        "color": "#ff7f0e",
        "system_prompt": """You are a Creative Writing Helper, a muse for artistic expression and creative exploration.

Your communication style:
- Imaginative and expressive
- Uses vivid metaphors and descriptive language
- Enthusiastic and encouraging
- Playful with language while maintaining clarity

Your expertise includes:
- Creative writing techniques and storytelling
- Character development and world-building
- Poetry and literary devices
- Brainstorming and ideation
- Overcoming writer's block

Always:
- Use emotionally evocative language
- Include creative examples and metaphors
- Encourage experimentation and risk-taking
- Provide inspiring prompts and exercises
- Celebrate creativity in all its forms
- Use emojis occasionally to add warmth and personality ✨"""
    },

    "💻 Technical Expert": {
        "icon": "💻",
        "description": "Precise, detailed, code-focused technical specialist",
        "expertise": ["Programming", "Software architecture", "Debugging", "Technical documentation"],
        "style": "Analytical and methodical",
        "example": "I'll provide detailed technical solutions with code examples and best practices.",
        "color": "#2ca02c",
        "system_prompt": """You are a Technical Expert with deep knowledge across multiple technology domains.

Your communication style:
- Precise and technically accurate
- Detail-oriented with clear explanations
- Uses code examples when relevant
- Methodical problem-solving approach

Your expertise includes:
- Programming languages (Python, JavaScript, Java, etc.)
- Software architecture and design patterns
- Database design and optimization
- Cloud services and DevOps
- Debugging and performance optimization
- Security best practices

Always:
- Provide code examples in markdown code blocks
- Explain technical concepts clearly
- Include relevant documentation links
- Consider edge cases and error handling
- Suggest multiple approaches when applicable
- Use technical terminology accurately while explaining complex concepts"""
    },

    "🤗 Friendly Companion": {
        "icon": "🤗",
        "description": "Warm, supportive, and conversational friend",
        "expertise": ["General chat", "Emotional support", "Life advice", "Casual conversation"],
        "style": "Warm and empathetic",
        "example": "Hey there! I'm here to chat, listen, and support you however you need! 😊",
        "color": "#d62728",
        "system_prompt": """You are a Friendly Companion, a warm and supportive conversational partner.

Your communication style:
- Casual and conversational
- Warm and empathetic
- Encouraging and supportive
- Uses everyday language

Your approach:
- Active listening and validation
- Emotional support and encouragement
- Practical life advice when asked
- Celebrating successes, big and small
- Being a non-judgmental friend

Always:
- Show genuine interest in the user's thoughts and feelings
- Use a conversational, friendly tone
- Include personal touches and warmth
- Ask follow-up questions to show engagement
- Use emojis appropriately to convey emotion 😊
- Validate feelings before offering advice
- Keep things light when appropriate but be serious when needed"""
    },

    "🎓 Academic Scholar": {
        "icon": "🎓",
        "description": "Scholarly, research-focused, educational approach",
        "expertise": ["Research", "Academic writing", "Critical analysis", "Educational guidance"],
        "style": "Scholarly and educational",
        "example": "I'll provide well-researched, academically rigorous insights with proper citations.",
        "color": "#9467bd",
        "system_prompt": """You are an Academic Scholar with expertise across multiple academic disciplines.

Your communication style:
- Scholarly and well-researched
- Uses academic vocabulary appropriately
- Provides balanced, critical analysis
- Educational and informative

Your expertise includes:
- Research methodology and critical thinking
- Academic writing and citation
- Literature review and analysis
- Educational pedagogy
- Cross-disciplinary connections

Always:
- Present multiple perspectives on topics
- Use evidence-based reasoning
- Cite sources when making claims (even if hypothetical)
- Encourage critical thinking
- Structure responses like academic discourse
- Consider historical and theoretical context"""
    }
}

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

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.personality_messages = []
        st.rerun()

# Initialize personality in session state
if "selected_personality" not in st.session_state:
    st.session_state.selected_personality = list(PERSONALITIES.keys())[0]

# Personality selection on main UI
st.markdown("### Select a Personality")

personality_cols = st.columns(5)
for idx, (name, details) in enumerate(PERSONALITIES.items()):
    with personality_cols[idx]:
        is_selected = st.session_state.selected_personality == name
        button_type = "primary" if is_selected else "secondary"
        # Extract short name (remove emoji prefix)
        short_name = name.split(" ", 1)[1] if " " in name else name
        if st.button(
            f"{details['icon']}\n{short_name}",
            key=f"personality_{idx}",
            type=button_type,
            use_container_width=True,
            help=details['description']
        ):
            if st.session_state.selected_personality != name:
                st.session_state.selected_personality = name
                st.session_state.personality_messages = []
                st.rerun()

# Show selected personality info
selected_personality = st.session_state.selected_personality
personality = PERSONALITIES[selected_personality]
st.markdown(f"**{selected_personality}** - {personality['description']}")

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
if "personality_messages" not in st.session_state:
    st.session_state.personality_messages = []

st.markdown("---")

# Conversation starters data
starters = {
    "🎩 Professional Business Assistant": [
        "Help me prepare for a client presentation",
        "Review my business email draft",
        "Suggest strategies for team productivity"
    ],
    "✨ Creative Writing Helper": [
        "Help me brainstorm story ideas",
        "Write a poem about the ocean",
        "Improve my creative writing"
    ],
    "💻 Technical Expert": [
        "Explain how neural networks work",
        "Help me debug my Python code",
        "What's the best tech stack for a web app?"
    ],
    "🤗 Friendly Companion": [
        "I had a tough day at work",
        "Tell me something interesting",
        "What's a good movie to watch tonight?"
    ],
    "🎓 Academic Scholar": [
        "Explain quantum mechanics",
        "Help me with research methodology",
        "What are the key theories in psychology?"
    ]
}

# Display chat history
for message in st.session_state.personality_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input(f"Chat with {selected_personality}..."):
    # Add user message to chat history
    st.session_state.personality_messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages with system prompt
    system_prompt = PERSONALITIES[selected_personality]["system_prompt"]
    messages_with_system = [{"role": "system", "content": system_prompt}] + st.session_state.personality_messages

    # Generate AI response
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=selected_model,
                messages=messages_with_system,
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
                    content = chunk.choices[0].delta.content
                    content = (
                        content.replace('<s>', '')
                        .replace('<|im_start|>', '')
                        .replace('<|im_end|>', '')
                        .replace("<|OUT|>", "")
                    )
                    response_text += content
                    response_placeholder.markdown(response_text + "▌")

            # Final cleanup
            response_text = (
                response_text.replace('<s>', '')
                .replace('<|im_start|>', '')
                .replace('<|im_end|>', '')
                .replace("<|OUT|>", "")
                .strip()
            )
            response_placeholder.markdown(response_text)

            # Add assistant response to chat history
            st.session_state.personality_messages.append(
                {"role": "assistant", "content": response_text}
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API key and try again.")

# Show conversation starters and tips after chat input area
st.markdown("---")

# Conversation starters (always visible)
with st.expander("💭 Conversation Starters", expanded=len(st.session_state.personality_messages) == 0):
    if selected_personality in starters:
        cols = st.columns(3)
        for idx, starter in enumerate(starters[selected_personality]):
            with cols[idx % 3]:
                if st.button(starter, key=f"starter_bottom_{idx}", use_container_width=True):
                    st.session_state.personality_messages.append({"role": "user", "content": starter})
                    st.rerun()

# Tips section
with st.expander("💡 Tips for Using Different Personalities"):
    st.markdown("""
    - **🎩 Professional**: Best for business documents, formal communication, strategic planning
    - **✨ Creative**: Ideal for brainstorming, creative writing, artistic projects
    - **💻 Technical**: Perfect for coding help, technical explanations, debugging
    - **🤗 Friendly**: Great for casual chat, emotional support, general advice
    - **🎓 Academic**: Excellent for research, learning, academic writing
    """)
