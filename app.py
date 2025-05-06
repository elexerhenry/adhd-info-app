import streamlit as st

# Page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Custom CSS to override expander styles
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Force font size change on expander header */
    [data-testid="stExpander"] summary {
        font-size: 28px !important;
        font-weight: bold !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# Define sections
adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

# Render each expander with HTML span for better control
for label, description in adhd_effects.items():
    title_html = f"<span>🧠 {label}</span>"
    with st.expander(label=title_html):
        st.write(description)
