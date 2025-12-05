"""Unit tests for ModerationOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.moderation import ModerationOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def moderation_ops(mock_api_key):
    """Create ModerationOperations instance for testing."""
    mock_client = Mock()
    return ModerationOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.flagged = False
    response.scores = {"toxicity": 0.1, "severe_toxicity": 0.05}
    response.provider_used = "perspective"
    return response


class TestModerate:
    """Tests for moderate() method."""

    def test_moderate_success(self, moderation_ops, mock_response):
        """Test successful content moderation."""
        with patch.object(
            moderation_ops._api,
            'moderate_content_api_v2_moderation_moderate_post',
            return_value=mock_response
        ):
            response = moderation_ops.moderate(
                content="User-generated text to check"
            )
            assert response.success is True
            assert response.flagged is False

    def test_moderate_with_categories(self, moderation_ops, mock_response):
        """Test moderation with specific categories."""
        with patch.object(
            moderation_ops._api,
            'moderate_content_api_v2_moderation_moderate_post',
            return_value=mock_response
        ):
            response = moderation_ops.moderate(
                content="Comment to moderate",
                categories=["hate", "harassment", "violence"]
            )
            assert response.success is True

    def test_moderate_with_provider(self, moderation_ops, mock_response):
        """Test moderation with provider override."""
        with patch.object(
            moderation_ops._api,
            'moderate_content_api_v2_moderation_moderate_post',
            return_value=mock_response
        ):
            response = moderation_ops.moderate(
                content="Test content",
                categories=["sexual"],
                provider="openai",
                model="text-moderation-latest"
            )
            assert response.success is True


class TestDetect:
    """Tests for detect() method."""

    def test_detect_success(self, moderation_ops, mock_response):
        """Test successful content detection."""
        with patch.object(
            moderation_ops._api,
            'detect_content_types_api_v2_moderation_detect_post',
            return_value=mock_response
        ):
            response = moderation_ops.detect(
                content="Email me at john@example.com"
            )
            assert response.success is True

    def test_detect_pii(self, moderation_ops, mock_response):
        """Test PII detection."""
        with patch.object(
            moderation_ops._api,
            'detect_content_types_api_v2_moderation_detect_post',
            return_value=mock_response
        ):
            response = moderation_ops.detect(
                content="My SSN is 123-45-6789",
                detection_types=["pii", "ssn"]
            )
            assert response.success is True

    def test_detect_spam(self, moderation_ops, mock_response):
        """Test spam detection."""
        with patch.object(
            moderation_ops._api,
            'detect_content_types_api_v2_moderation_detect_post',
            return_value=mock_response
        ):
            response = moderation_ops.detect(
                content="Click here for FREE stuff!!!",
                detection_types=["spam"],
                provider="custom"
            )
            assert response.success is True


class TestAnalyzeToxicity:
    """Tests for analyze_toxicity() method."""

    def test_analyze_toxicity_success(self, moderation_ops, mock_response):
        """Test successful toxicity analysis."""
        with patch.object(
            moderation_ops._api,
            'analyze_toxicity_api_v2_moderation_analyze_toxicity_post',
            return_value=mock_response
        ):
            response = moderation_ops.analyze_toxicity(
                content="Potentially toxic comment"
            )
            assert response.success is True
            assert response.scores is not None

    def test_analyze_toxicity_with_attributes(self, moderation_ops, mock_response):
        """Test toxicity analysis with specific attributes."""
        with patch.object(
            moderation_ops._api,
            'analyze_toxicity_api_v2_moderation_analyze_toxicity_post',
            return_value=mock_response
        ):
            response = moderation_ops.analyze_toxicity(
                content="Comment to analyze",
                attributes=["toxicity", "severe_toxicity", "threat"]
            )
            assert response.success is True

    def test_analyze_toxicity_perspective(self, moderation_ops, mock_response):
        """Test toxicity analysis with Perspective API."""
        with patch.object(
            moderation_ops._api,
            'analyze_toxicity_api_v2_moderation_analyze_toxicity_post',
            return_value=mock_response
        ):
            response = moderation_ops.analyze_toxicity(
                content="Test content",
                attributes=["insult", "profanity"],
                provider="perspective"
            )
            assert response.success is True


class TestModerationErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, moderation_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            moderation_ops._api,
            'moderate_content_api_v2_moderation_moderate_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                moderation_ops.moderate(content="Test")

    def test_validation_error(self, moderation_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            moderation_ops._api,
            'detect_content_types_api_v2_moderation_detect_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                moderation_ops.detect(content="Test")

    def test_rate_limit_error(self, moderation_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '45'}
        with patch.object(
            moderation_ops._api,
            'analyze_toxicity_api_v2_moderation_analyze_toxicity_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                moderation_ops.analyze_toxicity(content="Test")
            assert exc_info.value.retry_after == 45

    def test_server_error(self, moderation_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            moderation_ops._api,
            'moderate_content_api_v2_moderation_moderate_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                moderation_ops.moderate(content="Test")
