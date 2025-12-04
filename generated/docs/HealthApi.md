# llmhub_generated.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_health_get**](HealthApi.md#health_check_health_get) | **GET** /health/ | Health Check
[**liveness_probe_health_live_get**](HealthApi.md#liveness_probe_health_live_get) | **GET** /health/live | Liveness Probe
[**readiness_probe_health_ready_get**](HealthApi.md#readiness_probe_health_ready_get) | **GET** /health/ready | Readiness Probe


# **health_check_health_get**
> HealthCheckResponse health_check_health_get()

Health Check

Basic health check endpoint
Returns 200 OK if service is running

### Example


```python
import llmhub_generated
from llmhub_generated.models.health_check_response import HealthCheckResponse
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
    api_instance = llmhub_generated.HealthApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_health_get()
        print("The response of HealthApi->health_check_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_check_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

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

# **liveness_probe_health_live_get**
> DetailedHealthCheckResponse liveness_probe_health_live_get()

Liveness Probe

Kubernetes liveness probe
Checks if the service is alive and database is accessible

### Example


```python
import llmhub_generated
from llmhub_generated.models.detailed_health_check_response import DetailedHealthCheckResponse
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
    api_instance = llmhub_generated.HealthApi(api_client)

    try:
        # Liveness Probe
        api_response = api_instance.liveness_probe_health_live_get()
        print("The response of HealthApi->liveness_probe_health_live_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->liveness_probe_health_live_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DetailedHealthCheckResponse**](DetailedHealthCheckResponse.md)

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

# **readiness_probe_health_ready_get**
> DetailedHealthCheckResponse readiness_probe_health_ready_get()

Readiness Probe

Kubernetes readiness probe
Checks if service is ready to accept traffic

### Example


```python
import llmhub_generated
from llmhub_generated.models.detailed_health_check_response import DetailedHealthCheckResponse
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
    api_instance = llmhub_generated.HealthApi(api_client)

    try:
        # Readiness Probe
        api_response = api_instance.readiness_probe_health_ready_get()
        print("The response of HealthApi->readiness_probe_health_ready_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->readiness_probe_health_ready_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DetailedHealthCheckResponse**](DetailedHealthCheckResponse.md)

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

