# 🤖 AI Multi-Agent Collaboration System

A sophisticated multi-agent AI system that leverages collaborative AI agents to analyze topics and generate intelligent insights.  
Built with **Streamlit**, **FastAPI**, and **Mistral AI**.

![AI Multi-Agent](https://img.shields.io/badge/AI-Multi--Agent-blue)
![Python](https://img.shields.io/badge/Python-3.11%252B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

---

## 🌟 Features

### 🤖 Multi-Agent Architecture
- **Research Agent**: Conducts comprehensive topic research  
- **Summarization Agent**: Condenses information effectively  
- **Reasoning Agent**: Analyzes patterns and relationships  
- **Decision Agent**: Provides actionable recommendations  

### 💻 User Interface
- Streamlit-based Web Interface (modern and intuitive)  
- Real-time progress tracking with visual indicators  
- Export results as JSON/TXT  
- Responsive design (desktop & mobile)  

---

## ⚡ API Endpoints
- `/analyze` → Full topic analysis pipeline  
- `/generate` → Direct text generation  
- `/health` → System status monitoring  

---

## 🚀 Quick Start

### Prerequisites
- Python **3.11+**  
- GPU (recommended for faster inference)  
- Hugging Face account (for model access)  

### Installation
```bash
git clone https://github.com/yourusername/ai-multi-agent-system.git
cd ai-multi-agent-system
pip install -r requirements.txt
```

### Environment Variables
```bash
export HUGGINGFACE_TOKEN="your_hf_token"
export API_KEY="your_secret_key"
```

### Running the System
Start backend API:
```bash
python backend/api_server.py
```

Launch frontend UI (new terminal):
```bash
streamlit run frontend/app.py
```

Access:
- Web Interface → http://localhost:8501  
- API Docs → http://localhost:8000/docs  

---

## 📖 Usage Examples

### Multi-Agent Analysis
1. Open the web interface  
2. Navigate to **Multi-Agent Analysis** tab  
3. Enter a topic (e.g., *Artificial intelligence in healthcare*)  
4. Click **Start Analysis**  
5. View results from all agents  

### Direct Text Generation
1. Go to **Direct Text Generation** tab  
2. Enter your prompt  
3. Adjust settings if needed  
4. Click **Generate Text**  
5. Download or copy results  

---

## 🏗️ System Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │ ←→ │   FastAPI API    │ ←→ │   AI Models     │
│ - Topic Input   │    │ - /analyze       │    │ - Mistral AI    │
│ - Results       │    │ - /generate      │    │ - Multi-Agent   │
│ - Export        │    │ - /health        │    │   Pipeline      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## 🔧 Configuration

### API Settings
```python
API_URL = "https://your-ngrok-url.ngrok-free.app"
API_KEY = "your_secret_key"
```

### Timeout Settings
```python
ANALYSIS_TIMEOUT = 300    # 5 minutes
GENERATION_TIMEOUT = 120  # 2 minutes
```

---

## 🎯 Use Cases
- **Business Intelligence** → Market trend analysis, strategic planning  
- **Academic Research** → Literature review, research summarization  
- **Professional Services** → Content creation, decision support, risk analysis  

---

## 📊 Performance Metrics
- Analysis Time: ~2-3 min  
- Generation Time: ~30-60 sec  
- Accuracy: High-quality multi-agent insights  
- Scalability: Supports concurrent requests  

---

## 🔒 Security Features
- API Key authentication  
- Request rate limiting  
- Secure ngrok tunneling  
- Input validation & sanitization  

---

## 🛠️ Technical Stack

**Backend**
- FastAPI (modern web framework)  
- Mistral AI (language model)  
- LangChain (multi-agent orchestration)  
- Pyngrok (secure tunneling)  

**Frontend**
- Streamlit (UI framework)  
- Custom CSS (professional styling)  
- Responsive design  

**Deployment**
- Ngrok (public URL tunneling)  
- GPU Acceleration (fast inference)  
- Async Processing (non-blocking ops)  

---

## 📁 Project Structure
```
ai-multi-agent-system/
├── backend/
│   ├── api_server.py          # FastAPI server
│   ├── agents/                # AI agent modules
│   └── models/                # Model handling
├── frontend/
│   ├── app.py                 # Streamlit app
│   └── assets/                # CSS & images
├── notebooks/
│   └── multi-agent-system.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Deployment Options

### Local
```bash
uvicorn backend.api_server:app --host 0.0.0.0 --port 8000
streamlit run frontend/app.py
```

### Cloud
```bash
# Hugging Face Spaces
git push huggingface main

# Streamlit Cloud
streamlit deploy frontend/app.py
```

---

## 🤝 Contributing
Contributions are welcome! Please check the **Contributing Guidelines**.  

### Development Setup
```bash
git clone https://github.com/yourusername/ai-multi-agent-system.git
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

---

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments
- **Mistral AI** – Language model  
- **Streamlit** – UI framework  
- **FastAPI** – Backend API  
- **LangChain** – Multi-agent orchestration  

---

## 📞 Support
- 📧 Email: eng.youssef@example.com  
- 💬 GitHub Issues  
- 🐦 Twitter: [@TipsHindawi](https://twitter.com/TipsHindawi)  

---

## 🔮 Future Enhancements
- More specialized AI agents  
- Real-time collaboration features  
- Advanced analytics dashboard  
- Mobile app development  
- External API integrations  

---

**Made with ❤️ by Eng. Youssef Abdelnasser**
