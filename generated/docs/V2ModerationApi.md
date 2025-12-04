# llmhub_generated.V2ModerationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_toxicity_api_v2_moderation_analyze_toxicity_post**](V2ModerationApi.md#analyze_toxicity_api_v2_moderation_analyze_toxicity_post) | **POST** /api/v2/moderation/analyze-toxicity | Analyze Toxicity
[**detect_content_types_api_v2_moderation_detect_post**](V2ModerationApi.md#detect_content_types_api_v2_moderation_detect_post) | **POST** /api/v2/moderation/detect | Detect Content Types
[**moderate_content_api_v2_moderation_moderate_post**](V2ModerationApi.md#moderate_content_api_v2_moderation_moderate_post) | **POST** /api/v2/moderation/moderate | Moderate Content


# **analyze_toxicity_api_v2_moderation_analyze_toxicity_post**
> V2PerspectiveAnalyzeResponse analyze_toxicity_api_v2_moderation_analyze_toxicity_post(x_api_key, v2_perspective_analyze_request)

Analyze Toxicity

Analyze text for toxicity using Google Perspective API

Fast, accurate ML-based toxicity detection with ~100ms response time.
Much faster and more accurate than LLM-based moderation.

Attributes:
- TOXICITY: Overall toxicity likelihood
- SEVERE_TOXICITY: Very hateful, aggressive, disrespectful comments
- IDENTITY_ATTACK: Negative or hateful comments about identity/ethnicity
- INSULT: Insulting, inflammatory, or negative comments
- PROFANITY: Swear words, curse words, or other obscene language
- THREAT: Describes an intention to inflict pain, injury, or violence

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_perspective_analyze_request import V2PerspectiveAnalyzeRequest
from llmhub_generated.models.v2_perspective_analyze_response import V2PerspectiveAnalyzeResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2ModerationApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_perspective_analyze_request = llmhub_generated.V2PerspectiveAnalyzeRequest() # V2PerspectiveAnalyzeRequest | 

    try:
        # Analyze Toxicity
        api_response = api_instance.analyze_toxicity_api_v2_moderation_analyze_toxicity_post(x_api_key, v2_perspective_analyze_request)
        print("The response of V2ModerationApi->analyze_toxicity_api_v2_moderation_analyze_toxicity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ModerationApi->analyze_toxicity_api_v2_moderation_analyze_toxicity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_perspective_analyze_request** | [**V2PerspectiveAnalyzeRequest**](V2PerspectiveAnalyzeRequest.md)|  | 

### Return type

[**V2PerspectiveAnalyzeResponse**](V2PerspectiveAnalyzeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_content_types_api_v2_moderation_detect_post**
> V2BaseResponse detect_content_types_api_v2_moderation_detect_post(x_api_key, v2_detection_request)

Detect Content Types

Detect specific content types (PII, hate speech, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_detection_request import V2DetectionRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2ModerationApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_detection_request = llmhub_generated.V2DetectionRequest() # V2DetectionRequest | 

    try:
        # Detect Content Types
        api_response = api_instance.detect_content_types_api_v2_moderation_detect_post(x_api_key, v2_detection_request)
        print("The response of V2ModerationApi->detect_content_types_api_v2_moderation_detect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ModerationApi->detect_content_types_api_v2_moderation_detect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_detection_request** | [**V2DetectionRequest**](V2DetectionRequest.md)|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **moderate_content_api_v2_moderation_moderate_post**
> V2BaseResponse moderate_content_api_v2_moderation_moderate_post(x_api_key, v2_moderation_request)

Moderate Content

Check content for safety/policy violations

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_moderation_request import V2ModerationRequest
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2ModerationApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_moderation_request = llmhub_generated.V2ModerationRequest() # V2ModerationRequest | 

    try:
        # Moderate Content
        api_response = api_instance.moderate_content_api_v2_moderation_moderate_post(x_api_key, v2_moderation_request)
        print("The response of V2ModerationApi->moderate_content_api_v2_moderation_moderate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ModerationApi->moderate_content_api_v2_moderation_moderate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_moderation_request** | [**V2ModerationRequest**](V2ModerationRequest.md)|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

