"""Unit tests for AudioOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.audio import AudioOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def audio_ops(mock_api_key):
    """Create AudioOperations instance for testing."""
    mock_client = Mock()
    return AudioOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.content = "Transcribed text"
    response.audio_url = "https://example.com/audio.mp3"
    response.provider_used = "assemblyai"
    response.cost_usd = 0.001
    return response


class TestTranscribe:
    """Tests for transcribe() method."""

    def test_transcribe_success(self, audio_ops, mock_response):
        """Test successful audio transcription."""
        with patch.object(
            audio_ops._api,
            'transcribe_audio_api_v2_audio_transcribe_post',
            return_value=mock_response
        ):
            response = audio_ops.transcribe(
                audio_url="https://example.com/audio.mp3"
            )
            assert response.success is True
            assert response.content == "Transcribed text"

    def test_transcribe_with_language(self, audio_ops, mock_response):
        """Test transcription with language specification."""
        with patch.object(
            audio_ops._api,
            'transcribe_audio_api_v2_audio_transcribe_post',
            return_value=mock_response
        ):
            response = audio_ops.transcribe(
                audio_url="https://example.com/audio.mp3",
                language="en"
            )
            assert response.success is True

    def test_transcribe_with_provider(self, audio_ops, mock_response):
        """Test transcription with provider override."""
        with patch.object(
            audio_ops._api,
            'transcribe_audio_api_v2_audio_transcribe_post',
            return_value=mock_response
        ):
            response = audio_ops.transcribe(
                audio_url="https://example.com/audio.mp3",
                provider="deepgram",
                model="nova-2"
            )
            assert response.success is True


class TestSynthesize:
    """Tests for synthesize() method."""

    def test_synthesize_success(self, audio_ops, mock_response):
        """Test successful text-to-speech synthesis."""
        with patch.object(
            audio_ops._api,
            'synthesize_audio_api_v2_audio_synthesize_post',
            return_value=mock_response
        ):
            response = audio_ops.synthesize(
                text="Hello, how are you today?"
            )
            assert response.success is True
            assert response.audio_url is not None

    def test_synthesize_with_voice(self, audio_ops, mock_response):
        """Test synthesis with specific voice."""
        with patch.object(
            audio_ops._api,
            'synthesize_audio_api_v2_audio_synthesize_post',
            return_value=mock_response
        ):
            response = audio_ops.synthesize(
                text="Hello world",
                voice="adam",
                language="en-US"
            )
            assert response.success is True

    def test_synthesize_with_provider(self, audio_ops, mock_response):
        """Test synthesis with provider override."""
        with patch.object(
            audio_ops._api,
            'synthesize_audio_api_v2_audio_synthesize_post',
            return_value=mock_response
        ):
            response = audio_ops.synthesize(
                text="Test message",
                provider="elevenlabs",
                model="eleven_multilingual_v2"
            )
            assert response.success is True


class TestEnhance:
    """Tests for enhance() method."""

    def test_enhance_success(self, audio_ops, mock_response):
        """Test successful audio enhancement."""
        with patch.object(
            audio_ops._api,
            'enhance_audio_api_v2_audio_enhance_post',
            return_value=mock_response
        ):
            response = audio_ops.enhance(
                audio_url="https://example.com/noisy.mp3"
            )
            assert response.success is True

    def test_enhance_with_type(self, audio_ops, mock_response):
        """Test enhancement with specific type."""
        with patch.object(
            audio_ops._api,
            'enhance_audio_api_v2_audio_enhance_post',
            return_value=mock_response
        ):
            response = audio_ops.enhance(
                audio_url="https://example.com/audio.mp3",
                enhancement_type="denoise"
            )
            assert response.success is True

    def test_enhance_clarify(self, audio_ops, mock_response):
        """Test enhancement with clarify type."""
        with patch.object(
            audio_ops._api,
            'enhance_audio_api_v2_audio_enhance_post',
            return_value=mock_response
        ):
            response = audio_ops.enhance(
                audio_url="https://example.com/audio.mp3",
                enhancement_type="clarify",
                provider="custom_provider"
            )
            assert response.success is True


class TestSeparate:
    """Tests for separate() method."""

    def test_separate_success(self, audio_ops, mock_response):
        """Test successful audio separation."""
        with patch.object(
            audio_ops._api,
            'separate_audio_api_v2_audio_separate_post',
            return_value=mock_response
        ):
            response = audio_ops.separate(
                audio_url="https://example.com/song.mp3"
            )
            assert response.success is True

    def test_separate_vocals(self, audio_ops, mock_response):
        """Test separation for vocals."""
        with patch.object(
            audio_ops._api,
            'separate_audio_api_v2_audio_separate_post',
            return_value=mock_response
        ):
            response = audio_ops.separate(
                audio_url="https://example.com/song.mp3",
                separation_type="vocals"
            )
            assert response.success is True

    def test_separate_drums(self, audio_ops, mock_response):
        """Test separation for drums."""
        with patch.object(
            audio_ops._api,
            'separate_audio_api_v2_audio_separate_post',
            return_value=mock_response
        ):
            response = audio_ops.separate(
                audio_url="https://example.com/track.mp3",
                separation_type="drums",
                provider="custom_separator"
            )
            assert response.success is True


class TestAudioErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, audio_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            audio_ops._api,
            'transcribe_audio_api_v2_audio_transcribe_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                audio_ops.transcribe(audio_url="https://example.com/audio.mp3")

    def test_validation_error(self, audio_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            audio_ops._api,
            'synthesize_audio_api_v2_audio_synthesize_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                audio_ops.synthesize(text="Test")

    def test_rate_limit_error(self, audio_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '120'}
        with patch.object(
            audio_ops._api,
            'enhance_audio_api_v2_audio_enhance_post',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                audio_ops.enhance(audio_url="https://example.com/audio.mp3")
            assert exc_info.value.retry_after == 120

    def test_server_error(self, audio_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            audio_ops._api,
            'separate_audio_api_v2_audio_separate_post',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                audio_ops.separate(audio_url="https://example.com/audio.mp3")
