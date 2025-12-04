"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def mock_api_key():
    """Provide a mock API key for testing."""
    return "sk_test_1234567890abcdefghijklmnopqrstuvwxyz"


@pytest.fixture
def mock_base_url():
    """Provide a mock base URL for testing."""
    return "https://api.test.llmhub.com"


@pytest.fixture
def mock_api_response():
    """Provide a mock API response for testing."""
    return {
        "success": True,
        "content": "Generated text content",
        "provider_used": "claude",
        "model_used": "claude-3-5-sonnet-20241022",
        "cost_usd": 0.0015,
        "tokens_used": 100,
        "generation_time_ms": 1200,
        "log_id": "550e8400-e29b-41d4-a716-446655440000"
    }


@pytest.fixture
def mock_error_response():
    """Provide a mock error response for testing."""
    return {
        "success": False,
        "error": "Invalid API key",
        "error_code": "authentication_error"
    }
