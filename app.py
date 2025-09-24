import streamlit as st
import requests
import json
import time
from PIL import Image

# =======================
# Page Config
# =======================
st.set_page_config(
    page_title="AI Multi-Agent System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================
# Custom CSS Styling
# =======================
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .agent-card {
        background: rgba(30, 30, 30, 0.8);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #4ECDC4;
    }
    .result-box {
        background: rgba(40, 40, 40, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid #444;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(45deg, #4ECDC4, #45B7D1);
    }
    .tab-content {
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# =======================
# Header Layout
# =======================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="main-header">🤖 AI Multi-Agent Collaboration System</div>', unsafe_allow_html=True)

# Logo and creator info
with st.sidebar:
    st.markdown("### 🛠️ Configuration")
    
    # API Configuration
    API_URL = st.text_input("🌐 API URL", value="https://1d0f745acd0e.ngrok-free.app")
    API_KEY = st.text_input("🔑 API Key", value="secret123", type="password")
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Created by")
    st.markdown("**Eng/Youssef Abdelnasser**")
    
    try:
        logo = Image.open("Tips Hindawi.jpg")
        st.image(logo, width=100, caption="Tips Hindawi")
    except:
        st.info("📷 Logo image not found")

# =======================
# Main Tabs
# =======================
tab1, tab2, tab3 = st.tabs(["🚀 Multi-Agent Analysis", "📝 Direct Text Generation", "ℹ️ System Info"])

# =======================
# TAB 1: Multi-Agent Analysis
# =======================
with tab1:
    st.markdown("### 🚀 Multi-Agent Topic Analysis")
    st.markdown("Analyze topics using our collaborative AI agent system")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_area(
            "📝 Enter topic for analysis:",
            placeholder="e.g., Artificial intelligence and its impact on the job market...",
            height=100
        )
    
    with col2:
        st.markdown("###")
        st.markdown("###")
        analyze_btn = st.button("🔍 Start Analysis", type="primary", use_container_width=True)
    
    # Analysis parameters
    with st.expander("⚙️ Analysis Settings"):
        col1, col2 = st.columns(2)
        with col1:
            show_details = st.checkbox("Show detailed agent outputs", value=True)
        with col2:
            auto_expand = st.checkbox("Auto-expand results", value=True)
    
    if analyze_btn and topic.strip():
        if not topic.strip():
            st.warning("⚠️ Please enter a topic to analyze")
        else:
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Simulate progress steps
                steps = ["Initializing agents...", "Researching topic...", 
                        "Summarizing findings...", "Analyzing data...", 
                        "Generating recommendations...", "Finalizing results..."]
                
                results = {}
                
                for i, step in enumerate(steps):
                    status_text.text(f"🔄 {step}")
                    progress_bar.progress((i + 1) / len(steps))
                    time.sleep(0.5)  # Simulate processing time
                
                # Actual API call
                status_text.text("🔗 Connecting to AI system...")
                response = requests.post(
                    f"{API_URL}/analyze",
                    headers={"Authorization": f"Bearer {API_KEY}"},
                    json={"topic": topic.strip()},
                    timeout=120
                )
                
                if response.status_code == 200:
                    data = response.json()
                    progress_bar.progress(100)
                    status_text.text("✅ Analysis complete!")
                    
                    # Display results in an organized way
                    st.balloons()
                    
                    # Main results card
                    with st.container():
                        st.markdown("### 📊 Analysis Results")
                        
                        # Topic header
                        st.markdown(f"**Topic:** {data.get('topic', 'N/A')}")
                        
                        # Results in expandable sections
                        if show_details:
                            with st.expander("🔬 Research Data", expanded=auto_expand):
                                st.markdown(f"<div class='result-box'>{data.get('research_data', 'No data')}</div>", unsafe_allow_html=True)
                            
                            with st.expander("📋 Summary", expanded=auto_expand):
                                st.markdown(f"<div class='result-box'>{data.get('summary', 'No summary')}</div>", unsafe_allow_html=True)
                            
                            with st.expander("🔍 Analysis", expanded=auto_expand):
                                st.markdown(f"<div class='result-box'>{data.get('analysis', 'No analysis')}</div>", unsafe_allow_html=True)
                        
                        # Recommendations (always shown)
                        st.markdown("### 🎯 Final Recommendations")
                        st.markdown(f"<div class='result-box' style='border-left-color: #FF6B6B;'>{data.get('recommendations', 'No recommendations')}</div>", unsafe_allow_html=True)
                        
                        # Raw JSON view
                        with st.expander("📄 Raw JSON Data"):
                            st.json(data)
                        
                        # Download option
                        json_str = json.dumps(data, indent=2, ensure_ascii=False)
                        st.download_button(
                            label="📥 Download Results as JSON",
                            data=json_str,
                            file_name=f"analysis_{topic[:30]}.json",
                            mime="application/json"
                        )
                        
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.Timeout:
                st.error("⏰ Request timeout - The analysis is taking too long")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error - Please check the API URL")
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {str(e)}")
            
            finally:
                # Clean up progress indicators
                time.sleep(2)
                progress_bar.empty()
                status_text.empty()

# =======================
# TAB 2: Direct Text Generation
# =======================
with tab2:
    st.markdown("### 📝 Direct Text Generation")
    st.markdown("Generate text directly using the AI model")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        prompt = st.text_area(
            "💬 Enter your prompt:",
            placeholder="e.g., Explain quantum computing in simple terms...",
            height=100
        )
    
    with col2:
        st.markdown("###")
        st.markdown("###")
        generate_btn = st.button("✨ Generate Text", type="secondary", use_container_width=True)
    
    # Generation settings
    with st.expander("⚙️ Generation Settings"):
        col1, col2 = st.columns(2)
        with col1:
            max_length = st.slider("Max length", 100, 2000, 500, 100)
            temperature = st.slider("Temperature", 0.1, 1.0, 0.7, 0.1)
        with col2:
            top_k = st.slider("Top-K", 1, 100, 50)
            top_p = st.slider("Top-P", 0.1, 1.0, 0.95, 0.05)
    
    if generate_btn and prompt.strip():
        try:
            with st.spinner("Generating text..."):
                response = requests.post(
                    f"{API_URL}/generate",
                    headers={"Authorization": f"Bearer {API_KEY}"},
                    json={
                        "prompt": prompt.strip(),
                        "max_length": max_length
                    },
                    timeout=60
                )
            
            if response.status_code == 200:
                data = response.json()
                
                st.success("✅ Text generated successfully!")
                
                # Display generated text
                st.markdown("### 📄 Generated Text")
                st.markdown(f"<div class='result-box'>{data.get('generated_text', 'No text generated')}</div>", unsafe_allow_html=True)
                
                # Text stats
                col1, col2, col3 = st.columns(3)
                text_content = data.get('generated_text', '')
                with col1:
                    st.metric("Characters", len(text_content))
                with col2:
                    st.metric("Words", len(text_content.split()))
                with col3:
                    st.metric("Lines", text_content.count('\n') + 1)
                
                # Download option
                st.download_button(
                    label="📥 Download Text",
                    data=text_content,
                    file_name=f"generated_text_{prompt[:20]}.txt",
                    mime="text/plain"
                )
                
            else:
                st.error(f"❌ Generation error: {response.status_code} - {response.text}")
                
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

# =======================
# TAB 3: System Info
# =======================
with tab3:
    st.markdown("### ℹ️ System Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏗️ System Architecture")
        st.markdown("""
        Our multi-agent system consists of four specialized AI agents:
        
        - **🔍 Research Agent**: Gathers comprehensive information
        - **📊 Summarization Agent**: Condenses information effectively  
        - **🔎 Reasoning Agent**: Analyzes patterns and relationships
        - **🎯 Decision Agent**: Provides actionable recommendations
        """)
        
        st.markdown("#### 🌐 API Endpoints")
        st.markdown(f"""
        - **Multi-Agent Analysis**: `POST {API_URL}/analyze`
        - **Direct Generation**: `POST {API_URL}/generate`
        - **Health Check**: `GET {API_URL}/health`
        """)
    
    with col2:
        st.markdown("#### 📊 System Status")
        
        # Health check
        try:
            health_response = requests.get(f"{API_URL}/health", timeout=10)
            if health_response.status_code == 200:
                st.success("✅ System is online and healthy")
                st.metric("Status", "Operational")
            else:
                st.warning("⚠️ System response unexpected")
        except:
            st.error("❌ Cannot connect to system")
        
        st.markdown("#### 🔄 Recent Activity")
        st.info("No recent activity to display")
        
        st.markdown("#### 📈 Performance")
        st.metric("Response Time", "~2-3 minutes")
        st.metric("Max Topic Length", "Unlimited")

# =======================
# Footer
# =======================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "AI Multi-Agent System • Built with Streamlit • Powered by Mistral AI"
    "</div>", 
    unsafe_allow_html=True
)
