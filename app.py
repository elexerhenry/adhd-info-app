import streamlit as st

# Set page title and layout
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS to change background color
st.markdown("""
    <style>
    body {
        background-color: #FF7C52;
    }
    </style>
""", unsafe_allow_html=True)

# App title and intro
st.title("Understanding the Effects of ADHD")

st.markdown("Click on an icon to learn more about each effect:")

# ADHD effects and descriptions
adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

# Display each effect in an expandable section
for label, description in adhd_effects.items():
    with st.expander(f"🧠 {label}"):
        st.write(description)
