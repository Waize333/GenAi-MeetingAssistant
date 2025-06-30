# 🎤 AI-Powered Meeting Assistant

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Gradio](https://img.shields.io/badge/gradio-4.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)

Transform your audio recordings into actionable insights with AI-powered transcription and analysis. This tool combines OpenAI's Whisper for speech recognition with IBM watsonx Granite AI for intelligent content analysis.

## 🌟 Features

### 📝 **Smart Transcription**

- High-quality speech-to-text using OpenAI Whisper
- Supports multiple audio formats (MP3, WAV, M4A, FLAC)
- Optimized for English language processing
- Real-time microphone recording capability

### 🎯 **Intelligent Analysis**

- **Summary Mode**: Get concise overviews of your meetings
- **Key Points**: Extract main discussion points automatically
- **Detailed Analysis**: Comprehensive insights and action items
- Powered by IBM watsonx Granite AI

### 🚀 **Easy to Use**

- Simple drag-and-drop interface
- No technical knowledge required
- Process files up to 30 minutes
- Instant results with professional formatting

## 🆓 Try It Now - FREE!

**🔗 [Launch on Hugging Face Spaces](https://huggingface.co/spaces/waize333/GenAi-MeetingAssistant)**

*No installation required • No signup needed • Completely free*

## 💼 Perfect For

- **Business Meetings**: Capture decisions and action items
- **Interviews**: Transcribe and analyze candidate responses
- **Lectures**: Extract key learning points from recordings
- **Podcasts**: Generate summaries and highlights
- **Research**: Analyze qualitative data from audio
- **Legal**: Document important conversations (with consent)

## 🛠️ How It Works

1. **📤 Upload**: Drop your audio file or record directly
2. **⚙️ Choose**: Select your preferred analysis type
3. **🚀 Process**: Click the button and wait for AI magic
4. **📋 Get Results**: Receive formatted transcript + insights

```
Audio File → Whisper (Transcription) → IBM Granite (Analysis) → Formatted Results
```

## 📊 Example Output

```markdown
## 📝 Transcript
We discussed the quarterly sales figures, marketing strategies for Q2, 
and the budget allocation for the new product launch...

---

## 🎯 Analysis (Key Points)
• Q1 sales exceeded targets by 15%
• Marketing budget increased by 20% for Q2
• New product launch scheduled for June
• Team expansion planned for customer support
• Follow-up meeting scheduled for next Friday

---
*Powered by OpenAI Whisper + IBM Granite*
```

## 🏃‍♂️ Quick Start (Local Installation)

### Prerequisites

- Python 3.8+
- IBM Cloud account (for watsonx access)

### Installation

```bash
# Clone the repository
git clone https://github.com/Waize333/GenAi-MeetingAssistant
cd GenAi-MeetingAssistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your IBM credentials

# Run the application
python speech_analyzer.py
```

### Environment Setup

Create a .env file:

```env
IBM_CLOUD_API_KEY=your_ibm_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
```

## 🌐 Deployment

### Hugging Face Spaces (Recommended)

1. Fork this repository
2. Create a new [Hugging Face Space](https://huggingface.co/spaces)
3. Connect your GitHub repo
4. Add your IBM credentials as repository secrets
5. Deploy automatically!

### Local Deployment

```bash
python speech_analyzer.py
```

Access at `http://localhost:7860`

## 🔧 Technical Stack

- **Frontend**: Gradio (Python web framework)
- **Speech Recognition**: OpenAI Whisper
- **AI Analysis**: IBM watsonx Granite
- **Language Processing**: LangChain
- **Audio Processing**: Transformers (Hugging Face)

## 📋 Requirements

```txt
torch>=2.0.0
transformers>=4.20.0
gradio>=4.0.0
langchain-core>=0.1.0
langchain-ibm>=0.1.0
ibm-watson-machine-learning>=1.0.0
python-dotenv>=1.0.0
```

## 🔒 Privacy & Security

- ✅ Audio processed securely
- ✅ No permanent storage of files
- ✅ IBM enterprise-grade security
- ✅ GDPR compliant processing
- ❗ Always get consent before recording

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for Whisper speech recognition
- [IBM](https://www.ibm.com/) for watsonx Granite AI models
- [Hugging Face](https://huggingface.co/) for hosting and transformers
- [Gradio](https://gradio.app/) for the amazing UI framework

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/ai-meeting-assistant/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/ai-meeting-assistant/discussions)
- 📧 **Email**: your.email@example.com

## 🚀 What's Next?

- [ ]  Multi-language support
- [ ]  Speaker identification
- [ ]  Meeting sentiment analysis
- [ ]  Calendar integration
- [ ]  Export to various formats (PDF, Word, etc.)
- [ ]  Real-time live transcription

*

</div>
