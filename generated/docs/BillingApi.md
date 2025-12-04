# llmhub_generated.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_month_usage_api_v1_llm_billing_usage_current_month_get**](BillingApi.md#get_current_month_usage_api_v1_llm_billing_usage_current_month_get) | **GET** /api/v1/llm/billing/usage/current-month | Get Current Month Usage
[**get_generation_logs_api_v1_llm_billing_logs_get**](BillingApi.md#get_generation_logs_api_v1_llm_billing_logs_get) | **GET** /api/v1/llm/billing/logs | Get Generation Logs
[**get_log_details_api_v1_llm_billing_logs_log_id_get**](BillingApi.md#get_log_details_api_v1_llm_billing_logs_log_id_get) | **GET** /api/v1/llm/billing/logs/{log_id} | Get Log Details
[**get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get**](BillingApi.md#get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get) | **GET** /api/v1/llm/billing/usage/by-endpoint | Get Usage By Endpoint
[**get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get**](BillingApi.md#get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get) | **GET** /api/v1/llm/billing/usage/by-provider | Get Usage By Provider
[**get_usage_summary_api_v1_llm_billing_usage_summary_get**](BillingApi.md#get_usage_summary_api_v1_llm_billing_usage_summary_get) | **GET** /api/v1/llm/billing/usage/summary | Get Usage Summary


# **get_current_month_usage_api_v1_llm_billing_usage_current_month_get**
> object get_current_month_usage_api_v1_llm_billing_usage_current_month_get(x_api_key)

Get Current Month Usage

Get current month usage summary with budget status

Shows spending for current month and budget alerts if applicable.

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
    api_instance = llmhub_generated.BillingApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Current Month Usage
        api_response = api_instance.get_current_month_usage_api_v1_llm_billing_usage_current_month_get(x_api_key)
        print("The response of BillingApi->get_current_month_usage_api_v1_llm_billing_usage_current_month_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_current_month_usage_api_v1_llm_billing_usage_current_month_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_logs_api_v1_llm_billing_logs_get**
> object get_generation_logs_api_v1_llm_billing_logs_get(x_api_key, limit=limit, offset=offset, provider=provider, endpoint=endpoint, success=success)

Get Generation Logs

Get detailed generation logs

Returns individual LLM API calls with full details.
Useful for debugging and detailed analysis.

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
    api_instance = llmhub_generated.BillingApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    limit = 100 # int | Number of logs to return (optional) (default to 100)
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    provider = 'provider_example' # str | Filter by provider (optional)
    endpoint = 'endpoint_example' # str | Filter by endpoint (optional)
    success = True # bool | Filter by success status (optional)

    try:
        # Get Generation Logs
        api_response = api_instance.get_generation_logs_api_v1_llm_billing_logs_get(x_api_key, limit=limit, offset=offset, provider=provider, endpoint=endpoint, success=success)
        print("The response of BillingApi->get_generation_logs_api_v1_llm_billing_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_generation_logs_api_v1_llm_billing_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **limit** | **int**| Number of logs to return | [optional] [default to 100]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **provider** | **str**| Filter by provider | [optional] 
 **endpoint** | **str**| Filter by endpoint | [optional] 
 **success** | **bool**| Filter by success status | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_details_api_v1_llm_billing_logs_log_id_get**
> object get_log_details_api_v1_llm_billing_logs_log_id_get(log_id, x_api_key)

Get Log Details

Get detailed information for a specific log entry

Includes request/response metadata.

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
    api_instance = llmhub_generated.BillingApi(api_client)
    log_id = 'log_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Get Log Details
        api_response = api_instance.get_log_details_api_v1_llm_billing_logs_log_id_get(log_id, x_api_key)
        print("The response of BillingApi->get_log_details_api_v1_llm_billing_logs_log_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_log_details_api_v1_llm_billing_logs_log_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**|  | 
 **x_api_key** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get**
> object get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get(x_api_key, start_date=start_date, end_date=end_date)

Get Usage By Endpoint

Get usage breakdown by API endpoint

Shows which features are used most (content generation, images, translation, etc.)

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
    api_instance = llmhub_generated.BillingApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Usage By Endpoint
        api_response = api_instance.get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get(x_api_key, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_usage_by_endpoint_api_v1_llm_billing_usage_by_endpoint_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get**
> object get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get(x_api_key, start_date=start_date, end_date=end_date)

Get Usage By Provider

Get usage breakdown by LLM provider

Shows cost and usage distribution across Claude, OpenAI, Groq, etc.

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
    api_instance = llmhub_generated.BillingApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Usage By Provider
        api_response = api_instance.get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get(x_api_key, start_date=start_date, end_date=end_date)
        print("The response of BillingApi->get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_usage_by_provider_api_v1_llm_billing_usage_by_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_summary_api_v1_llm_billing_usage_summary_get**
> UsageReportResponse get_usage_summary_api_v1_llm_billing_usage_summary_get(x_api_key, start_date=start_date, end_date=end_date, group_by=group_by)

Get Usage Summary

Get usage summary for the current client

Returns aggregated usage data grouped by time period.
Includes cost, token usage, call counts, and success rates.

### Example


```python
import llmhub_generated
from llmhub_generated.models.usage_report_response import UsageReportResponse
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
    api_instance = llmhub_generated.BillingApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (defaults to 30 days ago) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (defaults to now) (optional)
    group_by = 'day' # str | Group by: hour, day, month (optional) (default to 'day')

    try:
        # Get Usage Summary
        api_response = api_instance.get_usage_summary_api_v1_llm_billing_usage_summary_get(x_api_key, start_date=start_date, end_date=end_date, group_by=group_by)
        print("The response of BillingApi->get_usage_summary_api_v1_llm_billing_usage_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_usage_summary_api_v1_llm_billing_usage_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **start_date** | **datetime**| Start date (defaults to 30 days ago) | [optional] 
 **end_date** | **datetime**| End date (defaults to now) | [optional] 
 **group_by** | **str**| Group by: hour, day, month | [optional] [default to &#39;day&#39;]

### Return type

[**UsageReportResponse**](UsageReportResponse.md)

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

