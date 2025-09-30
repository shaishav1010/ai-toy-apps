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

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

## Deployment on Hugging Face Spaces

This app is configured to run on Hugging Face Spaces using Docker.

## Adding New Apps

To add a new toy app:
1. Create a new Python file in the `pages/` directory
2. Add the page to the navigation in `app.py`