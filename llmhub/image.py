"""Image operations wrapper for LLMHub SDK."""

import sys
from typing import Optional

sys.path.insert(0, 'generated')

from llmhub_generated.api.v2_image_operations_api import V2ImageOperationsApi
from llmhub_generated.models.v2_image_generate_request import V2ImageGenerateRequest
from llmhub_generated.models.v2_image_edit_request import V2ImageEditRequest
from llmhub_generated.models.v2_image_analyze_request import V2ImageAnalyzeRequest
from llmhub_generated.models.v2_image_describe_request import V2ImageDescribeRequest
from llmhub_generated.models.v2_image_upscale_request import V2ImageUpscaleRequest
from llmhub_generated.models.v2_image_vary_request import V2ImageVaryRequest
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.exceptions import ApiException

from llmhub.exceptions import (
    LLMHubError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    ServerError
)


class ImageOperations:
    """
    Image operations for LLMHub API.

    Provides methods for image generation, editing, analysis,
    description, upscaling, and variation.
    """

    def __init__(self, api_client, api_key: str):
        """
        Initialize ImageOperations.

        Args:
            api_client: The API client instance from llmhub_generated
            api_key: The API key for authentication
        """
        self._api = V2ImageOperationsApi(api_client)
        self._api_key = api_key

    def generate(
        self,
        prompt: str,
        size: Optional[str] = None,
        style: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Generate an image from a text prompt.

        Args:
            prompt: Text description of the image to generate
            size: Image size (e.g., '1024x1024', '512x512')
            style: Image style (e.g., 'realistic', 'artistic', 'cartoon')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with generated image URL

        Example:
            >>> response = client.image.generate(
            ...     prompt="A serene mountain landscape at sunset",
            ...     size="1024x1024",
            ...     style="realistic"
            ... )
            >>> print(response.image_url)
        """
        try:
            request = V2ImageGenerateRequest(
                prompt=prompt,
                size=size,
                style=style,
                provider=provider,
                model=model
            )
            return self._api.generate_image_api_v2_image_generate_post(
                x_api_key=self._api_key,
                v2_image_generate_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def edit(
        self,
        image_url: str,
        prompt: str,
        mask_url: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Edit an existing image based on a prompt.

        Args:
            image_url: URL to the image to edit
            prompt: Description of edits to make
            mask_url: Optional mask URL for inpainting
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with edited image URL

        Example:
            >>> response = client.image.edit(
            ...     image_url="https://example.com/photo.jpg",
            ...     prompt="Add sunglasses to the person"
            ... )
        """
        try:
            request = V2ImageEditRequest(
                image_url=image_url,
                prompt=prompt,
                mask_url=mask_url,
                provider=provider,
                model=model
            )
            return self._api.edit_image_api_v2_image_edit_post(
                x_api_key=self._api_key,
                v2_image_edit_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def analyze(
        self,
        image_url: str,
        analysis_type: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Analyze an image for specific attributes.

        Args:
            image_url: URL to the image to analyze
            analysis_type: Type of analysis (e.g., 'objects', 'faces', 'sentiment')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with analysis results

        Example:
            >>> response = client.image.analyze(
            ...     image_url="https://example.com/photo.jpg",
            ...     analysis_type="objects"
            ... )
        """
        try:
            request = V2ImageAnalyzeRequest(
                image_url=image_url,
                analysis_type=analysis_type,
                provider=provider,
                model=model
            )
            return self._api.analyze_image_api_v2_image_analyze_post(
                x_api_key=self._api_key,
                v2_image_analyze_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def describe(
        self,
        image_url: str,
        detail_level: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Generate a text description of an image.

        Args:
            image_url: URL to the image to describe
            detail_level: Level of detail ('brief', 'detailed', 'comprehensive')
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with image description

        Example:
            >>> response = client.image.describe(
            ...     image_url="https://example.com/photo.jpg",
            ...     detail_level="detailed"
            ... )
            >>> print(response.content)
        """
        try:
            request = V2ImageDescribeRequest(
                image_url=image_url,
                detail_level=detail_level,
                provider=provider,
                model=model
            )
            return self._api.describe_image_api_v2_image_describe_post(
                x_api_key=self._api_key,
                v2_image_describe_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def upscale(
        self,
        image_url: str,
        scale_factor: Optional[int] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Upscale an image to higher resolution.

        Args:
            image_url: URL to the image to upscale
            scale_factor: Upscaling factor (e.g., 2, 4)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with upscaled image URL

        Example:
            >>> response = client.image.upscale(
            ...     image_url="https://example.com/low_res.jpg",
            ...     scale_factor=4
            ... )
        """
        try:
            request = V2ImageUpscaleRequest(
                image_url=image_url,
                scale_factor=scale_factor,
                provider=provider,
                model=model
            )
            return self._api.upscale_image_api_v2_image_upscale_post(
                x_api_key=self._api_key,
                v2_image_upscale_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def vary(
        self,
        image_url: str,
        variation_strength: Optional[float] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None
    ) -> V2BaseResponse:
        """
        Create variations of an image.

        Args:
            image_url: URL to the base image
            variation_strength: Strength of variation (0.0 to 1.0)
            provider: Optional provider override
            model: Optional model override

        Returns:
            V2BaseResponse with varied image URL

        Example:
            >>> response = client.image.vary(
            ...     image_url="https://example.com/base.jpg",
            ...     variation_strength=0.7
            ... )
        """
        try:
            request = V2ImageVaryRequest(
                image_url=image_url,
                variation_strength=variation_strength,
                provider=provider,
                model=model
            )
            return self._api.vary_image_api_v2_image_vary_post(
                x_api_key=self._api_key,
                v2_image_vary_request=request
            )
        except ApiException as e:
            raise self._convert_exception(e)

    def _convert_exception(self, e: ApiException) -> Exception:
        """Convert API exceptions to SDK exceptions."""
        status = getattr(e, 'status', 500)
        message = str(e)

        if status == 401:
            return AuthenticationError("Invalid API key or authentication failed")
        elif status == 403:
            return AuthenticationError("Access forbidden - check API key permissions")
        elif status == 422:
            return ValidationError(f"Validation error: {message}")
        elif status == 429:
            retry_after = None
            if hasattr(e, 'headers') and 'Retry-After' in e.headers:
                try:
                    retry_after = int(e.headers['Retry-After'])
                except (ValueError, TypeError):
                    pass
            return RateLimitError("Rate limit exceeded", retry_after=retry_after)
        elif 500 <= status < 600:
            return ServerError(f"Server error: {message}")
        else:
            return LLMHubError(f"API error: {message}")
