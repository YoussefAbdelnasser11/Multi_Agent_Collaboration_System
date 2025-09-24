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
    .warning-box {
        background: rgba(255, 165, 0, 0.1);
        border: 1px solid orange;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
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
    
    # Timeout settings
    st.markdown("### ⏱️ Timeout Settings")
    analysis_timeout = st.number_input("Analysis Timeout (seconds)", min_value=60, max_value=600, value=300, step=30)
    generation_timeout = st.number_input("Generation Timeout (seconds)", min_value=30, max_value=300, value=120, step=10)
    
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
# TAB 1: Multi-Agent Analysis (مع إصلاح الـ Timeout)
# =======================
with tab1:
    st.markdown("### 🚀 Multi-Agent Topic Analysis")
    st.markdown("Analyze topics using our collaborative AI agent system")
    
    # Warning about processing time
    st.markdown("""
    <div class='warning-box'>
    ⚠️ <strong>Note:</strong> Multi-agent analysis typically takes 2-3 minutes due to comprehensive processing by multiple AI agents.
    Please be patient and avoid refreshing the page during analysis.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_area(
            "📝 Enter topic for analysis:",
            placeholder="e.g., Artificial intelligence and its impact on the job market...",
            height=100,
            key="analysis_topic"
        )
    
    with col2:
        st.markdown("###")
        st.markdown("###")
        analyze_btn = st.button("🔍 Start Analysis", type="primary", use_container_width=True, key="analyze_btn")
    
    # Analysis parameters
    with st.expander("⚙️ Analysis Settings"):
        col1, col2 = st.columns(2)
        with col1:
            show_details = st.checkbox("Show detailed agent outputs", value=True)
            auto_expand = st.checkbox("Auto-expand results", value=True)
        with col2:
            enable_streaming = st.checkbox("Enable progress simulation", value=True)
    
    if analyze_btn and topic.strip():
        if not topic.strip():
            st.warning("⚠️ Please enter a topic to analyze")
        else:
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            result_container = st.empty()
            
            try:
                # Simulate progress steps (optional)
                if enable_streaming:
                    steps = [
                        "Initializing AI agents...", 
                        "Researching topic information...", 
                        "Processing research data...",
                        "Summarizing key findings...", 
                        "Analyzing patterns and relationships...", 
                        "Generating recommendations...",
                        "Finalizing analysis..."
                    ]
                    
                    for i, step in enumerate(steps):
                        status_text.text(f"🔄 {step} ({i+1}/{len(steps)})")
                        progress_bar.progress((i + 1) / len(steps))
                        time.sleep(2)  # زيادة الوقت بين الخطوات
                
                # Actual API call with increased timeout
                status_text.text("🔗 Connecting to AI analysis system...")
                
                response = requests.post(
                    f"{API_URL}/analyze",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={"topic": topic.strip()},
                    timeout=analysis_timeout  # استخدام الـ timeout من الإعدادات
                )
                
                if response.status_code == 200:
                    data = response.json()
                    progress_bar.progress(100)
                    status_text.text("✅ Analysis complete!")
                    
                    # Display results
                    with result_container.container():
                        st.balloons()
                        
                        # Main results card
                        st.markdown("### 📊 Analysis Results")
                        
                        # Topic header
                        st.markdown(f"**Topic:** `{data.get('topic', 'N/A')}`")
                        st.markdown("---")
                        
                        # Results in expandable sections
                        if show_details:
                            with st.expander("🔬 Research Data", expanded=auto_expand):
                                research_content = data.get('research_data', 'No research data available')
                                st.markdown(f"<div class='result-box'>{research_content}</div>", unsafe_allow_html=True)
                            
                            with st.expander("📋 Summary", expanded=auto_expand):
                                summary_content = data.get('summary', 'No summary available')
                                st.markdown(f"<div class='result-box'>{summary_content}</div>", unsafe_allow_html=True)
                            
                            with st.expander("🔍 Analysis", expanded=auto_expand):
                                analysis_content = data.get('analysis', 'No analysis available')
                                st.markdown(f"<div class='result-box'>{analysis_content}</div>", unsafe_allow_html=True)
                        
                        # Recommendations (always shown)
                        st.markdown("### 🎯 Final Recommendations")
                        recommendations_content = data.get('recommendations', 'No recommendations available')
                        st.markdown(f"<div class='result-box' style='border-left-color: #FF6B6B;'>{recommendations_content}</div>", unsafe_allow_html=True)
                        
                        # Success metrics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.success("✅ Research Completed")
                        with col2:
                            st.success("✅ Analysis Finished")
                        with col3:
                            st.success("✅ Recommendations Ready")
                        
                        # Raw JSON view
                        with st.expander("📄 Raw JSON Data"):
                            st.json(data)
                        
                        # Download option
                        json_str = json.dumps(data, indent=2, ensure_ascii=False)
                        st.download_button(
                            label="📥 Download Full Analysis (JSON)",
                            data=json_str,
                            file_name=f"ai_analysis_{topic[:20].replace(' ', '_')}.json",
                            mime="application/json",
                            use_container_width=True
                        )
                        
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.Timeout:
                st.error(f"⏰ Request timeout ({analysis_timeout}s) - The analysis is taking longer than expected")
                st.info("💡 Try reducing the topic complexity or increasing the timeout in settings")
            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error - Please check the API URL and internet connection")
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {str(e)}")
            
            finally:
                # Clean up progress indicators after delay
                time.sleep(3)
                progress_bar.empty()
                status_text.empty()

# =======================
# TAB 2: Direct Text Generation (مع إصلاح الـ Timeout)
# =======================
with tab2:
    st.markdown("### 📝 Direct Text Generation")
    st.markdown("Generate text directly using the AI model (Faster - usually under 1 minute)")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        prompt = st.text_area(
            "💬 Enter your prompt:",
            placeholder="e.g., Explain quantum computing in simple terms...",
            height=100,
            key="generation_prompt"
        )
    
    with col2:
        st.markdown("###")
        st.markdown("###")
        generate_btn = st.button("✨ Generate Text", type="secondary", use_container_width=True, key="generate_btn")
    
    # Generation settings
    with st.expander("⚙️ Generation Settings"):
        col1, col2 = st.columns(2)
        with col1:
            max_length = st.slider("Max length", 100, 2000, 500, 100)
        with col2:
            quick_generation = st.checkbox("Quick generation mode", value=True)
    
    if generate_btn and prompt.strip():
        try:
            with st.spinner(f"Generating text (timeout: {generation_timeout}s)..."):
                response = requests.post(
                    f"{API_URL}/generate",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "prompt": prompt.strip(),
                        "max_length": max_length
                    },
                    timeout=generation_timeout  # استخدام الـ timeout من الإعدادات
                )
            
            if response.status_code == 200:
                data = response.json()
                generated_text = data.get('generated_text', '')
                
                st.success("✅ Text generated successfully!")
                
                # Display generated text
                st.markdown("### 📄 Generated Text")
                st.markdown(f"<div class='result-box'>{generated_text}</div>", unsafe_allow_html=True)
                
                # Text stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Characters", len(generated_text))
                with col2:
                    st.metric("Words", len(generated_text.split()))
                with col3:
                    st.metric("Lines", generated_text.count('\n') + 1)
                
                # Download option
                st.download_button(
                    label="📥 Download Text",
                    data=generated_text,
                    file_name=f"generated_text_{prompt[:20].replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            else:
                st.error(f"❌ Generation error: {response.status_code} - {response.text}")
                
        except requests.exceptions.Timeout:
            st.error(f"⏰ Generation timeout ({generation_timeout}s) - Try reducing text length")
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
        
        # Health check with timeout
        try:
            health_response = requests.get(f"{API_URL}/health", timeout=10)
            if health_response.status_code == 200:
                st.success("✅ System is online and healthy")
                st.metric("Status", "Operational")
                st.metric("Current Timeout", f"{analysis_timeout}s")
            else:
                st.warning("⚠️ System response unexpected")
        except requests.exceptions.Timeout:
            st.error("❌ Health check timeout")
        except:
            st.error("❌ Cannot connect to system")
        
        st.markdown("#### ⚠️ Important Notes")
        st.info("""
        - **Analysis Time**: 2-3 minutes for complex topics
        - **Generation Time**: 30-60 seconds for direct generation  
        - **Timeout**: Adjust in sidebar if experiencing issues
        - **Stability**: ngrok URLs may change after restart
        """)

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
