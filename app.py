import streamlit as st

# Page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# CSS for full customization
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Style the whole dropdown container */
    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 15px 0;
        padding: 5px;
    }

    /* Force larger header font and thicker white border */
    [data-testid="stExpander"] > details > summary {
        font-size: 30px !important;
        font-weight: bold !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 6px;
        padding: 12px;
        list-style: none;
    }

    /* Optional: remove default triangle bullet */
    [data-testid="stExpander"] summary::-webkit-details-marker {
        display: none;
    }

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

# Create proper dropdowns with correct title placement
for label, description in adhd_effects.items():
    with st.expander(label):
        st.markdown(f"<div style='font-size: 18px; color: white;'>{description}</div>", unsafe_allow_html=True)
