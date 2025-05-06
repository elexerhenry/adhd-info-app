import streamlit as st

# Page setup
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Title and description
st.title("Understanding the Effects of ADHD")
st.markdown("Click on a section to learn more.")

# HTML and CSS for styled dropdowns
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    .dropdown {
        background-color: #ff9966;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        cursor: pointer;
        font-size: 26px;
        font-weight: bold;
        color: white;
    }

    .dropdown:hover {
        background-color: #e56742;
    }

    .content {
        display: none;
        padding: 10px 15px;
        font-size: 18px;
        color: white;
        background-color: #e67c52;
        border-radius: 0 0 8px 8px;
        margin-bottom: 10px;
    }
    </style>

    <script>
    function toggleContent(id) {
        var content = document.getElementById(id);
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    }
    </script>

    <div class="dropdown" onclick="toggleContent('inattention')">🧠 Inattention</div>
    <div id="inattention" class="content">
        People with ADHD may have trouble staying focused, get easily distracted, or avoid tasks that require sustained attention.
    </div>

    <div class="dropdown" onclick="toggleContent('impulsivity')">⚡ Impulsivity</div>
    <div id="impulsivity" class="content">
        Impulsivity includes interrupting others, making quick decisions without thinking, or difficulty waiting your turn.
    </div>

    <div class="dropdown" onclick="toggleContent('hyperactivity')">🏃 Hyperactivity</div>
    <div id="hyperactivity" class="content">
        Hyperactivity might look like fidgeting, restlessness, or feeling the need to constantly move or talk.
    </div>
""", unsafe_allow_html=True)
