# Chatbot Framework

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Extensible chatbot sample applications built with Chainlit, supporting multiple conversation modes including PDF document interaction, persistent conversation history, and customizable user interfaces.

## 🚀 Features

- **Multiple Chatbot Implementations**:
  - `chatbot_simple.py`: Basic implementation with minimal dependencies
  - `chatbot_streaming.py`: Real-time token streaming responses
  - `chatbot_history.py`: Persistent conversation history
  - `chatbot_widgets.py`: Customizable UI components
  - `chatbot_pdf.py`: Document interaction with PDF parsing capabilities

- **AI Model Integration**: Seamless integration with Ollama models (llama2, llama3)
- **Document Processing**: Extract and query content from PDF documents
- **Vector Database**: Store and retrieve semantic embeddings for improved responses
- **Streaming Responses**: Real-time token generation for a more interactive experience
- **Customizable Settings**: Adjust model parameters like temperature through an intuitive UI

## 📋 Prerequisites

- Python 3.6 or higher
- [Ollama](https://ollama.ai/) for local model inference
- Additional dependencies listed in `requirements.txt`

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/AmaMidzu/chatbot.git
cd chatbot
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

Run any of the chatbot implementations using Chainlit:

```bash
# Simple chatbot
chainlit run chatbot_simple.py

# Chatbot with streaming responses
chainlit run chatbot_streaming.py

# Chatbot with conversation history
chainlit run chatbot_history.py

# Chatbot with customizable widgets
chainlit run chatbot_widgets.py

# PDF document interaction chatbot
chainlit run chatbot_pdf.py
```

## 📖 Usage Examples

### Basic Conversation
Interact with the chatbot using simple text queries:

```
User: What is machine learning?
Chatbot: Machine learning is a branch of artificial intelligence that focuses on...
```

### PDF Document Interaction
Upload a PDF document and ask questions about its content:

```
User: [Uploads research paper]
User: What are the key findings of this paper?
Chatbot: According to the paper, the key findings are...
```

### Customizing Model Parameters
Adjust model settings through the UI components:
- Select between different LLM models (llama2, llama3)
- Adjust temperature for more creative or deterministic responses
- Configure other model parameters as needed

## 🧩 Architecture

The chatbot framework is built on these key components:

- **Chainlit**: Web interface for chatbot interaction
- **LangChain**: Orchestration of LLM workflows
- **Ollama**: Local model inference
- **Vector Databases**: Document embeddings and semantic search


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
