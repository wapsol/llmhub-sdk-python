"""Unit tests for TextOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.text import TextOperations
from llmhub.exceptions import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    return Mock()


@pytest.fixture
def text_ops(mock_api_client, mock_api_key):
    """Create TextOperations instance with mocked client."""
    return TextOperations(mock_api_client, mock_api_key)


@pytest.mark.unit
class TestTextGenerate:
    """Tests for text generation."""

    def test_generate_basic(self, text_ops):
        """Test basic text generation."""
        mock_response = Mock()
        mock_response.content = "Generated text"
        mock_response.cost_usd = 0.001

        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post', return_value=mock_response):
            result = text_ops.generate(prompt="Hello")
            assert result.content == "Generated text"
            assert result.cost_usd == 0.001

    def test_generate_with_all_params(self, text_ops):
        """Test text generation with all parameters."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post', return_value=mock_response):
            result = text_ops.generate(
                prompt="Test prompt",
                system_prompt="System context",
                provider="claude",
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                temperature=0.7
            )
            assert result is not None

    def test_generate_authentication_error(self, text_ops):
        """Test handling of authentication errors."""
        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=401)

            with pytest.raises(AuthenticationError):
                text_ops.generate(prompt="Test")

    def test_generate_rate_limit_error(self, text_ops):
        """Test handling of rate limit errors."""
        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post') as mock_post:
            exc = ApiException(status=429)
            exc.headers = {'Retry-After': '60'}
            mock_post.side_effect = exc

            with pytest.raises(RateLimitError) as exc_info:
                text_ops.generate(prompt="Test")

            assert exc_info.value.retry_after == 60


@pytest.mark.unit
class TestTextTranslate:
    """Tests for text translation."""

    def test_translate_basic(self, text_ops):
        """Test basic translation."""
        mock_response = Mock()
        mock_response.content = "Hola"

        with patch.object(text_ops._api, 'translate_text_api_v2_text_translate_post', return_value=mock_response):
            result = text_ops.translate(text="Hello", target_language="es")
            assert result.content == "Hola"

    def test_translate_with_source(self, text_ops):
        """Test translation with source language."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'translate_text_api_v2_text_translate_post', return_value=mock_response):
            result = text_ops.translate(
                text="Hello",
                target_language="es",
                source_language="en"
            )
            assert result is not None


@pytest.mark.unit
class TestTextSummarize:
    """Tests for text summarization."""

    def test_summarize_basic(self, text_ops):
        """Test basic summarization."""
        mock_response = Mock()
        mock_response.content = "Summary"

        with patch.object(text_ops._api, 'summarize_text_api_v2_text_summarize_post', return_value=mock_response):
            result = text_ops.summarize(text="Long text here...")
            assert result.content == "Summary"

    def test_summarize_with_length(self, text_ops):
        """Test summarization with length parameter."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'summarize_text_api_v2_text_summarize_post', return_value=mock_response):
            result = text_ops.summarize(
                text="Long text",
                summary_length="short"
            )
            assert result is not None


@pytest.mark.unit
class TestTextRewrite:
    """Tests for text rewriting."""

    def test_rewrite_basic(self, text_ops):
        """Test basic rewriting."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'rewrite_text_api_v2_text_rewrite_post', return_value=mock_response):
            result = text_ops.rewrite(text="Original text")
            assert result is not None

    def test_rewrite_with_style(self, text_ops):
        """Test rewriting with style."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'rewrite_text_api_v2_text_rewrite_post', return_value=mock_response):
            result = text_ops.rewrite(text="Text", style="formal")
            assert result is not None


@pytest.mark.unit
class TestTextExpand:
    """Tests for text expansion."""

    def test_expand_basic(self, text_ops):
        """Test basic expansion."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'expand_text_api_v2_text_expand_post', return_value=mock_response):
            result = text_ops.expand(text="Brief text")
            assert result is not None


@pytest.mark.unit
class TestTextCondense:
    """Tests for text condensing."""

    def test_condense_basic(self, text_ops):
        """Test basic condensing."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'condense_text_api_v2_text_condense_post', return_value=mock_response):
            result = text_ops.condense(text="Detailed text")
            assert result is not None


@pytest.mark.unit
class TestTextAnalyze:
    """Tests for text analysis."""

    def test_analyze_basic(self, text_ops):
        """Test basic analysis."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'analyze_text_api_v2_text_analyze_post', return_value=mock_response):
            result = text_ops.analyze(text="Text to analyze")
            assert result is not None

    def test_analyze_with_type(self, text_ops):
        """Test analysis with type parameter."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'analyze_text_api_v2_text_analyze_post', return_value=mock_response):
            result = text_ops.analyze(
                text="Text",
                analysis_type="sentiment"
            )
            assert result is not None


@pytest.mark.unit
class TestTextClassify:
    """Tests for text classification."""

    def test_classify_basic(self, text_ops):
        """Test basic classification."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'classify_text_api_v2_text_classify_post', return_value=mock_response):
            result = text_ops.classify(text="Text to classify")
            assert result is not None

    def test_classify_with_categories(self, text_ops):
        """Test classification with categories."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'classify_text_api_v2_text_classify_post', return_value=mock_response):
            result = text_ops.classify(
                text="Text",
                categories=["cat1", "cat2", "cat3"]
            )
            assert result is not None


@pytest.mark.unit
class TestTextExtract:
    """Tests for text extraction."""

    def test_extract_basic(self, text_ops):
        """Test basic extraction."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'extract_from_text_api_v2_text_extract_post', return_value=mock_response):
            result = text_ops.extract(text="Text with entities")
            assert result is not None

    def test_extract_with_types(self, text_ops):
        """Test extraction with types."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'extract_from_text_api_v2_text_extract_post', return_value=mock_response):
            result = text_ops.extract(
                text="Text",
                extract_types=["entities", "keywords"]
            )
            assert result is not None


@pytest.mark.unit
class TestTextCompare:
    """Tests for text comparison."""

    def test_compare_basic(self, text_ops):
        """Test basic comparison."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'compare_texts_api_v2_text_compare_post', return_value=mock_response):
            result = text_ops.compare(text1="First", text2="Second")
            assert result is not None

    def test_compare_with_type(self, text_ops):
        """Test comparison with type."""
        mock_response = Mock()

        with patch.object(text_ops._api, 'compare_texts_api_v2_text_compare_post', return_value=mock_response):
            result = text_ops.compare(
                text1="First",
                text2="Second",
                comparison_type="similarity"
            )
            assert result is not None


@pytest.mark.unit
class TestExceptionConversion:
    """Tests for exception conversion."""

    def test_convert_401_to_authentication_error(self, text_ops):
        """Test 401 converts to AuthenticationError."""
        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=401)

            with pytest.raises(AuthenticationError):
                text_ops.generate(prompt="Test")

    def test_convert_422_to_validation_error(self, text_ops):
        """Test 422 converts to ValidationError."""
        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=422)

            with pytest.raises(ValidationError):
                text_ops.generate(prompt="Test")

    def test_convert_500_to_server_error(self, text_ops):
        """Test 500 converts to ServerError."""
        with patch.object(text_ops._api, 'generate_text_api_v2_text_generate_post') as mock_post:
            mock_post.side_effect = ApiException(status=500)

            with pytest.raises(ServerError):
                text_ops.generate(prompt="Test")
