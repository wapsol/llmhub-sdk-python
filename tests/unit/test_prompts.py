"""Unit tests for PromptOperations."""

import pytest
from unittest.mock import Mock, patch
from llmhub.prompts import PromptOperations
from llmhub.exceptions import (
    ValidationError,
    AuthenticationError,
    RateLimitError,
    NotFoundError,
    ServerError
)
from llmhub_generated.exceptions import ApiException


@pytest.fixture
def prompts_ops(mock_api_key):
    """Create PromptOperations instance for testing."""
    mock_client = Mock()
    return PromptOperations(mock_client, mock_api_key)


@pytest.fixture
def mock_response():
    """Create a mock successful response."""
    response = Mock()
    response.success = True
    response.template_id = "tmpl_12345"
    response.name = "product_description"
    response.template_text = "Write a {tone} description for {product}"
    response.version = 1
    response.usage_count = 0
    return response


class TestCreateTemplate:
    """Tests for create_template() method."""

    def test_create_template_success(self, prompts_ops, mock_response):
        """Test successful template creation."""
        with patch.object(
            prompts_ops._api,
            'create_template_api_v2_prompts_post',
            return_value=mock_response
        ):
            response = prompts_ops.create_template(
                name="product_description",
                template_text="Write a {tone} product description for {product_name}"
            )
            assert response.success is True
            assert response.template_id is not None

    def test_create_template_with_description(self, prompts_ops, mock_response):
        """Test template creation with description."""
        with patch.object(
            prompts_ops._api,
            'create_template_api_v2_prompts_post',
            return_value=mock_response
        ):
            response = prompts_ops.create_template(
                name="email_template",
                template_text="Write an email to {recipient} about {topic}",
                description="Generate professional emails"
            )
            assert response.success is True

    def test_create_template_with_variables(self, prompts_ops, mock_response):
        """Test template creation with variables."""
        with patch.object(
            prompts_ops._api,
            'create_template_api_v2_prompts_post',
            return_value=mock_response
        ):
            response = prompts_ops.create_template(
                name="blog_post",
                template_text="Write a blog post about {topic} in {style} style",
                variables={"topic": "", "style": "informative"},
                tags=["content", "blog"],
                is_public=True
            )
            assert response.success is True


class TestGetTemplate:
    """Tests for get_template() method."""

    def test_get_template_success(self, prompts_ops, mock_response):
        """Test successful template retrieval."""
        with patch.object(
            prompts_ops._api,
            'get_template_api_v2_prompts_template_id_get',
            return_value=mock_response
        ):
            response = prompts_ops.get_template(
                template_id="tmpl_12345"
            )
            assert response.success is True
            assert response.name == "product_description"


class TestListTemplates:
    """Tests for list_templates() method."""

    def test_list_templates_success(self, prompts_ops, mock_response):
        """Test successful templates listing."""
        mock_response.templates = [
            Mock(name="template1", usage_count=10),
            Mock(name="template2", usage_count=5)
        ]
        with patch.object(
            prompts_ops._api,
            'list_templates_api_v2_prompts_get',
            return_value=mock_response
        ):
            response = prompts_ops.list_templates()
            assert response.success is True
            assert len(response.templates) == 2

    def test_list_templates_with_filters(self, prompts_ops, mock_response):
        """Test templates listing with filters."""
        with patch.object(
            prompts_ops._api,
            'list_templates_api_v2_prompts_get',
            return_value=mock_response
        ):
            response = prompts_ops.list_templates(
                tags=["marketing"],
                is_public=True,
                limit=50,
                offset=0
            )
            assert response.success is True

    def test_list_templates_pagination(self, prompts_ops, mock_response):
        """Test templates listing with pagination."""
        with patch.object(
            prompts_ops._api,
            'list_templates_api_v2_prompts_get',
            return_value=mock_response
        ):
            response = prompts_ops.list_templates(
                limit=20,
                offset=40
            )
            assert response.success is True


class TestUpdateTemplate:
    """Tests for update_template() method."""

    def test_update_template_success(self, prompts_ops, mock_response):
        """Test successful template update."""
        mock_response.version = 2
        with patch.object(
            prompts_ops._api,
            'update_template_api_v2_prompts_template_id_put',
            return_value=mock_response
        ):
            response = prompts_ops.update_template(
                template_id="tmpl_12345",
                template_text="Updated template with {new_variable}"
            )
            assert response.success is True
            assert response.version == 2

    def test_update_template_multiple_fields(self, prompts_ops, mock_response):
        """Test template update with multiple fields."""
        with patch.object(
            prompts_ops._api,
            'update_template_api_v2_prompts_template_id_put',
            return_value=mock_response
        ):
            response = prompts_ops.update_template(
                template_id="tmpl_12345",
                name="updated_name",
                template_text="New text with {var}",
                description="Updated description",
                variables={"var": "default"},
                tags=["updated"],
                is_public=False
            )
            assert response.success is True


class TestDeleteTemplate:
    """Tests for delete_template() method."""

    def test_delete_template_success(self, prompts_ops, mock_response):
        """Test successful template deletion."""
        with patch.object(
            prompts_ops._api,
            'delete_template_api_v2_prompts_template_id_delete',
            return_value=mock_response
        ):
            response = prompts_ops.delete_template(
                template_id="tmpl_12345"
            )
            assert response.success is True


class TestListTemplateVersions:
    """Tests for list_template_versions() method."""

    def test_list_template_versions_success(self, prompts_ops, mock_response):
        """Test successful template versions listing."""
        mock_response.versions = [
            Mock(version=1, created_at="2024-01-01", usage_count=50),
            Mock(version=2, created_at="2024-01-15", usage_count=30)
        ]
        with patch.object(
            prompts_ops._api,
            'list_template_versions_api_v2_prompts_template_id_versions_get',
            return_value=mock_response
        ):
            response = prompts_ops.list_template_versions(
                template_id="tmpl_12345"
            )
            assert response.success is True
            assert len(response.versions) == 2


class TestTestTemplate:
    """Tests for test_template() method."""

    def test_test_template_success(self, prompts_ops, mock_response):
        """Test successful template testing."""
        mock_response.rendered_prompt = "Write a professional description for Widget Pro"
        mock_response.content = "Widget Pro is a cutting-edge solution..."
        with patch.object(
            prompts_ops._api,
            'test_template_api_v2_prompts_template_id_test_post',
            return_value=mock_response
        ):
            response = prompts_ops.test_template(
                template_id="tmpl_12345",
                variables={"tone": "professional", "product_name": "Widget Pro"}
            )
            assert response.success is True
            assert response.rendered_prompt is not None

    def test_test_template_with_execution(self, prompts_ops, mock_response):
        """Test template testing with LLM execution."""
        mock_response.content = "Generated content from LLM"
        with patch.object(
            prompts_ops._api,
            'test_template_api_v2_prompts_template_id_test_post',
            return_value=mock_response
        ):
            response = prompts_ops.test_template(
                template_id="tmpl_12345",
                variables={"tone": "enthusiastic", "product_name": "SmartWidget"},
                provider="claude",
                max_tokens=500,
                temperature=0.7
            )
            assert response.success is True
            assert response.content is not None


class TestPromptsErrorHandling:
    """Tests for error handling."""

    def test_authentication_error(self, prompts_ops):
        """Test authentication error conversion."""
        api_exception = ApiException(status=401, reason="Unauthorized")
        with patch.object(
            prompts_ops._api,
            'create_template_api_v2_prompts_post',
            side_effect=api_exception
        ):
            with pytest.raises(AuthenticationError):
                prompts_ops.create_template(
                    name="test",
                    template_text="Test {var}"
                )

    def test_not_found_error(self, prompts_ops):
        """Test not found error conversion."""
        api_exception = ApiException(status=404, reason="Template not found")
        with patch.object(
            prompts_ops._api,
            'get_template_api_v2_prompts_template_id_get',
            side_effect=api_exception
        ):
            with pytest.raises(NotFoundError, match="Template not found"):
                prompts_ops.get_template(template_id="nonexistent")

    def test_validation_error(self, prompts_ops):
        """Test validation error conversion."""
        api_exception = ApiException(status=422, reason="Validation failed")
        with patch.object(
            prompts_ops._api,
            'test_template_api_v2_prompts_template_id_test_post',
            side_effect=api_exception
        ):
            with pytest.raises(ValidationError):
                prompts_ops.test_template(
                    template_id="tmpl_12345",
                    variables={}
                )

    def test_rate_limit_error(self, prompts_ops):
        """Test rate limit error conversion."""
        api_exception = ApiException(status=429, reason="Rate limit exceeded")
        api_exception.headers = {'Retry-After': '120'}
        with patch.object(
            prompts_ops._api,
            'list_templates_api_v2_prompts_get',
            side_effect=api_exception
        ):
            with pytest.raises(RateLimitError) as exc_info:
                prompts_ops.list_templates()
            assert exc_info.value.retry_after == 120

    def test_server_error(self, prompts_ops):
        """Test server error conversion."""
        api_exception = ApiException(status=500, reason="Internal server error")
        with patch.object(
            prompts_ops._api,
            'update_template_api_v2_prompts_template_id_put',
            side_effect=api_exception
        ):
            with pytest.raises(ServerError):
                prompts_ops.update_template(
                    template_id="tmpl_12345",
                    template_text="Updated"
                )
