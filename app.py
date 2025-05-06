import streamlit as st

# Set page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject CSS that directly targets the dropdown (expander) headers
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Target expander headers directly */
    details summary {
        font-size: 24px !important;
        font-weight: bold !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# Define the ADHD effect sections
adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

# Show each effect in an expander
for label, description in adhd_effects.items():
    with st.expander(f"🧠 {label}"):
        st.write(description)
