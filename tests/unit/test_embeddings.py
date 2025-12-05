"""Unit tests for EmbeddingsOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.embeddings import EmbeddingsOperations
from llmhub.exceptions import (
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    return Mock()


@pytest.fixture
def embeddings_ops(mock_api_client, mock_api_key):
    """Create EmbeddingsOperations instance with mocked client."""
    return EmbeddingsOperations(mock_api_client, mock_api_key)


@pytest.mark.unit
class TestEmbeddingsGenerate:
    """Tests for embeddings generation."""

    def test_generate_single_text(self, embeddings_ops):
        """Test generating embeddings for a single text."""
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2, 0.3]]
        mock_response.dimensions = 3
        mock_response.cost_usd = 0.0001

        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post', return_value=mock_response):
            result = embeddings_ops.generate(texts=["Hello world"])
            assert len(result.embeddings) == 1
            assert result.dimensions == 3
            assert result.cost_usd == 0.0001

    def test_generate_multiple_texts(self, embeddings_ops):
        """Test generating embeddings for multiple texts."""
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
        mock_response.dimensions = 2

        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post', return_value=mock_response):
            result = embeddings_ops.generate(
                texts=["Text 1", "Text 2", "Text 3"]
            )
            assert len(result.embeddings) == 3
            assert result.dimensions == 2

    def test_generate_with_model(self, embeddings_ops):
        """Test generating embeddings with specific model."""
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2]]

        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post', return_value=mock_response):
            result = embeddings_ops.generate(
                texts=["Hello"],
                model="voyage-2"
            )
            assert result is not None

    def test_generate_with_provider(self, embeddings_ops):
        """Test generating embeddings with specific provider."""
        mock_response = Mock()
        mock_response.embeddings = [[0.1, 0.2]]

        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post', return_value=mock_response):
            result = embeddings_ops.generate(
                texts=["Hello"],
                provider="voyageai"
            )
            assert result is not None

    def test_generate_empty_list_raises_error(self, embeddings_ops):
        """Test that empty texts list raises ValidationError."""
        with pytest.raises(ValidationError, match="texts must be a non-empty list"):
            embeddings_ops.generate(texts=[])

    def test_generate_non_list_raises_error(self, embeddings_ops):
        """Test that non-list input raises ValidationError."""
        with pytest.raises(ValidationError, match="texts must be a non-empty list"):
            embeddings_ops.generate(texts="not a list")

    def test_generate_non_string_items_raises_error(self, embeddings_ops):
        """Test that non-string items raise ValidationError."""
        with pytest.raises(ValidationError, match="all items in texts must be strings"):
            embeddings_ops.generate(texts=["valid", 123, "also valid"])

    def test_generate_authentication_error(self, embeddings_ops):
        """Test handling of authentication errors."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=401)

            with pytest.raises(AuthenticationError):
                embeddings_ops.generate(texts=["Test"])

    def test_generate_rate_limit_error(self, embeddings_ops):
        """Test handling of rate limit errors."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            exc = ApiException(status=429)
            exc.headers = {'Retry-After': '30'}
            mock_post.side_effect = exc

            with pytest.raises(RateLimitError) as exc_info:
                embeddings_ops.generate(texts=["Test"])

            assert exc_info.value.retry_after == 30

    def test_generate_server_error(self, embeddings_ops):
        """Test handling of server errors."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=500)

            with pytest.raises(ServerError):
                embeddings_ops.generate(texts=["Test"])


@pytest.mark.unit
class TestExceptionConversion:
    """Tests for exception conversion."""

    def test_convert_401_to_authentication_error(self, embeddings_ops):
        """Test 401 converts to AuthenticationError."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=401)

            with pytest.raises(AuthenticationError):
                embeddings_ops.generate(texts=["Test"])

    def test_convert_403_to_authentication_error(self, embeddings_ops):
        """Test 403 converts to AuthenticationError."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=403)

            with pytest.raises(AuthenticationError):
                embeddings_ops.generate(texts=["Test"])

    def test_convert_422_to_validation_error(self, embeddings_ops):
        """Test 422 converts to ValidationError."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=422)

            with pytest.raises(ValidationError):
                embeddings_ops.generate(texts=["Test"])

    def test_convert_500_to_server_error(self, embeddings_ops):
        """Test 500 converts to ServerError."""
        with patch.object(embeddings_ops._api, 'generate_embeddings_api_v2_embeddings_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=500)

            with pytest.raises(ServerError):
                embeddings_ops.generate(texts=["Test"])
