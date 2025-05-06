import streamlit as st

# Set page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS
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

    [data-testid="stExpander"] summary {
        font-size: 30px !important;
        font-weight: bold !important;
        color: white !important;
    }

    .stMarkdown {
        font-size: 18px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App title and intro
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# ADHD info dictionary
adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

# Render expanders with large, styled labels
for label, description in adhd_effects.items():
    # Use HTML in label to enlarge font
    styled_label = f"<span style='font-size: 30px; font-weight: bold; color: white;'>{label}</span>"
    with st.expander(label=styled_label):
        st.markdown(f"<div style='font-size: 18px; color: white;'>{description}</div>", unsafe_allow_html=True)
