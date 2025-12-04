# Development Guide

This guide covers local development setup for the LLMHub Python SDK.

## Prerequisites

- Python 3.9 or higher
- pip and virtualenv
- Node.js 18+ (for OpenAPI Generator CLI)
- Git

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/wapsol/llmhub-sdk-python.git
cd llmhub-sdk-python
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install package in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt
```

### 4. Install OpenAPI Generator

```bash
npm install -g @openapitools/openapi-generator-cli
```

## Development Workflow

### Regenerate Client from OpenAPI Spec

When the OpenAPI spec is updated:

```bash
./scripts/regenerate.sh
```

This script:
1. Generates base client from `openapi-spec.yaml`
2. Formats the generated code with Black and isort
3. Outputs to `generated/` directory

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=llmhub --cov-report=html

# Run specific test file
pytest tests/unit/test_client.py

# Run specific test
pytest tests/unit/test_client.py::test_initialization
```

### Code Quality

```bash
# Format code
black .
isort .

# Lint code
flake8

# Type checking
mypy llmhub
```

### Running All Quality Checks

```bash
# Format, lint, type check, and test
black . && isort . && flake8 && mypy llmhub && pytest
```

## Project Structure

```
llmhub-sdk-python/
├── llmhub/                    # Hand-crafted wrapper (edit this)
│   ├── __init__.py
│   ├── client.py             # Main LLMHub client
│   ├── text.py               # Text operations wrapper
│   ├── embeddings.py         # Embeddings wrapper
│   ├── exceptions.py         # Custom exceptions
│   └── ...                   # Other modality wrappers
├── generated/                 # Auto-generated (DO NOT EDIT)
│   └── llmhub_generated/
│       ├── api/
│       ├── models/
│       └── ...
├── tests/
│   ├── unit/                 # Unit tests
│   └── integration/          # Integration tests
├── docs/                     # Documentation
├── scripts/                  # Automation scripts
│   └── regenerate.sh
├── openapi-spec.yaml         # OpenAPI specification
├── openapi-config.yaml       # Generator configuration
├── pyproject.toml            # Project metadata
├── requirements.txt          # Runtime dependencies
└── requirements-dev.txt      # Development dependencies
```

## Writing Tests

### Unit Tests

```python
# tests/unit/test_client.py
import pytest
from llmhub import LLMHub

def test_client_initialization():
    client = LLMHub(api_key="test_key")
    assert client is not None

def test_invalid_api_key():
    with pytest.raises(ValueError):
        LLMHub(api_key="")
```

### Integration Tests

```python
# tests/integration/test_text.py
import pytest
from llmhub import LLMHub

@pytest.fixture
def client():
    return LLMHub(api_key="sk_test_...")

def test_text_generate(client):
    response = client.text.generate(prompt="Hello")
    assert response.success
    assert response.content
```

### Mocked Tests

```python
# tests/unit/test_text_mocked.py
from unittest.mock import Mock, patch
import pytest
from llmhub import LLMHub

@patch('llmhub_generated.api.text_api.TextApi.v2_text_generate_post')
def test_text_generate_mocked(mock_api):
    mock_api.return_value = {
        "success": True,
        "content": "Generated text",
        "cost_usd": 0.0015,
        "tokens_used": 100
    }

    client = LLMHub(api_key="test")
    response = client.text.generate(prompt="Test")

    assert response.content == "Generated text"
    mock_api.assert_called_once()
```

## Adding New Wrapper Methods

When adding wrapper methods to `llmhub/`, follow this pattern:

```python
# llmhub/text.py
from llmhub_generated.api.text_api import TextApi
from llmhub.exceptions import LLMHubError

class TextOperations:
    def __init__(self, client):
        self._api = TextApi(client)

    def generate(self, prompt: str, **kwargs):
        """
        Generate text from a prompt.

        Args:
            prompt: The input prompt
            **kwargs: Additional parameters (provider, model, temperature, etc.)

        Returns:
            TextGenerateResponse with content and metadata

        Raises:
            LLMHubError: If the API request fails

        Example:
            >>> client = LLMHub(api_key="sk_...")
            >>> response = client.text.generate(prompt="Hello")
            >>> print(response.content)
        """
        try:
            return self._api.v2_text_generate_post(prompt=prompt, **kwargs)
        except Exception as e:
            raise LLMHubError(f"Text generation failed: {str(e)}")
```

## Building Documentation

```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme

# Build docs
cd docs
make html

# View docs
open _build/html/index.html
```

## Publishing to PyPI

**Note: Only maintainers can publish releases.**

```bash
# Build distribution
python -m build

# Upload to PyPI (requires credentials)
twine upload dist/*
```

## Troubleshooting

### OpenAPI Generator Not Found

```bash
npm install -g @openapitools/openapi-generator-cli
```

### Generated Code Import Errors

```bash
# Regenerate client
./scripts/regenerate.sh

# Reinstall in development mode
pip install -e .
```

### Test Failures

```bash
# Clear pytest cache
rm -rf .pytest_cache

# Run tests with verbose output
pytest -vv
```

## Getting Help

- Open an issue: https://github.com/wapsol/llmhub-sdk-python/issues
- Main project: https://github.com/wapsol/llmhub
- SDK initiative: https://github.com/wapsol/llmhub/issues/63
