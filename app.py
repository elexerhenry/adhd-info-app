import streamlit as st

# Set page config
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject more specific CSS for Streamlit expanders
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    /* More specific target for expander headers */
    div[role="button"] > div:first-child {
        font-size: 1.6rem !important;
        font-weight: bold !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("Understanding the Effects of ADHD")
st.markdown("Click on an icon to learn more about each effect:")

adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

for label, description in adhd_effects.items():
    with st.expander(f"🧠 {label}"):
        st.write(description)
