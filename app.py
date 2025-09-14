# =======================
# Dark Mode Styling
# =======================
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    hr {
        border: 1px solid #444;
    }
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .logo-container {
        position: absolute;
        top: 10px;
        left: 10px; /* Changed from right to left */
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Changed to flex-start for left alignment */
        margin-top: 0;
        padding-top: 0;
    }
    .logo-text {
        color: #FF0000;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 2px;
        padding: 0;
        line-height: 1;
    }
    .main-content {
        margin-top: 50px; /* Adjust to avoid overlap with logo */
    }
    .st-image {
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# =======================
# Header Layout
# =======================
st.markdown("<div class='header-container'>", unsafe_allow_html=True)

# Left side - Name
st.markdown(
    "<p style='font-size:16px; color:#ffffff; margin: 0;'>Made by Eng/Youssef Abdelnasser</p>",
    unsafe_allow_html=True
)

# Center - Title
st.markdown(
    "<h1 style='text-align: center; margin: 0; font-size: 32px;'>🤖 Multi Agent Collaboration System</h1>",
    unsafe_allow_html=True
)

# Right side - Logo + Text (moved to top left)
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)

# الكلمة
st.markdown("<p class='logo-text'>Tips Hindawi</p>", unsafe_allow_html=True)

# اللوجو
try:
    logo = Image.open("Tips Hindawi.jpg")
    st.image(logo, width=90)
except:
    pass

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)  # Close header-container
st.markdown("<hr>", unsafe_allow_html=True)
