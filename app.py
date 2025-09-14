import streamlit as st
import requests
from PIL import Image

# =======================
# Page Config
# =======================
st.set_page_config(
    page_title="Multi Agent Collaboration System",
    page_icon="🤖",
    layout="wide"
)

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
# =======================
# API Config
# =======================
API_URL = "https://f6a6d0a4f2c1.ngrok-free.app"
API_KEY = "secret123"

# =======================
# User Interface - Centered Content
# =======================
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

st.markdown(
    "<p style='font-size: 18px; text-align: center;'>Analyze topics using a collaborative multi-agent system.</p>",
    unsafe_allow_html=True
)

col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    topic = st.text_input("📝 Enter a topic to analyze:", key="topic_input")
    
    if st.button("Analyze", key="analyze_btn", type="primary"):
        if topic.strip() == "":
            st.warning("⚠️ Please enter a topic to analyze")
        else:
            try:
                with st.spinner("Analyzing topic..."):
                    response = requests.post(
                        f"{API_URL}/analyze",
                        headers={"Authorization": f"Bearer {API_KEY}"},
                        json={"topic": topic}
                    )
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Analysis Complete!")
                    
                    st.markdown(
                        "<h2 style='font-size: 24px;'>📌 Analysis Results</h2>",
                        unsafe_allow_html=True
                    )
                    
                    tab1, tab2 = st.tabs(["Formatted View", "Raw JSON"])
                    
                    with tab1:
                        st.markdown(f"<p style='font-size: 18px;'><strong>Topic:</strong> {data.get('topic', 'N/A')}</p>", unsafe_allow_html=True)
                        st.markdown("---")
                        st.markdown(f"<p style='font-size: 18px;'><strong>Result:</strong><br>{data.get('result', 'No result available')}</p>", unsafe_allow_html=True)
                    
                    with tab2:
                        st.json(data)
                        
                else:
                    st.error(f"❌ Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"⚠️ Connection failed: {e}")

st.markdown("</div>", unsafe_allow_html=True)

# Spacing
st.markdown("<br><br>", unsafe_allow_html=True)
