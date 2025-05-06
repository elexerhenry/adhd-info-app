import streamlit as st

# Page configuration
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Custom CSS
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
""", unsafe_allow_html=True)

# App title and instructions
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# ADHD information
adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

# Dropdowns with large internal headers
for label, description in adhd_effects.items():
    with st.expander(" "):  # visually empty label
        st.markdown(
            f"<div style='font-size: 32px; font-weight: bold; color: white; margin-bottom: 10px;'>{label}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div style='font-size: 18px; color: white;'>{description}</div>",
            unsafe_allow_html=True
        )
