"""Unit tests for DocumentOperations."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from llmhub.document import DocumentOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError,
    LLMHubError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def document_ops(mock_api_key):
    """Create DocumentOperations instance for testing."""
    mock_client = Mock()
    return DocumentOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.content = "Extracted document content"
    response.provider_used = "provider"
    response.model_used = "model"
    response.cost_usd = 0.001
    return response


class TestDocumentParse:
    """Tests for parse() method."""

    def test_parse_success(self, document_ops, mock_response):
        """Test successful document parsing."""
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            return_value=mock_response
        ):
            response = document_ops.parse(
                document_url="https://example.com/doc.pdf"
            )
            assert response.success is True
            assert response.content == "Extracted document content"

    def test_parse_with_options(self, document_ops, mock_response):
        """Test parsing with output format and options."""
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            return_value=mock_response
        ):
            response = document_ops.parse(
                document_url="https://example.com/doc.pdf",
                output_format="markdown",
                provider="provider",
                model="model"
            )
            assert response.success is True


class TestDocumentExtract:
    """Tests for extract() method."""

    def test_extract_success(self, document_ops, mock_response):
        """Test successful data extraction."""
        with patch.object(
            document_ops._api,
            'extract_data_api_v2_document_extract_post',
            return_value=mock_response
        ):
            response = document_ops.extract(
                document_url="https://example.com/invoice.pdf",
                extraction_schema={"fields": ["total", "date"]}
            )
            assert response.success is True

    def test_extract_with_instructions(self, document_ops, mock_response):
        """Test extraction with custom instructions."""
        with patch.object(
            document_ops._api,
            'extract_data_api_v2_document_extract_post',
            return_value=mock_response
        ):
            response = document_ops.extract(
                document_url="https://example.com/contract.pdf",
                extraction_schema={"fields": ["party_a", "party_b"]},
                extraction_instructions="Extract all party names"
            )
            assert response.success is True


class TestDocumentClassify:
    """Tests for classify() method."""

    def test_classify_success(self, document_ops, mock_response):
        """Test successful document classification."""
        with patch.object(
            document_ops._api,
            'classify_document_api_v2_document_classify_post',
            return_value=mock_response
        ):
            response = document_ops.classify(
                document_url="https://example.com/doc.pdf",
                categories=["invoice", "contract", "receipt"]
            )
            assert response.success is True

    def test_classify_with_provider(self, document_ops, mock_response):
        """Test classification with provider override."""
        with patch.object(
            document_ops._api,
            'classify_document_api_v2_document_classify_post',
            return_value=mock_response
        ):
            response = document_ops.classify(
                document_url="https://example.com/doc.pdf",
                categories=["legal", "financial"],
                provider="claude"
            )
            assert response.success is True


class TestDocumentCompare:
    """Tests for compare() method."""

    def test_compare_success(self, document_ops, mock_response):
        """Test successful document comparison."""
        with patch.object(
            document_ops._api,
            'compare_documents_api_v2_document_compare_post',
            return_value=mock_response
        ):
            response = document_ops.compare(
                document_url1="https://example.com/doc1.pdf",
                document_url2="https://example.com/doc2.pdf"
            )
            assert response.success is True

    def test_compare_with_aspects(self, document_ops, mock_response):
        """Test comparison with specific aspects."""
        with patch.object(
            document_ops._api,
            'compare_documents_api_v2_document_compare_post',
            return_value=mock_response
        ):
            response = document_ops.compare(
                document_url1="https://example.com/v1.pdf",
                document_url2="https://example.com/v2.pdf",
                comparison_aspects=["structure", "content", "formatting"]
            )
            assert response.success is True


class TestDocumentGenerate:
    """Tests for generate() method."""

    def test_generate_success(self, document_ops, mock_response):
        """Test successful document generation."""
        with patch.object(
            document_ops._api,
            'generate_document_api_v2_document_generate_post',
            return_value=mock_response
        ):
            response = document_ops.generate(
                content="Document content here",
                document_type="pdf"
            )
            assert response.success is True

    def test_generate_with_template(self, document_ops, mock_response):
        """Test generation with template."""
        with patch.object(
            document_ops._api,
            'generate_document_api_v2_document_generate_post',
            return_value=mock_response
        ):
            response = document_ops.generate(
                content="Report content",
                document_type="docx",
                template_url="https://example.com/template.docx"
            )
            assert response.success is True


class TestDocumentStructure:
    """Tests for structure() method."""

    def test_structure_success(self, document_ops, mock_response):
        """Test successful structure analysis."""
        with patch.object(
            document_ops._api,
            'analyze_structure_api_v2_document_structure_post',
            return_value=mock_response
        ):
            response = document_ops.structure(
                document_url="https://example.com/doc.pdf"
            )
            assert response.success is True

    def test_structure_with_detail(self, document_ops, mock_response):
        """Test structure analysis with detail level."""
        with patch.object(
            document_ops._api,
            'analyze_structure_api_v2_document_structure_post',
            return_value=mock_response
        ):
            response = document_ops.structure(
                document_url="https://example.com/doc.pdf",
                detail_level="detailed"
            )
            assert response.success is True


class TestDocumentErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, document_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                document_ops.parse(document_url="https://example.com/doc.pdf")

    def test_validation_error(self, document_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                document_ops.parse(document_url="https://example.com/doc.pdf")

    def test_rate_limit_error(self, document_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '60'}
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                document_ops.parse(document_url="https://example.com/doc.pdf")
            assert exc_info.value.retry_after == 60

    def test_server_error(self, document_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            document_ops._api,
            'parse_document_api_v2_document_parse_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                document_ops.parse(document_url="https://example.com/doc.pdf")
