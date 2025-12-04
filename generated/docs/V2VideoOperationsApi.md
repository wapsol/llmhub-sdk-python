# llmhub_generated.V2VideoOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_video_clips_api_v2_video_clip_post**](V2VideoOperationsApi.md#create_video_clips_api_v2_video_clip_post) | **POST** /api/v2/video/clip | Create Video Clips
[**describe_video_api_v2_video_describe_post**](V2VideoOperationsApi.md#describe_video_api_v2_video_describe_post) | **POST** /api/v2/video/describe | Describe Video
[**extend_video_api_v2_video_extend_post**](V2VideoOperationsApi.md#extend_video_api_v2_video_extend_post) | **POST** /api/v2/video/extend | Extend Video
[**generate_video_api_v2_video_generate_post**](V2VideoOperationsApi.md#generate_video_api_v2_video_generate_post) | **POST** /api/v2/video/generate | Generate Video
[**get_project_clips_api_v2_video_clips_project_id_get**](V2VideoOperationsApi.md#get_project_clips_api_v2_video_clips_project_id_get) | **GET** /api/v2/video/clips/{project_id} | Get Project Clips
[**handle_webhook_api_v2_video_webhook_post**](V2VideoOperationsApi.md#handle_webhook_api_v2_video_webhook_post) | **POST** /api/v2/video/webhook | Handle Webhook
[**interpolate_video_api_v2_video_interpolate_post**](V2VideoOperationsApi.md#interpolate_video_api_v2_video_interpolate_post) | **POST** /api/v2/video/interpolate | Interpolate Video
[**remix_video_api_v2_video_remix_post**](V2VideoOperationsApi.md#remix_video_api_v2_video_remix_post) | **POST** /api/v2/video/remix | Remix Video
[**share_project_api_v2_video_share_project_id_post**](V2VideoOperationsApi.md#share_project_api_v2_video_share_project_id_post) | **POST** /api/v2/video/share/{project_id} | Share Project


# **create_video_clips_api_v2_video_clip_post**
> CreateClipResponse create_video_clips_api_v2_video_clip_post(x_api_key, create_clip_request)

Create Video Clips

Create viral short clips from a long-form video

This endpoint starts an OpusClip project that:
- Analyzes your video for viral-worthy moments
- Creates multiple short-form clips (30-90 seconds)
- Adds auto-captions and reframes for mobile
- Applies optional brand templates

**Processing is async**: Use the returned project_id to check status and retrieve clips.

**Cost**: 1 credit per minute of video (e.g., 10-minute video = 10 credits)

**Supported video sources**:
- YouTube URLs
- Direct video URLs (MP4, MOV, WEBM)

**Example Request**:
```json
{
    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "model": "clip-basic",
    "clip_durations": ["30-60", "60-90"],
    "genre": "educational",
    "topic_keywords": ["AI", "machine learning"]
}
```

### Example


```python
import llmhub_generated
from llmhub_generated.models.create_clip_request import CreateClipRequest
from llmhub_generated.models.create_clip_response import CreateClipResponse
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    create_clip_request = llmhub_generated.CreateClipRequest() # CreateClipRequest | 

    try:
        # Create Video Clips
        api_response = api_instance.create_video_clips_api_v2_video_clip_post(x_api_key, create_clip_request)
        print("The response of V2VideoOperationsApi->create_video_clips_api_v2_video_clip_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->create_video_clips_api_v2_video_clip_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **create_clip_request** | [**CreateClipRequest**](CreateClipRequest.md)|  | 

### Return type

[**CreateClipResponse**](CreateClipResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_video_api_v2_video_describe_post**
> V2BaseResponse describe_video_api_v2_video_describe_post(x_api_key, v2_video_describe_request)

Describe Video

Generate description of video contents using vision models

Status: Placeholder - requires GPT-4 Vision or Gemini Vision integration

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_video_describe_request import V2VideoDescribeRequest
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_video_describe_request = llmhub_generated.V2VideoDescribeRequest() # V2VideoDescribeRequest | 

    try:
        # Describe Video
        api_response = api_instance.describe_video_api_v2_video_describe_post(x_api_key, v2_video_describe_request)
        print("The response of V2VideoOperationsApi->describe_video_api_v2_video_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->describe_video_api_v2_video_describe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_video_describe_request** | [**V2VideoDescribeRequest**](V2VideoDescribeRequest.md)|  | 

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

# **extend_video_api_v2_video_extend_post**
> V2BaseResponse extend_video_api_v2_video_extend_post(x_api_key, v2_video_extend_request)

Extend Video

Extend video duration by generating additional frames

Status: Placeholder - requires RunwayML extend endpoint

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_video_extend_request import V2VideoExtendRequest
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_video_extend_request = llmhub_generated.V2VideoExtendRequest() # V2VideoExtendRequest | 

    try:
        # Extend Video
        api_response = api_instance.extend_video_api_v2_video_extend_post(x_api_key, v2_video_extend_request)
        print("The response of V2VideoOperationsApi->extend_video_api_v2_video_extend_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->extend_video_api_v2_video_extend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_video_extend_request** | [**V2VideoExtendRequest**](V2VideoExtendRequest.md)|  | 

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

# **generate_video_api_v2_video_generate_post**
> V2BaseResponse generate_video_api_v2_video_generate_post(x_api_key, v2_video_generate_request)

Generate Video

Generate video from text prompt and image

Supported providers:
- Pika Labs (via Fal.ai): v2.2 models, 720p ($0.20) or 1080p ($0.45) per 5s video
- RunwayML: Gen-4 models, credit-based pricing

Both require 'prompt_image' URL for image-to-video generation.

Note: Pure text-to-video may require first generating an image,
then converting to video.

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_video_generate_request import V2VideoGenerateRequest
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_video_generate_request = llmhub_generated.V2VideoGenerateRequest() # V2VideoGenerateRequest | 

    try:
        # Generate Video
        api_response = api_instance.generate_video_api_v2_video_generate_post(x_api_key, v2_video_generate_request)
        print("The response of V2VideoOperationsApi->generate_video_api_v2_video_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->generate_video_api_v2_video_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_video_generate_request** | [**V2VideoGenerateRequest**](V2VideoGenerateRequest.md)|  | 

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

# **get_project_clips_api_v2_video_clips_project_id_get**
> GetClipsResponse get_project_clips_api_v2_video_clips_project_id_get(project_id, x_api_key)

Get Project Clips

Get clips for a project

Returns all generated clips for the specified project.
Projects may take several minutes to process depending on video length.

**Status values**:
- `processing`: Still generating clips
- `completed`: All clips ready
- `failed`: Processing failed

**Example Response**:
```json
{
    "project_id": "abc123",
    "status": "completed",
    "total_clips": 5,
    "clips": [
        {
            "clip_id": "clip1",
            "title": "Best moment from your video",
            "duration_seconds": 45,
            "virality_score": 8.5,
            "video_url": "https://...",
            "thumbnail_url": "https://..."
        }
    ]
}
```

### Example


```python
import llmhub_generated
from llmhub_generated.models.get_clips_response import GetClipsResponse
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Project Clips
        api_response = api_instance.get_project_clips_api_v2_video_clips_project_id_get(project_id, x_api_key)
        print("The response of V2VideoOperationsApi->get_project_clips_api_v2_video_clips_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->get_project_clips_api_v2_video_clips_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**|  | 

### Return type

[**GetClipsResponse**](GetClipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_webhook_api_v2_video_webhook_post**
> object handle_webhook_api_v2_video_webhook_post(webhook_payload)

Handle Webhook

Webhook endpoint for OpusClip notifications

OpusClip sends updates when:
- Processing completes
- Processing fails
- New clips become available

This endpoint logs the event and can trigger custom actions.

**Webhook Security**: In production, verify webhook signatures.

**Example Payload**:
```json
{
    "project_id": "abc123",
    "status": "completed",
    "event": "clips_ready",
    "timestamp": "2024-01-15T10:30:00Z",
    "data": {
        "total_clips": 5,
        "processing_time_seconds": 180
    }
}
```

### Example


```python
import llmhub_generated
from llmhub_generated.models.webhook_payload import WebhookPayload
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    webhook_payload = llmhub_generated.WebhookPayload() # WebhookPayload | 

    try:
        # Handle Webhook
        api_response = api_instance.handle_webhook_api_v2_video_webhook_post(webhook_payload)
        print("The response of V2VideoOperationsApi->handle_webhook_api_v2_video_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->handle_webhook_api_v2_video_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_payload** | [**WebhookPayload**](WebhookPayload.md)|  | 

### Return type

**object**

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

# **interpolate_video_api_v2_video_interpolate_post**
> V2BaseResponse interpolate_video_api_v2_video_interpolate_post(x_api_key, v2_video_interpolate_request)

Interpolate Video

Create smooth transitions between video frames (frame interpolation)

Status: Placeholder - requires specialized video processing

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_video_interpolate_request import V2VideoInterpolateRequest
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_video_interpolate_request = llmhub_generated.V2VideoInterpolateRequest() # V2VideoInterpolateRequest | 

    try:
        # Interpolate Video
        api_response = api_instance.interpolate_video_api_v2_video_interpolate_post(x_api_key, v2_video_interpolate_request)
        print("The response of V2VideoOperationsApi->interpolate_video_api_v2_video_interpolate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->interpolate_video_api_v2_video_interpolate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_video_interpolate_request** | [**V2VideoInterpolateRequest**](V2VideoInterpolateRequest.md)|  | 

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

# **remix_video_api_v2_video_remix_post**
> V2BaseResponse remix_video_api_v2_video_remix_post(x_api_key, v2_video_remix_request)

Remix Video

Remix/edit existing video with AI

Status: Placeholder - requires RunwayML video-to-video endpoint

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_video_remix_request import V2VideoRemixRequest
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_video_remix_request = llmhub_generated.V2VideoRemixRequest() # V2VideoRemixRequest | 

    try:
        # Remix Video
        api_response = api_instance.remix_video_api_v2_video_remix_post(x_api_key, v2_video_remix_request)
        print("The response of V2VideoOperationsApi->remix_video_api_v2_video_remix_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->remix_video_api_v2_video_remix_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_video_remix_request** | [**V2VideoRemixRequest**](V2VideoRemixRequest.md)|  | 

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

# **share_project_api_v2_video_share_project_id_post**
> ShareProjectResponse share_project_api_v2_video_share_project_id_post(project_id, x_api_key, share_project_request)

Share Project

Update project visibility for sharing

Make a project public or private. Public projects can be shared via URL.

**Visibility options**:
- `public`: Anyone with the link can view
- `private`: Only you can access

**Example Request**:
```json
{
    "visibility": "public"
}
```

### Example


```python
import llmhub_generated
from llmhub_generated.models.share_project_request import ShareProjectRequest
from llmhub_generated.models.share_project_response import ShareProjectResponse
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
    api_instance = llmhub_generated.V2VideoOperationsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    share_project_request = llmhub_generated.ShareProjectRequest() # ShareProjectRequest | 

    try:
        # Share Project
        api_response = api_instance.share_project_api_v2_video_share_project_id_post(project_id, x_api_key, share_project_request)
        print("The response of V2VideoOperationsApi->share_project_api_v2_video_share_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2VideoOperationsApi->share_project_api_v2_video_share_project_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **share_project_request** | [**ShareProjectRequest**](ShareProjectRequest.md)|  | 

### Return type

[**ShareProjectResponse**](ShareProjectResponse.md)

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

