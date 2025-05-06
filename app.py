services:
  - type: web
    name: my-streamlit-app
    env: python
    buildCommand: ""
    startCommand: streamlit run app.py --server.port=$PORT --server.enableCORS=false
    plan: free
import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS and JS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 15px 0;
        padding: 5px;
    }

    .stMarkdown {
        font-size: 18px;
        color: white;
    }
    </style>

    <script>
    window.addEventListener('load', function() {
        const expanders = window.parent.document.querySelectorAll('summary');
        expanders.forEach(e => {
            e.style.fontSize = '30px';
            e.style.fontWeight = 'bold';
            e.style.color = 'white';
            e.style.border = '2px solid white';
            e.style.borderRadius = '6px';
            e.style.padding = '12px';
            e.style.marginBottom = '4px';
        });
    });
    </script>
""", unsafe_allow_html=True)

# Title and instructions
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# ADHD effects content
adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

# Render dropdowns
for label, description in adhd_effects.items():
    with st.expander(label):
        st.markdown(f"<div style='font-size: 18px; color: white;'>{description}</div>", unsafe_allow_html=True)
