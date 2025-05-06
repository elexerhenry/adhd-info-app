import streamlit as st

# Page setup
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Custom background styling
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }
    .dropdown-title {
        font-size: 30px;
        font-weight: bold;
        color: white;
        margin-bottom: 0.5rem;
    }
    .dropdown-content {
        font-size: 18px;
        color: white;
    }
    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 15px 0;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# ADHD topics and their descriptions
adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

# Build expanders with styled titles inside
for label, description in adhd_effects.items():
    with st.expander(""):
        st.markdown(f"<div class='dropdown-title'>{label}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dropdown-content'>{description}</div>", unsafe_allow_html=True)
