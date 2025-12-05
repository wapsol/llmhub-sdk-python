"""Unit tests for ImageOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.image import ImageOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def image_ops(mock_api_key):
    """Create ImageOperations instance for testing."""
    mock_client = Mock()
    return ImageOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.image_url = "https://example.com/image.png"
    response.content = "Image description"
    response.provider_used = "dalle"
    response.cost_usd = 0.02
    return response


class TestGenerate:
    """Tests for generate() method."""

    def test_generate_success(self, image_ops, mock_response):
        """Test successful image generation."""
        with patch.object(
            image_ops._api,
            'generate_image_api_v2_image_generate_post',
            return_value=mock_response
        ):
            response = image_ops.generate(
                prompt="A serene mountain landscape at sunset"
            )
            assert response.success is True
            assert response.image_url is not None

    def test_generate_with_size(self, image_ops, mock_response):
        """Test generation with size specification."""
        with patch.object(
            image_ops._api,
            'generate_image_api_v2_image_generate_post',
            return_value=mock_response
        ):
            response = image_ops.generate(
                prompt="Abstract art",
                size="1024x1024"
            )
            assert response.success is True

    def test_generate_with_style(self, image_ops, mock_response):
        """Test generation with style."""
        with patch.object(
            image_ops._api,
            'generate_image_api_v2_image_generate_post',
            return_value=mock_response
        ):
            response = image_ops.generate(
                prompt="City skyline",
                size="512x512",
                style="realistic",
                provider="midjourney"
            )
            assert response.success is True


class TestEdit:
    """Tests for edit() method."""

    def test_edit_success(self, image_ops, mock_response):
        """Test successful image editing."""
        with patch.object(
            image_ops._api,
            'edit_image_api_v2_image_edit_post',
            return_value=mock_response
        ):
            response = image_ops.edit(
                image_url="https://example.com/photo.jpg",
                prompt="Add sunglasses to the person"
            )
            assert response.success is True

    def test_edit_with_mask(self, image_ops, mock_response):
        """Test editing with mask for inpainting."""
        with patch.object(
            image_ops._api,
            'edit_image_api_v2_image_edit_post',
            return_value=mock_response
        ):
            response = image_ops.edit(
                image_url="https://example.com/photo.jpg",
                prompt="Change background to beach",
                mask_url="https://example.com/mask.png"
            )
            assert response.success is True


class TestAnalyze:
    """Tests for analyze() method."""

    def test_analyze_success(self, image_ops, mock_response):
        """Test successful image analysis."""
        with patch.object(
            image_ops._api,
            'analyze_image_api_v2_image_analyze_post',
            return_value=mock_response
        ):
            response = image_ops.analyze(
                image_url="https://example.com/photo.jpg"
            )
            assert response.success is True

    def test_analyze_objects(self, image_ops, mock_response):
        """Test object detection analysis."""
        with patch.object(
            image_ops._api,
            'analyze_image_api_v2_image_analyze_post',
            return_value=mock_response
        ):
            response = image_ops.analyze(
                image_url="https://example.com/scene.jpg",
                analysis_type="objects"
            )
            assert response.success is True

    def test_analyze_faces(self, image_ops, mock_response):
        """Test face detection analysis."""
        with patch.object(
            image_ops._api,
            'analyze_image_api_v2_image_analyze_post',
            return_value=mock_response
        ):
            response = image_ops.analyze(
                image_url="https://example.com/portrait.jpg",
                analysis_type="faces",
                provider="custom"
            )
            assert response.success is True


class TestDescribe:
    """Tests for describe() method."""

    def test_describe_success(self, image_ops, mock_response):
        """Test successful image description."""
        with patch.object(
            image_ops._api,
            'describe_image_api_v2_image_describe_post',
            return_value=mock_response
        ):
            response = image_ops.describe(
                image_url="https://example.com/photo.jpg"
            )
            assert response.success is True
            assert response.content is not None

    def test_describe_with_detail(self, image_ops, mock_response):
        """Test description with detail level."""
        with patch.object(
            image_ops._api,
            'describe_image_api_v2_image_describe_post',
            return_value=mock_response
        ):
            response = image_ops.describe(
                image_url="https://example.com/artwork.jpg",
                detail_level="comprehensive"
            )
            assert response.success is True


class TestUpscale:
    """Tests for upscale() method."""

    def test_upscale_success(self, image_ops, mock_response):
        """Test successful image upscaling."""
        with patch.object(
            image_ops._api,
            'upscale_image_api_v2_image_upscale_post',
            return_value=mock_response
        ):
            response = image_ops.upscale(
                image_url="https://example.com/low_res.jpg"
            )
            assert response.success is True

    def test_upscale_with_factor(self, image_ops, mock_response):
        """Test upscaling with scale factor."""
        with patch.object(
            image_ops._api,
            'upscale_image_api_v2_image_upscale_post',
            return_value=mock_response
        ):
            response = image_ops.upscale(
                image_url="https://example.com/small.jpg",
                scale_factor=4
            )
            assert response.success is True


class TestVary:
    """Tests for vary() method."""

    def test_vary_success(self, image_ops, mock_response):
        """Test successful image variation."""
        with patch.object(
            image_ops._api,
            'vary_image_api_v2_image_vary_post',
            return_value=mock_response
        ):
            response = image_ops.vary(
                image_url="https://example.com/base.jpg"
            )
            assert response.success is True

    def test_vary_with_strength(self, image_ops, mock_response):
        """Test variation with strength parameter."""
        with patch.object(
            image_ops._api,
            'vary_image_api_v2_image_vary_post',
            return_value=mock_response
        ):
            response = image_ops.vary(
                image_url="https://example.com/original.jpg",
                variation_strength=0.7
            )
            assert response.success is True


class TestImageErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, image_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            image_ops._api,
            'generate_image_api_v2_image_generate_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                image_ops.generate(prompt="Test image")

    def test_validation_error(self, image_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            image_ops._api,
            'edit_image_api_v2_image_edit_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                image_ops.edit(
                    image_url="invalid",
                    prompt="Edit"
                )

    def test_rate_limit_error(self, image_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '60'}
        with patch.object(
            image_ops._api,
            'analyze_image_api_v2_image_analyze_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                image_ops.analyze(image_url="https://example.com/image.jpg")
            assert exc_info.value.retry_after == 60

    def test_server_error(self, image_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            image_ops._api,
            'upscale_image_api_v2_image_upscale_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                image_ops.upscale(image_url="https://example.com/image.jpg")
