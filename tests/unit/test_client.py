"""Unit tests for the main LLMHub client."""

import pytest
from llmhub.client import LLMHub
from llmhub.exceptions import LLMHubError


@pytest.mark.unit
class TestLLMHubClient:
    """Test suite for LLMHub client initialization."""

    def test_client_initialization_with_api_key(self):
        """Test client can be initialized with API key."""
        client = LLMHub(api_key="test_key_123")
        assert client is not None
        # Add more assertions once client is implemented

    def test_client_initialization_with_base_url(self):
        """Test client can be initialized with custom base URL."""
        client = LLMHub(
            api_key="test_key_123",
            base_url="https://custom.llmhub.com"
        )
        assert client is not None
        # Add more assertions once client is implemented

    def test_client_initialization_without_api_key(self):
        """Test client raises error when API key is missing."""
        with pytest.raises((ValueError, LLMHubError)):
            LLMHub(api_key="")

    def test_client_initialization_with_invalid_api_key(self):
        """Test client handles invalid API key format."""
        # This test will be updated once validation is implemented
        client = LLMHub(api_key="invalid")
        assert client is not None
