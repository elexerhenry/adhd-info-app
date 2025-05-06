import streamlit as st

# Set up the page
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Force larger dropdown title text */
    summary {
        font-size: 32px !important;
        font-weight: bold !important;
        color: white !important;
    }

    /* Optional: style inside content */
    .stMarkdown {
        font-size: 18px;
        color: white;
    }

    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 12px 0px;
        padding: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and prompt
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# Define dropdown sections
adhd_effects = {
    "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
    "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
    "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
}

# Create styled dropdowns
for label, description in adhd_effects.items():
    with st.expander(label):
        st.write(description)
