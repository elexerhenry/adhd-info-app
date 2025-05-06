import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

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
