import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject CSS and JavaScript to force expander title font size
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
    window.onload = function() {
        const summaries = window.parent.document.querySelectorAll('summary');
        summaries.forEach(s => {
            s.style.fontSize = '30px';
            s.style.fontWeight = 'bold';
            s.style.color = 'white';
            s.style.border = '2px solid white';
            s.style.borderRadius = '6px';
            s.style.padding = '10px';
        });
    }
    </script>
""", unsafe_allow_html=True)

st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

for label, description in adhd_effects.items():
    with st.expander(label):
        st.markdown(f"<div style='font-size: 18px; color: white;'>{description}</div>", unsafe_allow_html=True)
