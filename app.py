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
    </style>
""", unsafe_allow_html=True)

# =======================
# Header + Logo
# =======================
col1, col2 = st.columns([8, 2])

with col2:
    logo = Image.open("Screenshot 2025-09-12 011923.png")  # Make sure logo file is in the same folder
    st.image(logo, width=90)

    st.markdown(
        "<p style='text-align:center; color:#FF0000; font-weight:bold;'>Tips Hindawi</p>",
        unsafe_allow_html=True
    )

with col1:
    st.markdown(
        "<p style='text-align:right; font-size:16px; color:#ffffff;'>Made by Eng/Youssef Abdelnasser</p>",
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# =======================
# API Config
# =======================
API_URL = "https://f6a6d0a4f2c1.ngrok-free.app"
API_KEY = "secret123"  # change if needed

# =======================
# User Interface
# =======================
st.title("🤖 Multi Agent Collaboration System")
st.write("Analyze topics using a collaborative multi-agent system.")

topic = st.text_input("📝 Enter a topic to analyze:")

if st.button("Analyze"):
    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic to analyze")
    else:
        try:
            response = requests.post(
                f"{API_URL}/analyze",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={"topic": topic}
            )
            
            if response.status_code == 200:
                data = response.json()
                st.subheader("📌 Results")
                st.json(data)
            else:
                st.error(f"❌ Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"⚠️ Connection failed: {e}")
