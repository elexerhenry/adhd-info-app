import streamlit as st

# Page configuration
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Style the entire expander block */
    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 15px 0;
        padding: 5px;
    }

    /* Force font size and border on expander title */
    section[data-testid="stExpander"] > details > summary {
        font-size: 30px !important;
        font-weight: bold !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 6px;
        padding: 10px;
    }

    /* Style inside content */
    .stMarkdown {
        font-size: 18px;
        color: white;
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

# Create dropdowns
for label, description in adhd_effects.items():
    with st.expander(label):
        st.markdown(description)
