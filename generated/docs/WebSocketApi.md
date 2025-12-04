# llmhub_generated.WebSocketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**websocket_status_api_ws_status_get**](WebSocketApi.md#websocket_status_api_ws_status_get) | **GET** /api/ws/status | Websocket Status


# **websocket_status_api_ws_status_get**
> object websocket_status_api_ws_status_get()

Websocket Status

Get WebSocket server status

Returns:
    Connection count and room information

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
    api_instance = llmhub_generated.WebSocketApi(api_client)

    try:
        # Websocket Status
        api_response = api_instance.websocket_status_api_ws_status_get()
        print("The response of WebSocketApi->websocket_status_api_ws_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSocketApi->websocket_status_api_ws_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

