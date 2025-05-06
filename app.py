import streamlit as st

# Page setup
st.set_page_config(page_title="ADHD Info App", layout="centered")

# Inject custom HTML and CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #E56742;
    }

    .dropdown {
        background-color: #ff9966;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        cursor: pointer;
        font-size: 26px;
        font-weight: bold;
        color: white;
    }

    .dropdown:hover {
        background-color: #e67c52;
    }

    .content {
        display: none;
        padding: 10px;
        font-size: 18px;
        color: white;
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
        People with ADHD may have trouble staying focused or following through on tasks.
    </div>

    <div class="dropdown" onclick="toggleContent('impulsivity')">🧠 Impulsivity</div>
    <div id="impulsivity" class="content">
        This includes acting without thinking, interrupting others, or making hasty decisions.
    </div>

    <div class="dropdown" onclick="toggleContent('hyperactivity')">🧠 Hyperactivity</div>
    <div id="hyperactivity" class="content">
        Fidgeting, restlessness, or an inability to stay still are common symptoms.
    </div>
""", unsafe_allow_html=True)

st.title("Understanding the Effects of ADHD")
st.markdown("Click on a section to learn more.")
