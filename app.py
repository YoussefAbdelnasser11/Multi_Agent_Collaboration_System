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
col1, col2, col3 = st.columns([2, 6, 2])

with col1:
    st.markdown(
        "<p style='font-size:16px; color:#ffffff;'>Made by Eng/Youssef Abdelnasser</p>",
        unsafe_allow_html=True
    )

with col2:
    st.title("🤖 Multi Agent Collaboration System")

with col3:
    try:
        logo = Image.open("Tips Hindawi.jpg")
        st.image(logo, width=90)
        st.markdown(
            "<p style='text-align:center; color:#FF0000; font-weight:bold;'>Tips Hindawi</p>",
            unsafe_allow_html=True
        )
    except:
        st.markdown(
            "<p style='text-align:center; color:#FF0000; font-weight:bold;'>Tips Hindawi</p>",
            unsafe_allow_html=True
        )

st.markdown("<hr>", unsafe_allow_html=True)

# =======================
# API Config
# =======================
API_URL = "https://f6a6d0a4f2c1.ngrok-free.app"
API_KEY = "secret123"  # change if needed

# =======================
# User Interface - Centered Content
# =======================
st.write("Analyze topics using a collaborative multi-agent system.")

# Center the input and button
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    topic = st.text_input("📝 Enter a topic to analyze:", key="topic_input")
    
    if st.button("Analyze", key="analyze_btn"):
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
                    
                    # Display results in a nice format
                    st.subheader("📌 Analysis Results")
                    
                    # Create tabs for different views
                    tab1, tab2 = st.tabs(["Formatted View", "Raw JSON"])
                    
                    with tab1:
                        st.markdown(f"**Topic:** {data.get('topic', 'N/A')}")
                        st.markdown("---")
                        st.markdown(f"**Result:**\n{data.get('result', 'No result available')}")
                    
                    with tab2:
                        st.json(data)
                        
                else:
                    st.error(f"❌ Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"⚠️ Connection failed: {e}")

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
