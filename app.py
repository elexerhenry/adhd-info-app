import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS and JS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    [data-testid="stExpander"] {
        background-color: #ff9966;
        border-radius: 8px;
        margin: 15px 0;
        padding: 5px;
    }

    .stMarkdown {
        font-size: 18px;
        color: white;
    }

    /* Style for the tab headers */
    [data-baseweb="tab-list"] {
        justify-content: center;
        gap: 20px;
    }

    [data-baseweb="tab"] {
        border: 2px solid white;
        border-radius: 12px;
        padding: 8px 16px;
        color: white;
        font-weight: bold;
        font-size: 18px;
        background-color: transparent;
        transition: background-color 0.3s;
    }

    [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }

    [data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(255, 255, 255, 0.2);
    }
    </style>

    <script>
    window.addEventListener('load', function() {
        const expanders = window.parent.document.querySelectorAll('summary');
        expanders.forEach(e => {
            e.style.fontSize = '30px';
            e.style.fontWeight = 'bold';
            e.style.color = 'white';
            e.style.border = '2px solid white';
            e.style.borderRadius = '6px';
            e.style.padding = '12px';
            e.style.marginBottom = '4px';
        });
    });
    </script>
""", unsafe_allow_html=True)

# Tabs for content
tab1, tab2 = st.tabs(["📘 ADHD Info", "📝 Quiz"])

# --- TAB 1: ADHD Information ---
with tab1:
    st.title("Understanding the Effects of ADHD")
    st.markdown("Click on an icon to learn more about each effect:")

    adhd_effects = {
        "🧠 Inattention": "People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.",
        "⚡ Impulsivity": "Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.",
        "🏃 Hyperactivity": "Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.",
    }

    for label, description in adhd_effects.items():
        with st.expander(label):
            st.markdown(f"<div style='font-size: 18px; color: white;'>{description}</div>", unsafe_allow_html=True)

# --- TAB 2: Quiz ---
with tab2:
    st.title("Test Your Knowledge About ADHD")

    question = "Which of the following is a common symptom of ADHD?"
    options = [
        "Feeling sad most of the day",
        "Experiencing hallucinations",
        "Difficulty paying attention",
        "Sudden muscle spasms"
    ]
    answer = "Difficulty paying attention"

    user_answer = st.radio(question, options)

    if st.button("Submit Answer"):
        if user_answer == answer:
            st.success("✅ Correct! Difficulty paying attention is a common symptom.")
        else:
            st.error("❌ Incorrect. The correct answer is: 'Difficulty paying attention'.")
