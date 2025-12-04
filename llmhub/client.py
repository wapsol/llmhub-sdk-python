"""Main LLMHub client."""

import sys
from typing import Optional

# Add generated package to path for imports
sys.path.insert(0, 'generated')

from llmhub_generated import Configuration, ApiClient
from llmhub.exceptions import LLMHubError


class LLMHub:
    """
    Main LLMHub client for interacting with the LLMHub API.

    This client provides a unified interface to access 18+ AI providers
    across 11 modalities including text generation, embeddings, audio,
    video, image generation, and more.

    Example:
        >>> client = LLMHub(api_key="your-api-key")
        >>> response = client.text.generate(prompt="Hello world")
        >>> print(response.content)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "http://localhost:8000"
    ):
        """
        Initialize LLMHub client.

        Args:
            api_key: Your LLMHub API key (required)
            base_url: Base URL for the LLMHub API (optional)

        Raises:
            ValueError: If api_key is empty or invalid
        """
        if not api_key or not isinstance(api_key, str) or len(api_key.strip()) == 0:
            raise ValueError("API key is required and cannot be empty")

        self.api_key = api_key
        self.base_url = base_url

        # Configure the generated client
        self.config = Configuration()
        self.config.api_key = {'X-API-Key': api_key}
        self.config.host = base_url

        # Initialize API client
        self._client = ApiClient(self.config)

        # Initialize operation modules (will be implemented in wrapper classes)
        # self.text = TextOperations(self._client)
        # self.document = DocumentOperations(self._client)
        # self.embeddings = EmbeddingsOperations(self._client)
        # self.audio = AudioOperations(self._client)
        # self.video = VideoOperations(self._client)
        # self.image = ImageOperations(self._client)
        # self.moderation = ModerationOperations(self._client)
        # self.enrichment = EnrichmentOperations(self._client)
        # self.discovery = DiscoveryOperations(self._client)
        # self.prompts = PromptOperations(self._client)
        # self.data = DataOperations(self._client)

    def __repr__(self) -> str:
        """Return string representation of the client."""
        return f"LLMHub(base_url='{self.base_url}')"
