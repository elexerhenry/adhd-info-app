import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

st.title("Understanding the Effects of ADHD")

st.markdown("Click on an icon to learn more about each effect:")

# Example data - you can expand this
adhd_effects = {
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",
}

# Display icons and descriptions
for label, description in adhd_effects.items():
    with st.expander(f"🧠 {label}"):
        st.write(description)

{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
st.set_page_config(page_title="ADHD Info App", layout="centered")\
\
st.title("Understanding the Effects of ADHD")\
\
st.markdown("Click on an icon to learn more about each effect:")\
\
# Example data - you can expand this\
adhd_effects = \{\
    "Inattention": "People with ADHD may have trouble staying focused or following through on tasks.",\
    "Impulsivity": "This includes acting without thinking, interrupting others, or making hasty decisions.",\
    "Hyperactivity": "Fidgeting, restlessness, or an inability to stay still are common symptoms.",\
\}\
\
# Display icons and descriptions\
for label, description in adhd_effects.items():\
    with st.expander(f"\uc0\u55358 \u56800  \{label\}"):\
        st.write(description)\
}
