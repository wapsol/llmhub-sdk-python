"""Unit tests for VideoOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.video import VideoOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def video_ops(mock_api_key):
    """Create VideoOperations instance for testing."""
    mock_client = Mock()
    return VideoOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.video_url = "https://example.com/video.mp4"
    response.content = "Video description"
    response.provider_used = "runway"
    response.cost_usd = 0.05
    return response


class TestGenerate:
    """Tests for generate() method."""

    def test_generate_success(self, video_ops, mock_response):
        """Test successful video generation."""
        with patch.object(
            video_ops._api,
            'generate_video_api_v2_video_generate_post',
            return_value=mock_response
        ):
            response = video_ops.generate(
                prompt="A serene mountain landscape"
            )
            assert response.success is True
            assert response.video_url is not None

    def test_generate_with_options(self, video_ops, mock_response):
        """Test generation with all options."""
        with patch.object(
            video_ops._api,
            'generate_video_api_v2_video_generate_post',
            return_value=mock_response
        ):
            response = video_ops.generate(
                prompt="Sunset over ocean",
                duration=10,
                aspect_ratio="16:9",
                include_audio=True,
                provider="pika"
            )
            assert response.success is True

    def test_generate_with_image(self, video_ops, mock_response):
        """Test generation with prompt image."""
        with patch.object(
            video_ops._api,
            'generate_video_api_v2_video_generate_post',
            return_value=mock_response
        ):
            response = video_ops.generate(
                prompt="Animate this scene",
                prompt_image="https://example.com/scene.jpg"
            )
            assert response.success is True


class TestDescribe:
    """Tests for describe() method."""

    def test_describe_success(self, video_ops, mock_response):
        """Test successful video description."""
        with patch.object(
            video_ops._api,
            'describe_video_api_v2_video_describe_post',
            return_value=mock_response
        ):
            response = video_ops.describe(
                video_url="https://example.com/video.mp4"
            )
            assert response.success is True
            assert response.content is not None

    def test_describe_with_detail(self, video_ops, mock_response):
        """Test description with detail level."""
        with patch.object(
            video_ops._api,
            'describe_video_api_v2_video_describe_post',
            return_value=mock_response
        ):
            response = video_ops.describe(
                video_url="https://example.com/video.mp4",
                detail_level="comprehensive"
            )
            assert response.success is True


class TestClip:
    """Tests for clip() method."""

    def test_clip_success(self, video_ops, mock_response):
        """Test successful video clipping."""
        with patch.object(
            video_ops._api,
            'create_video_clips_api_v2_video_clip_post',
            return_value=mock_response
        ):
            response = video_ops.clip(
                video_url="https://example.com/video.mp4",
                start_time=5.0,
                end_time=15.0
            )
            assert response.success is True

    def test_clip_without_times(self, video_ops, mock_response):
        """Test clipping without specific times."""
        with patch.object(
            video_ops._api,
            'create_video_clips_api_v2_video_clip_post',
            return_value=mock_response
        ):
            response = video_ops.clip(
                video_url="https://example.com/video.mp4"
            )
            assert response.success is True


class TestExtend:
    """Tests for extend() method."""

    def test_extend_success(self, video_ops, mock_response):
        """Test successful video extension."""
        with patch.object(
            video_ops._api,
            'extend_video_api_v2_video_extend_post',
            return_value=mock_response
        ):
            response = video_ops.extend(
                video_url="https://example.com/video.mp4",
                extension_duration=5
            )
            assert response.success is True

    def test_extend_with_direction(self, video_ops, mock_response):
        """Test extension with direction."""
        with patch.object(
            video_ops._api,
            'extend_video_api_v2_video_extend_post',
            return_value=mock_response
        ):
            response = video_ops.extend(
                video_url="https://example.com/video.mp4",
                extension_duration=3,
                direction="forward"
            )
            assert response.success is True


class TestInterpolate:
    """Tests for interpolate() method."""

    def test_interpolate_success(self, video_ops, mock_response):
        """Test successful video interpolation."""
        with patch.object(
            video_ops._api,
            'interpolate_video_api_v2_video_interpolate_post',
            return_value=mock_response
        ):
            response = video_ops.interpolate(
                video_url="https://example.com/video.mp4",
                target_fps=60
            )
            assert response.success is True

    def test_interpolate_default(self, video_ops, mock_response):
        """Test interpolation without target FPS."""
        with patch.object(
            video_ops._api,
            'interpolate_video_api_v2_video_interpolate_post',
            return_value=mock_response
        ):
            response = video_ops.interpolate(
                video_url="https://example.com/video.mp4"
            )
            assert response.success is True


class TestRemix:
    """Tests for remix() method."""

    def test_remix_success(self, video_ops, mock_response):
        """Test successful video remix."""
        with patch.object(
            video_ops._api,
            'remix_video_api_v2_video_remix_post',
            return_value=mock_response
        ):
            response = video_ops.remix(
                video_url="https://example.com/video.mp4",
                remix_prompt="Make it look vintage"
            )
            assert response.success is True

    def test_remix_with_strength(self, video_ops, mock_response):
        """Test remix with strength parameter."""
        with patch.object(
            video_ops._api,
            'remix_video_api_v2_video_remix_post',
            return_value=mock_response
        ):
            response = video_ops.remix(
                video_url="https://example.com/video.mp4",
                remix_prompt="Add sepia tone",
                remix_strength=0.8
            )
            assert response.success is True


class TestGetProjectClips:
    """Tests for get_project_clips() method."""

    def test_get_project_clips_success(self, video_ops, mock_response):
        """Test successful project clips retrieval."""
        mock_response.clips = [
            Mock(name="clip1.mp4", url="https://example.com/clip1.mp4"),
            Mock(name="clip2.mp4", url="https://example.com/clip2.mp4")
        ]
        with patch.object(
            video_ops._api,
            'get_project_clips_api_v2_video_clips_project_id_get',
            return_value=mock_response
        ):
            response = video_ops.get_project_clips(
                project_id="proj_12345"
            )
            assert len(response.clips) == 2


class TestShareProject:
    """Tests for share_project() method."""

    def test_share_project_success(self, video_ops, mock_response):
        """Test successful project sharing."""
        mock_response.share_url = "https://example.com/share/abc123"
        with patch.object(
            video_ops._api,
            'share_project_api_v2_video_share_project_id_post',
            return_value=mock_response
        ):
            response = video_ops.share_project(
                project_id="proj_12345"
            )
            assert response.share_url is not None

    def test_share_project_with_settings(self, video_ops, mock_response):
        """Test sharing with settings."""
        with patch.object(
            video_ops._api,
            'share_project_api_v2_video_share_project_id_post',
            return_value=mock_response
        ):
            response = video_ops.share_project(
                project_id="proj_12345",
                share_settings={"public": True, "allow_download": False}
            )
            assert response.success is True


class TestHandleWebhook:
    """Tests for handle_webhook() method."""

    def test_handle_webhook_success(self, video_ops, mock_response):
        """Test successful webhook handling."""
        with patch.object(
            video_ops._api,
            'handle_webhook_api_v2_video_webhook_post',
            return_value=mock_response
        ):
            response = video_ops.handle_webhook(
                webhook_data={"event": "video.completed", "project_id": "proj_123"}
            )
            assert response.success is True

    def test_handle_webhook_with_metadata(self, video_ops, mock_response):
        """Test webhook handling with metadata."""
        with patch.object(
            video_ops._api,
            'handle_webhook_api_v2_video_webhook_post',
            return_value=mock_response
        ):
            response = video_ops.handle_webhook(
                webhook_data={
                    "event": "video.processing",
                    "project_id": "proj_456",
                    "progress": 75
                }
            )
            assert response.success is True


class TestVideoErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, video_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            video_ops._api,
            'generate_video_api_v2_video_generate_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                video_ops.generate(prompt="Test video")

    def test_validation_error(self, video_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            video_ops._api,
            'describe_video_api_v2_video_describe_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                video_ops.describe(video_url="invalid_url")

    def test_rate_limit_error(self, video_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '300'}
        with patch.object(
            video_ops._api,
            'remix_video_api_v2_video_remix_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                video_ops.remix(
                    video_url="https://example.com/video.mp4",
                    remix_prompt="Test"
                )
            assert exc_info.value.retry_after == 300

    def test_server_error(self, video_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            video_ops._api,
            'extend_video_api_v2_video_extend_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                video_ops.extend(
                    video_url="https://example.com/video.mp4",
                    extension_duration=5
                )
