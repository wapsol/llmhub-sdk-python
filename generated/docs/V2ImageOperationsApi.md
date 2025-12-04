# llmhub_generated.V2ImageOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_image_api_v2_image_analyze_post**](V2ImageOperationsApi.md#analyze_image_api_v2_image_analyze_post) | **POST** /api/v2/image/analyze | Analyze Image
[**describe_image_api_v2_image_describe_post**](V2ImageOperationsApi.md#describe_image_api_v2_image_describe_post) | **POST** /api/v2/image/describe | Describe Image
[**edit_image_api_v2_image_edit_post**](V2ImageOperationsApi.md#edit_image_api_v2_image_edit_post) | **POST** /api/v2/image/edit | Edit Image
[**generate_image_api_v2_image_generate_post**](V2ImageOperationsApi.md#generate_image_api_v2_image_generate_post) | **POST** /api/v2/image/generate | Generate Image
[**upscale_image_api_v2_image_upscale_post**](V2ImageOperationsApi.md#upscale_image_api_v2_image_upscale_post) | **POST** /api/v2/image/upscale | Upscale Image
[**vary_image_api_v2_image_vary_post**](V2ImageOperationsApi.md#vary_image_api_v2_image_vary_post) | **POST** /api/v2/image/vary | Vary Image


# **analyze_image_api_v2_image_analyze_post**
> V2BaseResponse analyze_image_api_v2_image_analyze_post(x_api_key)

Analyze Image

Analyze images (OCR, object detection, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Analyze Image
        api_response = api_instance.analyze_image_api_v2_image_analyze_post(x_api_key)
        print("The response of V2ImageOperationsApi->analyze_image_api_v2_image_analyze_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->analyze_image_api_v2_image_analyze_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

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

# **describe_image_api_v2_image_describe_post**
> V2BaseResponse describe_image_api_v2_image_describe_post(x_api_key)

Describe Image

Generate description of image contents

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Describe Image
        api_response = api_instance.describe_image_api_v2_image_describe_post(x_api_key)
        print("The response of V2ImageOperationsApi->describe_image_api_v2_image_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->describe_image_api_v2_image_describe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

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

# **edit_image_api_v2_image_edit_post**
> object edit_image_api_v2_image_edit_post(x_api_key, image_edit_request)

Edit Image

Edit images using DALL-E 2 (DALL-E 3 doesn't support edits)

Requires X-API-Key header for authentication.

### Example


```python
import llmhub_generated
from llmhub_generated.models.image_edit_request import ImageEditRequest
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    image_edit_request = llmhub_generated.ImageEditRequest() # ImageEditRequest | 

    try:
        # Edit Image
        api_response = api_instance.edit_image_api_v2_image_edit_post(x_api_key, image_edit_request)
        print("The response of V2ImageOperationsApi->edit_image_api_v2_image_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->edit_image_api_v2_image_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **image_edit_request** | [**ImageEditRequest**](ImageEditRequest.md)|  | 

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

# **generate_image_api_v2_image_generate_post**
> ImageGenerationResponse generate_image_api_v2_image_generate_post(x_api_key, image_generation_request)

Generate Image

Generate images using DALL-E 3

Requires X-API-Key header for authentication.
Tracks usage and costs per API client.
Uploads generated images to MinIO for permanent storage.

Returns:
    Generated image URLs with cost tracking

### Example


```python
import llmhub_generated
from llmhub_generated.models.image_generation_request import ImageGenerationRequest
from llmhub_generated.models.image_generation_response import ImageGenerationResponse
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    image_generation_request = llmhub_generated.ImageGenerationRequest() # ImageGenerationRequest | 

    try:
        # Generate Image
        api_response = api_instance.generate_image_api_v2_image_generate_post(x_api_key, image_generation_request)
        print("The response of V2ImageOperationsApi->generate_image_api_v2_image_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->generate_image_api_v2_image_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **image_generation_request** | [**ImageGenerationRequest**](ImageGenerationRequest.md)|  | 

### Return type

[**ImageGenerationResponse**](ImageGenerationResponse.md)

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

# **upscale_image_api_v2_image_upscale_post**
> V2BaseResponse upscale_image_api_v2_image_upscale_post(x_api_key)

Upscale Image

Upscale/enhance image quality

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Upscale Image
        api_response = api_instance.upscale_image_api_v2_image_upscale_post(x_api_key)
        print("The response of V2ImageOperationsApi->upscale_image_api_v2_image_upscale_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->upscale_image_api_v2_image_upscale_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

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

# **vary_image_api_v2_image_vary_post**
> V2BaseResponse vary_image_api_v2_image_vary_post(x_api_key)

Vary Image

Create variations of images

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
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
    api_instance = llmhub_generated.V2ImageOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Vary Image
        api_response = api_instance.vary_image_api_v2_image_vary_post(x_api_key)
        print("The response of V2ImageOperationsApi->vary_image_api_v2_image_vary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2ImageOperationsApi->vary_image_api_v2_image_vary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

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

