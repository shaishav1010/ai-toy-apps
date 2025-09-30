---
title: Shah's AI World
emoji: 🤖
colorFrom: purple
colorTo: pink
sdk: docker
pinned: false
---

# Shah's AI World

A collection of AI-powered toy applications built with Streamlit.

## Features

- Multi-page Streamlit application
- Interactive AI demos
- Easy navigation through sidebar
- Responsive design

## Project Structure

```
ai-toy-apps/
├── 0_🏠_Home.py              # Main entry point (Home page)
├── pages/                     # Additional pages
│   ├── 1_🤖_AI_Chatbot.py
│   └── 2_🎨_Image_Generator.py
├── requirements.txt           # Python dependencies
├── Dockerfile                 # For Docker/Hugging Face deployment
└── .streamlit/               # Streamlit configuration
    └── config.toml
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run "0_🏠_Home.py"
```

3. Open your browser to `http://localhost:8501`

## Deployment

### Hugging Face Spaces

This app is configured to run on Hugging Face Spaces using Docker. The Dockerfile is pre-configured for optimal deployment.

### Streamlit Cloud

1. Push your code to GitHub
2. Connect your GitHub repo to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Docker Deployment

Build and run the Docker container:
```bash
docker build -t ai-toy-apps .
docker run -p 8501:8501 ai-toy-apps
```

## Adding New Apps

To add a new AI toy app:
1. Create a new Python file in the `pages/` directory
2. Follow the naming convention: `[number]_[emoji]_[PageName].py`
3. The page will automatically appear in the sidebar navigation

Example:
```python
# pages/3_🔮_Future_Predictor.py
import streamlit as st

st.set_page_config(page_title="Future Predictor", page_icon="🔮")
st.title("🔮 Future Predictor")
# Your app code here
```