"""Custom exceptions for LLMHub SDK."""


class LLMHubError(Exception):
    """Base exception for all LLMHub errors."""
    pass


class AuthenticationError(LLMHubError):
    """Invalid API key or authentication failure."""
    pass


class RateLimitError(LLMHubError):
    """Rate limit exceeded."""

    def __init__(self, message: str, retry_after: int = None):
        """
        Initialize RateLimitError.

        Args:
            message: Error message
            retry_after: Seconds to wait before retrying (optional)
        """
        super().__init__(message)
        self.retry_after = retry_after


class ProviderError(LLMHubError):
    """Provider-specific error."""
    pass


class ValidationError(LLMHubError):
    """Request validation error."""
    pass


class NotFoundError(LLMHubError):
    """Resource not found error."""
    pass


class ServerError(LLMHubError):
    """Server-side error (5xx)."""
    pass
