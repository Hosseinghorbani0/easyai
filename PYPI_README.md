# askai-python 🚀

**AI Made Stupid Simple.** One unified Python client for OpenAI, Claude, Gemini, Groq, and Azure.

[![PyPI version](https://img.shields.io/pypi/v/askai-python.svg)](https://pypi.org/project/askai-python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-View%20Source-blue.svg)](https://github.com/Hosseinghorbani0/ask-ai)

---

## ⚡ What is askai-python?

`askai-python` is a lightweight, zero-dependency-logic wrapper that provides a **single API** for all major AI providers. Stop learning multiple SDKs; just call `.ask()` and get your answer.

- **Unified Interface**: One syntax for OpenAI, Anthropic, Google, and more.
- **Zero-Config**: Seamlessly uses environment variables for API keys.
- **Smart Media**: Easy handling of images and audio (Provider permitting).
- **Production Grade**: Built-in robust error handling and type hints.

---

## 📦 Installation

```bash
pip install askai-python
```

---

## 🚀 Examples & Tutorials

### 1. Basic Usage (The 3-Line Magic)
```python
from ask_ai import OpenAI

ai = OpenAI() # Auto-loads OPENAI_API_KEY from env
print(ai.ask("What is the capital of France?").text)
```

### 2. Multi-Provider Mastery
Switching between top-tier models has never been easier:

```python
from ask_ai import OpenAI, Anthropic, Google

prompt = "Explain quantum computing to a 5-year-old."

# OpenAI (GPT-4o)
print(OpenAI().ask(prompt).text)

# Anthropic (Claude 3.5 Sonnet)
print(Anthropic().ask(prompt).text)

# Google (Gemini 1.5 Pro)
print(Google().ask(prompt).text)
```

### 3. Advanced Configuration (System Personas)
You can set a system prompt and temperature globally for an instance or per-request.

```python
from ask_ai import OpenAI

ai = OpenAI()

# Global config
ai.advanced(
    prompt="You are a sarcastic robot from the year 3000.",
    temperature=0.9
)

print(ai.ask("What is love?").text)

# Per-request override
print(ai.ask("What is 1+1?", temperature=0.1).text)
```

### 4. Handling Structured Exceptions
Build reliable apps by catching specific AI errors:

```python
from ask_ai import OpenAI
from ask_ai.exceptions import AskAIError, APIKeyError

try:
    ai = OpenAI(api_key="invalid-key")
    ai.ask("Hello")
except APIKeyError:
    print("Check your API keys!")
except AskAIError as e:
    print(f"An AI error occurred: {e}")
```

---

## 🔌 Supported Providers

| Provider | Class | Capabilities |
|----------|-------|-------------|
| **OpenAI** | `OpenAI` | Text, Images (DALL-E), Vision |
| **Anthropic** | `Anthropic` | Text, Vision (Claude 3.5) |
| **Google** | `Google` | Text, Images, Video, Audio |
| **Groq** | `Groq` | Ultra-fast Llama 3 & Mixtral |
| **Azure** | `Azure` | Enterprise-grade OpenAI |
| **OpenRouter**| `OpenRouter`| 100+ community models |

---

## 🔗 Important Links

- **GitHub Repository**: [Hosseinghorbani0/ask-ai](https://github.com/Hosseinghorbani0/ask-ai) (Star us! ⭐)
- **Official Website**: [hosseinghorbani0.ir](https://hosseinghorbani0.ir/)
- **Bug Tracker**: [Report an Issue](https://github.com/Hosseinghorbani0/ask-ai/issues)

---
*Built with ❤️ by [Hossein Ghorbani](https://github.com/Hosseinghorbani0).*
