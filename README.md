# 🤖 Multi Agent Collaboration System

A sophisticated multi-agent AI system that collaboratively analyzes topics through a pipeline of specialized agents, providing comprehensive insights and actionable recommendations.

## 🌟 Features

- **Multi-Agent Architecture**: Four specialized AI agents working in sequence
- **Research Agent**: Conducts comprehensive research on any topic
- **Summarization Agent**: Extracts key insights and creates concise summaries
- **Reasoning Agent**: Analyzes patterns and draws logical conclusions
- **Decision Agent**: Provides actionable recommendations and strategic plans
- **RESTful API**: FastAPI backend with multiple endpoints
- **Web Interface**: Streamlit-based responsive web UI
- **Secure Access**: API key authentication for all endpoints
- **Public Access**: Ngrok tunneling for external access

## 🏗️ System Architecture
User Input → Research Agent → Summarization Agent → Reasoning Agent → Decision Agent → Final Output

text

### Agents Overview:

1. **Research Agent**: Gathers comprehensive information about the topic
2. **Summarization Agent**: Extracts and condenses key information
3. **Reasoning Agent**: Analyzes patterns and draws conclusions
4. **Decision Agent**: Provides strategic recommendations and action plans

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- HuggingFace account and token
- Ngrok account (for public access)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd multi-agent-collaboration-system
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

Get your HuggingFace token from huggingface.co

Get your Ngrok token from ngrok.com

Configure the system

python
# In your main script:
NGROK_TOKEN = "your_ngrok_token_here"
API_KEY = "your_secret_api_key_here"
Run the system

bash
# Start the backend API
python main.py

# In another terminal, start the frontend
streamlit run app.py
📡 API Endpoints
Available Endpoints:
POST /generate - Direct text generation with LLM

POST /research - Research agent only

POST /summarize - Summarization agent only

POST /analyze - Reasoning agent only

POST /decide - Decision agent only

POST /full_analysis - Complete multi-agent pipeline

GET /health - Health check endpoint

Example API Usage:
python
import requests

url = "http://your-api-url/analyze"
headers = {
    "Authorization": "Bearer your_api_key_here",
    "Content-Type": "application/json"
}
data = {"topic": "Artificial intelligence impact on job market"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
🎨 Web Interface
The Streamlit interface provides:

Dark mode styling for comfortable use

Responsive design that works on desktop and mobile

Real-time analysis with progress indicators

Multiple output formats (formatted view and raw JSON)

Professional branding with logo support

🔧 Configuration
Environment Variables:
python
NGROK_TOKEN = "your_ngrok_token"  # For public access
API_KEY = "your_secret_key"       # For API authentication
MODEL_NAME = "mistralai/Mistral-Nemo-Instruct-2407"  # AI model
Customization:
Modify agent prompts in the prompt templates

Adjust model parameters (temperature, max_length, etc.)

Customize the UI theme and branding

Add new agents or processing steps

🛡️ Security
API key authentication for all endpoints

Secure token management

Input validation and sanitization

Error handling and logging

📊 Example Output
json
{
  "topic": "AI in healthcare",
  "research_data": "Comprehensive research about AI applications...",
  "summary": "Key applications include diagnostics, drug discovery...",
  "analysis": "AI shows 30% improvement in diagnostic accuracy...",
  "recommendations": "Invest in AI diagnostic tools, train medical staff..."
}
🚦 Performance
Response Time: 10-30 seconds depending on topic complexity

Model: Mistral-Nemo-Instruct-2407 (7B parameters)

Memory: ~8GB GPU RAM recommended

Storage: ~15GB for model and dependencies

🤝 Contributing
Fork the repository

Create a feature branch

Make your changes

Add tests if applicable

Submit a pull request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Developer
Eng/Youssef Abdelnasser

Email: youssefabdelnasser13@gmail.com


🙏 Acknowledgments
Tips Hindawi for support and inspiration

HuggingFace for the transformer models

Mistral AI for the base model architecture

Streamlit for the web framework

FastAPI for the efficient backend

📞 Support
For support and questions:

Create an issue on GitHub

Contact the developer directly

Check the documentation
