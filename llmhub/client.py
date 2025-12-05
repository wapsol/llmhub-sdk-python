"""Main LLMHub client."""

import sys
from typing import Optional

# Add generated package to path for imports
sys.path.insert(0, 'generated')

from llmhub_generated import Configuration, ApiClient
from llmhub.exceptions import LLMHubError
from llmhub.text import TextOperations
from llmhub.embeddings import EmbeddingsOperations
from llmhub.document import DocumentOperations
from llmhub.audio import AudioOperations
from llmhub.video import VideoOperations
from llmhub.image import ImageOperations
from llmhub.moderation import ModerationOperations
from llmhub.enrichment import EnrichmentOperations
from llmhub.discovery import DiscoveryOperations
from llmhub.prompts import PromptOperations
from llmhub.data import DataOperations


class LLMHub:
    """
    Main LLMHub client for interacting with the LLMHub API.

    This client provides a unified interface to access 18+ AI providers
    across 11 modalities including text generation, embeddings, audio,
    video, image generation, and more.

    Available Operations:
        - text: Text generation, translation, summarization, etc.
        - embeddings: Generate vector embeddings for text
        - document: Parse, extract, and classify documents
        - audio: Transcribe, synthesize, enhance audio
        - video: Generate, describe, edit video
        - image: Generate, edit, analyze images
        - moderation: Content moderation and toxicity analysis
        - enrichment: B2B data enrichment (Hunter.io)
        - discovery: Discover available providers and models
        - prompts: Manage reusable prompt templates
        - data: Data operations (embed, rerank)

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
        self.config.host = base_url

        # Initialize API client
        self._client = ApiClient(self.config)

        # Initialize operation modules (pass API key for authentication)
        self.text = TextOperations(self._client, api_key)
        self.embeddings = EmbeddingsOperations(self._client, api_key)
        self.document = DocumentOperations(self._client, api_key)
        self.audio = AudioOperations(self._client, api_key)
        self.video = VideoOperations(self._client, api_key)
        self.image = ImageOperations(self._client, api_key)
        self.moderation = ModerationOperations(self._client, api_key)
        self.enrichment = EnrichmentOperations(self._client, api_key)
        self.discovery = DiscoveryOperations(self._client, api_key)
        self.prompts = PromptOperations(self._client, api_key)
        self.data = DataOperations(self._client, api_key)

    def __repr__(self) -> str:
        """Return string representation of the client."""
        return f"LLMHub(base_url='{self.base_url}')"
