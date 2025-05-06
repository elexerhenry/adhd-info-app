import streamlit as st

# Page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    [data-testid="stExpander"] summary {
        font-size: 26px !important;
        font-weight: bold !important;
        color: white !important;
    }

    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 12px 0px;
        padding: 4px;
    }

    /* Optional: style the expander content */
    .stMarkdown {
        color: white;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

for label, description in adhd_effects.items():
    with st.expander(label):
        st.write(description)
