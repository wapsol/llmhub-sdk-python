"""Unit tests for custom exceptions."""

import pytest
from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ProviderError
)


@pytest.mark.unit
class TestExceptions:
    """Test suite for custom exception classes."""

    def test_llmhub_error_base(self):
        """Test base LLMHubError exception."""
        error = LLMHubError("Test error")
        assert str(error) == "Test error"
        assert isinstance(error, Exception)

    def test_authentication_error(self):
        """Test AuthenticationError exception."""
        error = AuthenticationError("Invalid API key")
        assert str(error) == "Invalid API key"
        assert isinstance(error, LLMHubError)

    def test_rate_limit_error(self):
        """Test RateLimitError exception."""
        error = RateLimitError("Rate limit exceeded", retry_after=60)
        assert str(error) == "Rate limit exceeded"
        assert error.retry_after == 60
        assert isinstance(error, LLMHubError)

    def test_rate_limit_error_without_retry_after(self):
        """Test RateLimitError without retry_after parameter."""
        error = RateLimitError("Rate limit exceeded")
        assert str(error) == "Rate limit exceeded"
        assert error.retry_after is None

    def test_provider_error(self):
        """Test ProviderError exception."""
        error = ProviderError("Provider unavailable")
        assert str(error) == "Provider unavailable"
        assert isinstance(error, LLMHubError)
