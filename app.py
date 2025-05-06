import streamlit as st

# Set page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* Make expander titles larger and more readable */
    .streamlit-expanderHeader {
        font-size: 1.6rem;
        font-weight: bold;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

# ADHD effects
adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

# Expanders
for label, description in adhd_effects.items():
    with st.expander(f"🧠 {label}"):
        st.write(description)
