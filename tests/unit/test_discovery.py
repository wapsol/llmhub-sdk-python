"""Unit tests for DiscoveryOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.discovery import DiscoveryOperations
from llmhub.exceptions import (
    AuthenticationError,
    RateLimitError,
    ServerError,
    LLMHubError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def discovery_ops(mock_api_key):
    """Create DiscoveryOperations instance for testing."""
    mock_client = Mock()
    return DiscoveryOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_catalog_response():
    """Create a mock catalog response."""
    response = Mock()
    response.providers = [
        Mock(name="claude", models=["claude-3-5-sonnet", "claude-3-opus"]),
        Mock(name="openai", models=["gpt-4", "gpt-3.5-turbo"])
    ]
    return response


@pytest.fixture
def mock_providers_response():
    """Create a mock providers response."""
    response = Mock()
    response.providers = [
        Mock(name="claude", description="Anthropic Claude models"),
        Mock(name="openai", description="OpenAI GPT models")
    ]
    return response


@pytest.fixture
def mock_models_response():
    """Create a mock models response."""
    response = Mock()
    response.models = [
        Mock(name="claude-3-5-sonnet", price_per_1k_tokens=0.003),
        Mock(name="gpt-4", price_per_1k_tokens=0.03)
    ]
    return response


class TestGetCatalog:
    """Tests for get_catalog() method."""

    def test_get_catalog_success(self, discovery_ops, mock_catalog_response):
        """Test successful catalog retrieval."""
        with patch.object(
            discovery_ops._api,
            'get_catalog_api_v2_discovery_catalog_get',
            return_value=mock_catalog_response
        ):
            response = discovery_ops.get_catalog()
            assert len(response.providers) == 2
            assert response.providers[0].name == "claude"

    def test_get_catalog_provider_count(self, discovery_ops, mock_catalog_response):
        """Test catalog contains expected providers."""
        with patch.object(
            discovery_ops._api,
            'get_catalog_api_v2_discovery_catalog_get',
            return_value=mock_catalog_response
        ):
            response = discovery_ops.get_catalog()
            provider_names = [p.name for p in response.providers]
            assert "claude" in provider_names
            assert "openai" in provider_names


class TestGetProviders:
    """Tests for get_providers() method."""

    def test_get_providers_success(self, discovery_ops, mock_providers_response):
        """Test successful providers retrieval."""
        with patch.object(
            discovery_ops._api,
            'get_providers_api_v2_discovery_providers_get',
            return_value=mock_providers_response
        ):
            response = discovery_ops.get_providers()
            assert len(response.providers) == 2

    def test_get_providers_with_modality(self, discovery_ops, mock_providers_response):
        """Test providers retrieval with modality filter."""
        with patch.object(
            discovery_ops._api,
            'get_providers_api_v2_discovery_providers_get',
            return_value=mock_providers_response
        ):
            response = discovery_ops.get_providers(modality="text")
            assert len(response.providers) == 2

    def test_get_providers_no_filter(self, discovery_ops, mock_providers_response):
        """Test providers retrieval without filter."""
        with patch.object(
            discovery_ops._api,
            'get_providers_api_v2_discovery_providers_get',
            return_value=mock_providers_response
        ):
            response = discovery_ops.get_providers(modality=None)
            assert response.providers is not None


class TestGetModels:
    """Tests for get_models() method."""

    def test_get_models_success(self, discovery_ops, mock_models_response):
        """Test successful models retrieval."""
        with patch.object(
            discovery_ops._api,
            'get_models_api_v2_discovery_models_get',
            return_value=mock_models_response
        ):
            response = discovery_ops.get_models()
            assert len(response.models) == 2

    def test_get_models_with_provider(self, discovery_ops, mock_models_response):
        """Test models retrieval with provider filter."""
        with patch.object(
            discovery_ops._api,
            'get_models_api_v2_discovery_models_get',
            return_value=mock_models_response
        ):
            response = discovery_ops.get_models(provider="claude")
            assert len(response.models) == 2

    def test_get_models_with_modality(self, discovery_ops, mock_models_response):
        """Test models retrieval with modality filter."""
        with patch.object(
            discovery_ops._api,
            'get_models_api_v2_discovery_models_get',
            return_value=mock_models_response
        ):
            response = discovery_ops.get_models(modality="text")
            assert len(response.models) == 2

    def test_get_models_with_both_filters(self, discovery_ops, mock_models_response):
        """Test models retrieval with both provider and modality filters."""
        with patch.object(
            discovery_ops._api,
            'get_models_api_v2_discovery_models_get',
            return_value=mock_models_response
        ):
            response = discovery_ops.get_models(
                provider="claude",
                modality="text"
            )
            assert len(response.models) == 2


class TestDiscoveryErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, discovery_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            discovery_ops._api,
            'get_catalog_api_v2_discovery_catalog_get',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                discovery_ops.get_catalog()

    def test_forbidden_error(self, discovery_ops):
        """Test forbidden error conversion."""
        api_exception = ApiException(status=403, reason="Forbidden")
        with patch.object(
            discovery_ops._api,
            'get_providers_api_v2_discovery_providers_get',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError, match="Access forbidden"):
                discovery_ops.get_providers()

    def test_rate_limit_error(self, discovery_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '30'}
        with patch.object(
            discovery_ops._api,
            'get_models_api_v2_discovery_models_get',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                discovery_ops.get_models()
            assert exc_info.value.retry_after == 30

    def test_server_error(self, discovery_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            discovery_ops._api,
            'get_catalog_api_v2_discovery_catalog_get',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                discovery_ops.get_catalog()

    def test_generic_error(self, discovery_ops):
        """Test generic error conversion."""
        api_exception = ApiException(status=418, reason="I'm a teapot")
        with patch.object(
            discovery_ops._api,
            'get_catalog_api_v2_discovery_catalog_get',
            side_effect=api_exception
        ):
            with pytest.raises(LLMHubError, match="API error"):
                discovery_ops.get_catalog()
