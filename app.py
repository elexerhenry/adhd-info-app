import streamlit as st

st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom CSS and JavaScript
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

    .fade-message {
        transition: opacity 1s ease;
        opacity: 1;
    }
    </style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📘 ADHD Info", "📝 Quiz", "🚫 Don't Click This"])

# --- Tab 1: ADHD Info ---
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

# --- Tab 2: Quiz ---
with tab2:
    st.title("Test Your Knowledge About ADHD")

    # Questions
    questions = [
        {
            "question": "Which of the following is a common symptom of ADHD?",
            "options": [
                "Feeling sad most of the day",
                "Experiencing hallucinations",
                "Difficulty paying attention",
                "Sudden muscle spasms"
            ],
            "answer": "Difficulty paying attention",
            "correct_msg": "✅ Correct! Difficulty paying attention is a common symptom.",
            "wrong_msg": "❌ Sorry, but that's incorrect. Try again!"
        },
        {
            "question": "How does a person have ADHD?",
            "options": [
                "Genetics",
                "Gender",
                "Age",
                "Doctor's fault"
            ],
            "answer": "Genetics",
            "correct_msg": "✅ Correct! People obtain ADHD from genetics.",
            "wrong_msg": "❌ Sorry, but that's incorrect. Try again!"
        }
    ]

    # Session state
    if "current_q" not in st.session_state:
        st.session_state.current_q = 0
    if "responses" not in st.session_state:
        st.session_state.responses = [None] * len(questions)
    if "submitted" not in st.session_state:
        st.session_state.submitted = [False] * len(questions)

    current_index = st.session_state.current_q
    q = questions[current_index]

    st.subheader(f"Question {current_index + 1}")
    user_response = st.radio(q["question"], q["options"], key=f"question_{current_index}")

    result_placeholder = st.empty()

    if st.button("Submit Answer", key=f"submit_{current_index}"):
        if user_response:
            st.session_state.responses[current_index] = user_response
            st.session_state.submitted[current_index] = True

            if user_response == q["answer"]:
                result_placeholder.markdown(
                    f"""<div class="fade-message" style="color: white; font-size: 18px; background-color: green;
                    padding: 10px; border-radius: 8px;">{q["correct_msg"]}</div>""", unsafe_allow_html=True
                )
            else:
                result_placeholder.markdown(
                    f"""<div class="fade-message" style="color: white; font-size: 18px; background-color: red;
                    padding: 10px; border-radius: 8px;">{q["wrong_msg"]}</div>""", unsafe_allow_html=True
                )

            # Only show fade effect after a short delay
            st.session_state.fade_message = True

    # Handle the fade-out effect and navigation
    if 'fade_message' in st.session_state and st.session_state.fade_message:
        st.markdown("<script>setTimeout(fadeText, 3000);</script>", unsafe_allow_html=True)
        st.session_state.fade_message = False

    # Show "Next" only if answer was submitted
    if st.session_state.submitted[current_index] and current_index < len(questions) - 1:
        # Update the session state to move to the next question
        if st.button("Next ➡", key=f"next_{current_index}"):
            st.session_state.current_q += 1
            # No need for rerun, Streamlit will re-render automatically
            st.session_state.submitted[current_index] = False  # Reset the current question submission

# --- Tab 3: Don't Click This ---
with tab3:
    st.title("🚫 Don't Click This")
    st.markdown("""
    <p style='font-size:18px; color:white;'>You really shouldn't click this, but if you do, enjoy the surprise!</p>
    """, unsafe_allow_html=True)

    # HTML anchor tag to open the image URL in a new tab
    st.markdown("""
    <a href="https://i.pinimg.com/564x/c6/3e/cd/c63ecdcc786bb3fb3078775f73826d52.jpg" target="_blank">
        <button style="background-color: #ff6666; color: white; padding: 10px; border-radius: 6px; font-size: 18px; cursor: pointer;">
            Click me (I dare you!)
        </button>
    </a>
    """, unsafe_allow_html=True)
