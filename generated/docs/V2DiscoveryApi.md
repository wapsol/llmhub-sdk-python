# llmhub_generated.V2DiscoveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_api_v2_discovery_catalog_get**](V2DiscoveryApi.md#get_catalog_api_v2_discovery_catalog_get) | **GET** /api/v2/discovery/catalog | Get Catalog
[**get_models_api_v2_discovery_models_get**](V2DiscoveryApi.md#get_models_api_v2_discovery_models_get) | **GET** /api/v2/discovery/models | Get Models
[**get_providers_api_v2_discovery_providers_get**](V2DiscoveryApi.md#get_providers_api_v2_discovery_providers_get) | **GET** /api/v2/discovery/providers | Get Providers


# **get_catalog_api_v2_discovery_catalog_get**
> Dict[str, object] get_catalog_api_v2_discovery_catalog_get(x_api_key)

Get Catalog

Get complete catalog of available providers and models

Returns all configured providers with their enabled models,
including pricing information for cost estimation.

Requires X-API-Key header for authentication.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.V2DiscoveryApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Catalog
        api_response = api_instance.get_catalog_api_v2_discovery_catalog_get(x_api_key)
        print("The response of V2DiscoveryApi->get_catalog_api_v2_discovery_catalog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DiscoveryApi->get_catalog_api_v2_discovery_catalog_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_models_api_v2_discovery_models_get**
> Dict[str, object] get_models_api_v2_discovery_models_get(x_api_key, provider=provider, model_type=model_type)

Get Models

Get list of available models

Optionally filter by provider and/or model type.
Returns models with pricing information.

Requires X-API-Key header for authentication.

Query Parameters:
    provider: Provider key (e.g., 'claude', 'openai', 'groq')
    model_type: Model type (e.g., 'text', 'image', 'audio')

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.V2DiscoveryApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    provider = 'provider_example' # str | Filter by provider key (optional)
    model_type = 'model_type_example' # str | Filter by model type (text, image, etc.) (optional)

    try:
        # Get Models
        api_response = api_instance.get_models_api_v2_discovery_models_get(x_api_key, provider=provider, model_type=model_type)
        print("The response of V2DiscoveryApi->get_models_api_v2_discovery_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DiscoveryApi->get_models_api_v2_discovery_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **provider** | **str**| Filter by provider key | [optional] 
 **model_type** | **str**| Filter by model type (text, image, etc.) | [optional] 

### Return type

**Dict[str, object]**

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

# **get_providers_api_v2_discovery_providers_get**
> Dict[str, object] get_providers_api_v2_discovery_providers_get(x_api_key)

Get Providers

Get list of available providers

Returns simplified list of configured providers without detailed model information.
Use /catalog for full details including models.

Requires X-API-Key header for authentication.

### Example


```python
import llmhub_generated
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
    api_instance = llmhub_generated.V2DiscoveryApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Providers
        api_response = api_instance.get_providers_api_v2_discovery_providers_get(x_api_key)
        print("The response of V2DiscoveryApi->get_providers_api_v2_discovery_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DiscoveryApi->get_providers_api_v2_discovery_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

**Dict[str, object]**

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

