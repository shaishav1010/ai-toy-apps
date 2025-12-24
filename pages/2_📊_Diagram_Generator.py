import streamlit as st
import re
from openai import OpenAI
from streamlit_mermaid import st_mermaid

st.set_page_config(
    page_title="Diagram Generator - Shah's AI World",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Software Diagram Generator")

st.markdown("""
### Create Software Architecture & Design Diagrams

Generate professional software diagrams from text descriptions using AI.
Supports architecture diagrams, flowcharts, sequence diagrams, ERDs, and more.
""")

# System prompt to restrict to software diagrams only
SYSTEM_PROMPT = """You are a software diagram expert that generates Mermaid diagram code.

IMPORTANT RULES:
1. You ONLY create software-related diagrams including:
   - Software architecture diagrams
   - System design diagrams
   - Flowcharts for algorithms/processes
   - Sequence diagrams
   - Class diagrams
   - Entity-Relationship diagrams (ERD)
   - State diagrams
   - Component diagrams
   - Deployment diagrams
   - API flow diagrams
   - Database schemas
   - Network architecture diagrams

2. You must REFUSE any request that is NOT related to software/technical diagrams. This includes:
   - General artwork or illustrations
   - Photos or realistic images
   - Non-technical diagrams
   - Any image generation that isn't a software/technical diagram

   For refused requests, respond with: "I can only generate software and technical diagrams. Please describe a software architecture, flowchart, sequence diagram, or other technical diagram you'd like me to create."

3. Always output valid Mermaid syntax wrapped in ```mermaid code blocks.

4. After the diagram code, provide a brief explanation of the diagram components.

5. Keep diagrams clean and readable - don't overcomplicate them.
"""

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

    # Model selection - choosing models good at structured output/code generation
    model_options = {
        "DeepSeek V3.2": "deepseek/deepseek-v3.2",
        "Google Gemini 2.5 Flash": "google/gemini-2.5-flash",
        "Claude Sonnet 4": "anthropic/claude-sonnet-4",
    }

    selected_model_name = st.selectbox(
        "Select Model",
        options=list(model_options.keys()),
        help="Choose an AI model for diagram generation"
    )

    selected_model = model_options[selected_model_name]

    st.caption(f"Model ID: `{selected_model}`")

    st.markdown("---")

    # Diagram type helper
    st.subheader("📋 Diagram Types")
    st.markdown("""
    - **Flowchart** - Process flows
    - **Sequence** - Interactions
    - **Class** - OOP structure
    - **ERD** - Database design
    - **State** - State machines
    - **Architecture** - System overview
    """)

# Check for API key
if not api_key:
    st.warning("👈 Please enter your OpenRouter API key in the sidebar to start generating diagrams.")
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

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Describe Your Diagram")

    prompt = st.text_area(
        "What diagram would you like to create?",
        placeholder="e.g., Create a sequence diagram showing user authentication flow with login, token generation, and session management",
        height=150
    )

    # Example prompts
    with st.expander("💡 Example Prompts"):
        st.markdown("""
        **Architecture Diagram:**
        > "Create a microservices architecture for an e-commerce platform with API gateway, user service, product service, order service, and database"

        **Sequence Diagram:**
        > "Show the OAuth 2.0 authorization code flow between user, client app, auth server, and resource server"

        **Flowchart:**
        > "Create a flowchart for a CI/CD pipeline with build, test, staging deployment, and production deployment stages"

        **ERD:**
        > "Design a database schema for a blog platform with users, posts, comments, and tags"

        **Class Diagram:**
        > "Create a class diagram for a payment processing system with Payment, CreditCard, PayPal, and Transaction classes"
        """)

    generate_btn = st.button("📊 Generate Diagram", type="primary", use_container_width=True)

with col2:
    diagram_placeholder = st.container()

# Initialize session state for storing generated response
if "diagram_response" not in st.session_state:
    st.session_state.diagram_response = ""

if "show_preview" not in st.session_state:
    st.session_state.show_preview = False

# Function to extract mermaid code from response
def extract_mermaid_code(text):
    """Extract Mermaid code from markdown code blocks."""
    pattern = r'```mermaid\s*([\s\S]*?)\s*```'
    matches = re.findall(pattern, text)
    return matches[0].strip() if matches else None

# Generate diagram
if generate_btn and prompt:
    with diagram_placeholder:
        with st.spinner("Generating diagram..."):
            try:
                response = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ],
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

                # Store response in session state
                st.session_state.diagram_response = response_text

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key and try again.")

elif generate_btn and not prompt:
    st.warning("Please enter a description for your diagram.")

# Show preview button and render diagram if response exists
if st.session_state.diagram_response:
    st.markdown("---")

    mermaid_code = extract_mermaid_code(st.session_state.diagram_response)

    if mermaid_code:
        if st.session_state.show_preview:
            # Preview mode - show rendered diagram
            st.subheader("Diagram Preview")
            st_mermaid(mermaid_code, height="500px")
            if st.button("📝 Back to Code", type="secondary", use_container_width=True):
                st.session_state.show_preview = False
                st.rerun()
        else:
            # Code mode - show the raw response with code and explanation
            st.subheader("Generated Code & Explanation")
            st.markdown(st.session_state.diagram_response)
            if st.button("👁️ Preview Diagram", type="secondary", use_container_width=True):
                st.session_state.show_preview = True
                st.rerun()
    else:
        st.info("No Mermaid diagram code found in the response.")
