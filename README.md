# LangChain Models Application

This project is a Python application designed to integrate and experiment with various Large Language Models (LLMs) using the [LangChain](https://www.langchain.com/) framework. It provides a unified interface to interact with models from different providers, enabling easy comparison and switching between different AI backends.

## 🚀 Features

- **Multi-Provider Support**: Integrated support for:
    - **OpenAI**: Access to GPT models.
    - **Anthropic**: Access to Claude models.
    - **Google Gemini**: Access to Gemini/PaLM models.
    - **Hugging Face**: Access to a vast library of open-source models.
- **Unified Interface**: Leverages `langchain-core` to maintain a consistent API across different LLMs.
- **Environment Management**: Secure handling of API keys using `python-dotenv`.
- **ML Utilities**: Includes `numpy` and `scikit-learn` for data processing and evaluation tasks.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd LangChainModels
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv envr
   # Windows
   .\envr\Scripts\activate
   # macOS/Linux
   source envr/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r root/requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   GOOGLE_API_KEY=your_google_key
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   ```

## 📂 Project Structure

- `root/requirements.txt`: Project dependencies.
- `envr/`: Python virtual environment.

## 📦 Dependencies

The project relies on the following key libraries:
- `langchain` & `langchain-core`: The core orchestration framework.
- `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-huggingface`: Provider-specific integrations.
- `python-dotenv`: For managing secrets.
- `numpy` & `scikit-learn`: For machine learning utilities.

## 📄 License
[Specify License, e.g., MIT]
