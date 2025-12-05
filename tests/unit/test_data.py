"""Unit tests for DataOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.data import DataOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def data_ops(mock_api_key):
    """Create DataOperations instance for testing."""
    mock_client = Mock()
    return DataOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_embeddings_response():
    """Create a mock embeddings response."""
    response = Mock()
    response.success = True
    response.embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    response.provider_used = "voyage"
    response.model_used = "voyage-2"
    response.cost_usd = 0.0001
    return response


@pytest.fixture
def mock_rerank_response():
    """Create a mock rerank response."""
    response = Mock()
    response.success = True
    response.ranked_documents = [
        Mock(text="Doc 1", score=0.95),
        Mock(text="Doc 2", score=0.82)
    ]
    response.provider_used = "cohere"
    return response


class TestEmbed:
    """Tests for embed() method."""

    def test_embed_success(self, data_ops, mock_embeddings_response):
        """Test successful embedding generation."""
        with patch.object(
            data_ops._api,
            'generate_embeddings_api_v2_data_embed_post',
            return_value=mock_embeddings_response
        ):
            response = data_ops.embed(
                texts=["Document 1", "Document 2", "Document 3"]
            )
            assert response.success is True
            assert len(response.embeddings) == 2

    def test_embed_with_model(self, data_ops, mock_embeddings_response):
        """Test embedding with model override."""
        with patch.object(
            data_ops._api,
            'generate_embeddings_api_v2_data_embed_post',
            return_value=mock_embeddings_response
        ):
            response = data_ops.embed(
                texts=["Text 1", "Text 2"],
                model="voyage-lite-02"
            )
            assert response.success is True

    def test_embed_with_provider(self, data_ops, mock_embeddings_response):
        """Test embedding with provider override."""
        with patch.object(
            data_ops._api,
            'generate_embeddings_api_v2_data_embed_post',
            return_value=mock_embeddings_response
        ):
            response = data_ops.embed(
                texts=["Sample text"],
                provider="openai",
                model="text-embedding-3-large"
            )
            assert response.success is True

    def test_embed_empty_list(self, data_ops):
        """Test embedding with empty list raises error."""
        with pytest.raises(ValidationError, match="texts must be a non-empty list"):
            data_ops.embed(texts=[])

    def test_embed_non_list(self, data_ops):
        """Test embedding with non-list raises error."""
        with pytest.raises(ValidationError, match="texts must be a non-empty list"):
            data_ops.embed(texts="not a list")

    def test_embed_non_string_items(self, data_ops):
        """Test embedding with non-string items raises error."""
        with pytest.raises(ValidationError, match="all items in texts must be strings"):
            data_ops.embed(texts=["valid", 123, "also valid"])


class TestRerank:
    """Tests for rerank() method."""

    def test_rerank_success(self, data_ops, mock_rerank_response):
        """Test successful document reranking."""
        with patch.object(
            data_ops._api,
            'rerank_documents_api_v2_data_rerank_post',
            return_value=mock_rerank_response
        ):
            response = data_ops.rerank(
                query="machine learning",
                documents=["Doc about ML", "Doc about cooking", "Doc about AI"]
            )
            assert response.success is True
            assert len(response.ranked_documents) == 2

    def test_rerank_with_top_k(self, data_ops, mock_rerank_response):
        """Test reranking with top_k parameter."""
        with patch.object(
            data_ops._api,
            'rerank_documents_api_v2_data_rerank_post',
            return_value=mock_rerank_response
        ):
            response = data_ops.rerank(
                query="artificial intelligence",
                documents=["AI doc", "Cooking doc", "ML doc", "Sports doc"],
                top_k=2
            )
            assert response.success is True

    def test_rerank_with_provider(self, data_ops, mock_rerank_response):
        """Test reranking with provider override."""
        with patch.object(
            data_ops._api,
            'rerank_documents_api_v2_data_rerank_post',
            return_value=mock_rerank_response
        ):
            response = data_ops.rerank(
                query="python programming",
                documents=["Python doc", "Java doc", "Ruby doc"],
                top_k=3,
                provider="cohere",
                model="rerank-english-v2.0"
            )
            assert response.success is True


class TestDataErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, data_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            data_ops._api,
            'generate_embeddings_api_v2_data_embed_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                data_ops.embed(texts=["Test"])

    def test_validation_error(self, data_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            data_ops._api,
            'rerank_documents_api_v2_data_rerank_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                data_ops.rerank(query="test", documents=["doc"])

    def test_rate_limit_error(self, data_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '90'}
        with patch.object(
            data_ops._api,
            'generate_embeddings_api_v2_data_embed_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                data_ops.embed(texts=["Test"])
            assert exc_info.value.retry_after == 90

    def test_server_error(self, data_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            data_ops._api,
            'rerank_documents_api_v2_data_rerank_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                data_ops.rerank(query="test", documents=["doc"])
