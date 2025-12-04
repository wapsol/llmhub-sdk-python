# LLMHub Python SDK

Official Python SDK for LLMHub - Unified access to 18+ AI providers with built-in cost tracking and provider management.

## Status

**🚧 Under Development** - This SDK is part of the [multi-language SDK initiative](https://github.com/wapsol/llmhub/issues/63).

## Features

- **Unified API**: Single interface for 18+ AI providers (Claude, OpenAI, Groq, Google Gemini, Mistral AI, and more)
- **11 Modalities**: Text generation, document processing, embeddings, audio (TTS/STT), video generation, image generation, moderation, enrichment, discovery, prompt management, and data operations
- **Cost Tracking**: Automatic cost tracking for all operations (cost_usd, tokens_used, generation_time_ms)
- **Provider Flexibility**: Use default providers or override per request
- **Type Safety**: Full type hints and validation with Pydantic
- **Python 3.9+**: Compatible with Python 3.9, 3.10, 3.11, and 3.12

## Installation

**Note: Not yet published to PyPI. Coming soon!**

```bash
# From source (development)
git clone https://github.com/wapsol/llmhub-sdk-python.git
cd llmhub-sdk-python
pip install -e .
```

Once published:
```bash
pip install llmhub
```

## Quick Start

```python
from llmhub import LLMHub

# Initialize client
client = LLMHub(
    api_key="your-api-key-here",
    base_url="https://your-llmhub-instance.com"  # Optional
)

# Generate text
response = client.text.generate(
    prompt="Write a haiku about coding",
    temperature=0.7
)

print(response.content)
print(f"Cost: ${response.cost_usd:.4f}")
print(f"Provider: {response.provider_used}")
print(f"Model: {response.model_used}")
```

## API Overview

### Text Operations

```python
# Generate text
client.text.generate(prompt="...")

# Translate text
client.text.translate(text="...", target_language="es")

# Summarize text
client.text.summarize(text="...")

# Analyze text
client.text.analyze(text="...")

# And more: rewrite, expand, condense, classify, extract, compare
```

### Document Operations

```python
# Parse document
client.document.parse(document="...")

# Extract data
client.document.extract(document="...", extract_fields=["invoice_number", "total"])

# Classify document
client.document.classify(document="...")

# And more: structure, compare, generate
```

### Embeddings

```python
# Generate embeddings
embeddings = client.embeddings.generate(
    texts=["Hello world", "Machine learning"],
    model="voyage-2"  # Optional model override
)
```

### Discovery

```python
# Get available providers
catalog = client.discovery.get_catalog()

# Get available models
models = client.discovery.get_models(provider="claude")

# Get all providers
providers = client.discovery.get_providers()
```

### Provider Override

You can override the default provider for any request:

```python
# Use specific provider
response = client.text.generate(
    prompt="Hello",
    provider="claude",
    model="claude-3-5-sonnet-20241022"
)
```

## Configuration

### Environment Variables

```bash
export LLMHUB_API_KEY="your-api-key"
export LLMHUB_BASE_URL="https://your-instance.com"  # Optional
```

### In Code

```python
from llmhub import LLMHub

client = LLMHub(
    api_key="your-api-key",
    base_url="https://your-instance.com"  # Optional, defaults to standard endpoint
)
```

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for local development setup.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Requirements

- Python 3.9 or higher
- Valid LLMHub API key

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Links

- **Main Project**: [LLMHub](https://github.com/wapsol/llmhub)
- **SDK Development Tracker**: [Issue #63](https://github.com/wapsol/llmhub/issues/63)
- **Documentation**: Coming soon
- **PyPI Package**: Coming soon

## Roadmap

- [x] Repository setup
- [x] OpenAPI spec integration
- [ ] Base client generation with OpenAPI Generator
- [ ] Hand-crafted convenience wrapper
- [ ] Custom exception hierarchy
- [ ] Comprehensive test suite
- [ ] Sphinx documentation
- [ ] PyPI publication (v1.0.0)

**Target Release**: Week 4 of SDK development initiative

---

Generated as part of the LLMHub multi-language SDK initiative.
