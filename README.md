---
title: Shah's AI World
emoji: 🤖
colorFrom: purple
colorTo: pink
sdk: docker
pinned: false
---

# Shah's AI World

Your personal AI playground - a collection of powerful, interactive AI applications that bring cutting-edge AI capabilities to your fingertips. No complex setup, no coding required - just pure AI magic!

## What's Inside?

### 💬 AI Chatbot
Chat with state-of-the-art language models! Choose from multiple AI providers including DeepSeek, Google Gemini, and Claude. Features streaming responses, conversation history, and a clean chat interface.

### 📊 Software Diagram Generator
Transform your ideas into professional diagrams instantly! Describe your software architecture, database schema, or workflow in plain English, and watch as AI generates beautiful Mermaid diagrams. Perfect for:
- System architecture diagrams
- Sequence diagrams
- Flowcharts & ERDs
- Class diagrams

### 🎭 Personality Bot
Experience AI with character! Choose from 5 distinct personalities:
- **🎩 Professional Business Assistant** - Your corporate ally
- **✨ Creative Writing Helper** - Unleash your imagination
- **💻 Technical Expert** - Code & debug like a pro
- **🤗 Friendly Companion** - A warm chat buddy
- **🎓 Academic Scholar** - Research & learn

Each personality adapts its communication style, expertise, and responses to match your needs.

## Tech Stack

- **Frontend**: Streamlit
- **AI Integration**: OpenRouter API (access to multiple LLM providers)
- **Diagram Rendering**: Mermaid.js via streamlit-mermaid
- **Deployment**: Docker + Hugging Face Spaces

## Quick Start

### Live Demo
Visit the live app: [Shah's AI World on Hugging Face](https://huggingface.co/spaces/shaishavnshah/shah-toy-apps)

### Run Locally

1. Clone the repository:
```bash
git clone https://github.com/shaishav1010/ai-toy-apps.git
cd ai-toy-apps
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run "0_🏠_Home.py"
```

4. Open `http://localhost:8501` in your browser

### Get an API Key
All apps use OpenRouter for AI capabilities. Get your free API key at [openrouter.ai/keys](https://openrouter.ai/keys)

## Project Structure

```
ai-toy-apps/
├── 0_🏠_Home.py                    # Welcome page
├── pages/
│   ├── 1_🤖_AI_Chatbot.py          # Multi-model chatbot
│   ├── 2_📊_Diagram_Generator.py   # AI-powered diagram creator
│   └── 3_🎭_Personality_Bot.py     # Chat with AI personalities
├── requirements.txt
├── Dockerfile
└── .streamlit/config.toml
```

## Coming Soon

- 🔊 Speech Recognition
- 📝 Document Summarizer
- 🌐 Language Translator
- 📊 Data Analysis Tool

---

Made with ❤️ by Shah | Powered by AI
