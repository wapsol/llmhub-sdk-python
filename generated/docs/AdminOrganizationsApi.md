# llmhub_generated.AdminOrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post**](AdminOrganizationsApi.md#create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post) | **POST** /api/v1/admin/organizations/{org_id}/pricing | Create custom pricing
[**create_organization_api_v1_admin_organizations_post**](AdminOrganizationsApi.md#create_organization_api_v1_admin_organizations_post) | **POST** /api/v1/admin/organizations | Create new organization
[**create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post**](AdminOrganizationsApi.md#create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post) | **POST** /api/v1/admin/organizations/{org_id}/usage-reports | Create Usage Report Record
[**delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete**](AdminOrganizationsApi.md#delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete) | **DELETE** /api/v1/admin/pricing/{pricing_id} | Delete custom pricing
[**download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get**](AdminOrganizationsApi.md#download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get) | **GET** /api/v1/admin/organizations/{org_id}/usage-reports/{report_id}/download | Download Usage Report PDF
[**generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post**](AdminOrganizationsApi.md#generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post) | **POST** /api/v1/admin/organizations/{org_id}/usage-reports/generate | Generate Usage Report PDF
[**get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get**](AdminOrganizationsApi.md#get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get) | **GET** /api/v1/admin/organizations/{org_id}/pricing | Get customer pricing rules
[**get_organization_activity_api_v1_admin_organizations_org_id_activity_get**](AdminOrganizationsApi.md#get_organization_activity_api_v1_admin_organizations_org_id_activity_get) | **GET** /api/v1/admin/organizations/{org_id}/activity | Get organization activity timeline
[**get_organization_api_v1_admin_organizations_org_id_get**](AdminOrganizationsApi.md#get_organization_api_v1_admin_organizations_org_id_get) | **GET** /api/v1/admin/organizations/{org_id} | Get organization by ID
[**get_organization_clients_api_v1_admin_organizations_org_id_clients_get**](AdminOrganizationsApi.md#get_organization_clients_api_v1_admin_organizations_org_id_clients_get) | **GET** /api/v1/admin/organizations/{org_id}/clients | Get API clients for organization
[**get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get**](AdminOrganizationsApi.md#get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get) | **GET** /api/v1/admin/organizations/{org_id}/usage-stats | Get organization usage statistics
[**get_organization_users_api_v1_admin_organizations_org_id_users_get**](AdminOrganizationsApi.md#get_organization_users_api_v1_admin_organizations_org_id_users_get) | **GET** /api/v1/admin/organizations/{org_id}/users | Get users for organization
[**get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post**](AdminOrganizationsApi.md#get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post) | **POST** /api/v1/admin/usage-reports/date-range | Get usage by date range
[**get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get**](AdminOrganizationsApi.md#get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get) | **GET** /api/v1/admin/organizations/{org_id}/usage-reports/{report_id} | Get Usage Report Details
[**get_usage_report_by_customer_api_v1_admin_usage_reports_post**](AdminOrganizationsApi.md#get_usage_report_by_customer_api_v1_admin_usage_reports_post) | **POST** /api/v1/admin/usage-reports | Get usage report by customer
[**list_organizations_api_v1_admin_organizations_get**](AdminOrganizationsApi.md#list_organizations_api_v1_admin_organizations_get) | **GET** /api/v1/admin/organizations | List all organizations
[**list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get**](AdminOrganizationsApi.md#list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get) | **GET** /api/v1/admin/organizations/{org_id}/usage-reports | List Usage Reports
[**toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch**](AdminOrganizationsApi.md#toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch) | **PATCH** /api/v1/admin/organizations/{org_id}/toggle-active | Toggle organization active status
[**update_customer_pricing_api_v1_admin_pricing_pricing_id_patch**](AdminOrganizationsApi.md#update_customer_pricing_api_v1_admin_pricing_pricing_id_patch) | **PATCH** /api/v1/admin/pricing/{pricing_id} | Update custom pricing
[**update_organization_api_v1_admin_organizations_org_id_patch**](AdminOrganizationsApi.md#update_organization_api_v1_admin_organizations_org_id_patch) | **PATCH** /api/v1/admin/organizations/{org_id} | Update organization


# **create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post**
> CustomerPricingResponse create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post(org_id, customer_pricing_create, session_token=session_token)

Create custom pricing

Create a new custom pricing rule for an organization

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.customer_pricing_create import CustomerPricingCreate
from llmhub_generated.models.customer_pricing_response import CustomerPricingResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    customer_pricing_create = llmhub_generated.CustomerPricingCreate() # CustomerPricingCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create custom pricing
        api_response = api_instance.create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post(org_id, customer_pricing_create, session_token=session_token)
        print("The response of AdminOrganizationsApi->create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->create_customer_pricing_api_v1_admin_organizations_org_id_pricing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **customer_pricing_create** | [**CustomerPricingCreate**](CustomerPricingCreate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CustomerPricingResponse**](CustomerPricingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_api_v1_admin_organizations_post**
> OrganizationResponse create_organization_api_v1_admin_organizations_post(organization_create, session_token=session_token)

Create new organization

Create a new organization

Organization name must be unique.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_create import OrganizationCreate
from llmhub_generated.models.organization_response import OrganizationResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    organization_create = llmhub_generated.OrganizationCreate() # OrganizationCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create new organization
        api_response = api_instance.create_organization_api_v1_admin_organizations_post(organization_create, session_token=session_token)
        print("The response of AdminOrganizationsApi->create_organization_api_v1_admin_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->create_organization_api_v1_admin_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_create** | [**OrganizationCreate**](OrganizationCreate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post**
> UsageReportResponse create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post(org_id, usage_report_create, session_token=session_token)

Create Usage Report Record

Create a new usage report metadata record for an organization

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.usage_report_create import UsageReportCreate
from llmhub_generated.models.usage_report_response import UsageReportResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    usage_report_create = llmhub_generated.UsageReportCreate() # UsageReportCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create Usage Report Record
        api_response = api_instance.create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post(org_id, usage_report_create, session_token=session_token)
        print("The response of AdminOrganizationsApi->create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->create_usage_report_api_v1_admin_organizations_org_id_usage_reports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **usage_report_create** | [**UsageReportCreate**](UsageReportCreate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportResponse**](UsageReportResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete**
> delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete(pricing_id, session_token=session_token)

Delete custom pricing

Delete a custom pricing rule

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    pricing_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Delete custom pricing
        api_instance.delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete(pricing_id, session_token=session_token)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->delete_customer_pricing_api_v1_admin_pricing_pricing_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get**
> object download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get(org_id, report_id, session_token=session_token)

Download Usage Report PDF

Download the PDF file for a specific usage report

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    report_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Download Usage Report PDF
        api_response = api_instance.download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get(org_id, report_id, session_token=session_token)
        print("The response of AdminOrganizationsApi->download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->download_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **report_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post**
> UsageReportResponse generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post(org_id, report_month, session_token=session_token)

Generate Usage Report PDF

Generate a new PDF usage report for an organization for a specific month

### Example

* Bearer Authentication (HTTPBearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    report_month = '2013-10-20T19:20:30+01:00' # datetime | First day of the report month (e.g., 2025-01-01)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Generate Usage Report PDF
        api_response = api_instance.generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post(org_id, report_month, session_token=session_token)
        print("The response of AdminOrganizationsApi->generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->generate_usage_report_api_v1_admin_organizations_org_id_usage_reports_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **report_month** | **datetime**| First day of the report month (e.g., 2025-01-01) | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportResponse**](UsageReportResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get**
> CustomerPricingListResponse get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get(org_id, is_active=is_active, session_token=session_token)

Get customer pricing rules

Get all custom pricing rules for an organization

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.customer_pricing_list_response import CustomerPricingListResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    is_active = True # bool | Filter by active status (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get customer pricing rules
        api_response = api_instance.get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get(org_id, is_active=is_active, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_customer_pricing_api_v1_admin_organizations_org_id_pricing_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **is_active** | **bool**| Filter by active status | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**CustomerPricingListResponse**](CustomerPricingListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_activity_api_v1_admin_organizations_org_id_activity_get**
> OrganizationActivityResponse get_organization_activity_api_v1_admin_organizations_org_id_activity_get(org_id, page=page, page_size=page_size, event_type=event_type, start_date=start_date, end_date=end_date, session_token=session_token)

Get organization activity timeline

Get activity timeline for an organization

Combines API calls, user events, and client events into a unified timeline.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_activity_response import OrganizationActivityResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    event_type = 'event_type_example' # str | Filter by event type (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter by start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter by end date (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get organization activity timeline
        api_response = api_instance.get_organization_activity_api_v1_admin_organizations_org_id_activity_get(org_id, page=page, page_size=page_size, event_type=event_type, start_date=start_date, end_date=end_date, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_organization_activity_api_v1_admin_organizations_org_id_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_organization_activity_api_v1_admin_organizations_org_id_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **event_type** | **str**| Filter by event type | [optional] 
 **start_date** | **datetime**| Filter by start date | [optional] 
 **end_date** | **datetime**| Filter by end date | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationActivityResponse**](OrganizationActivityResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_api_v1_admin_organizations_org_id_get**
> OrganizationResponse get_organization_api_v1_admin_organizations_org_id_get(org_id, session_token=session_token)

Get organization by ID

Get detailed information about a specific organization

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_response import OrganizationResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get organization by ID
        api_response = api_instance.get_organization_api_v1_admin_organizations_org_id_get(org_id, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_organization_api_v1_admin_organizations_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_organization_api_v1_admin_organizations_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_clients_api_v1_admin_organizations_org_id_clients_get**
> Dict[str, object] get_organization_clients_api_v1_admin_organizations_org_id_clients_get(org_id, is_active=is_active, session_token=session_token)

Get API clients for organization

Get all API clients belonging to a specific organization

Returns client details with usage statistics.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    is_active = True # bool | Filter by active status (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get API clients for organization
        api_response = api_instance.get_organization_clients_api_v1_admin_organizations_org_id_clients_get(org_id, is_active=is_active, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_organization_clients_api_v1_admin_organizations_org_id_clients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_organization_clients_api_v1_admin_organizations_org_id_clients_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **is_active** | **bool**| Filter by active status | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get**
> OrganizationUsageStatsResponse get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get(org_id, session_token=session_token)

Get organization usage statistics

Get comprehensive usage statistics for organization detail view

Returns quick stats including users, clients, usage, and budget utilization.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_usage_stats_response import OrganizationUsageStatsResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get organization usage statistics
        api_response = api_instance.get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get(org_id, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_organization_usage_stats_api_v1_admin_organizations_org_id_usage_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationUsageStatsResponse**](OrganizationUsageStatsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_users_api_v1_admin_organizations_org_id_users_get**
> Dict[str, object] get_organization_users_api_v1_admin_organizations_org_id_users_get(org_id, skip=skip, limit=limit, is_active=is_active, search=search, session_token=session_token)

Get users for organization

Get all users belonging to a specific organization

Returns user details with roles assigned.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Maximum records to return (optional) (default to 100)
    is_active = True # bool | Filter by active status (optional)
    search = 'search_example' # str | Search by name or email (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get users for organization
        api_response = api_instance.get_organization_users_api_v1_admin_organizations_org_id_users_get(org_id, skip=skip, limit=limit, is_active=is_active, search=search, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_organization_users_api_v1_admin_organizations_org_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_organization_users_api_v1_admin_organizations_org_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Maximum records to return | [optional] [default to 100]
 **is_active** | **bool**| Filter by active status | [optional] 
 **search** | **str**| Search by name or email | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post**
> UsageReportByCustomerResponse get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post(date_range_usage_request, session_token=session_token)

Get usage by date range

Simple endpoint to get usage data for a specific date range

Optionally filter by organization.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.date_range_usage_request import DateRangeUsageRequest
from llmhub_generated.models.usage_report_by_customer_response import UsageReportByCustomerResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    date_range_usage_request = llmhub_generated.DateRangeUsageRequest() # DateRangeUsageRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get usage by date range
        api_response = api_instance.get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post(date_range_usage_request, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_usage_by_date_range_api_v1_admin_usage_reports_date_range_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_range_usage_request** | [**DateRangeUsageRequest**](DateRangeUsageRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportByCustomerResponse**](UsageReportByCustomerResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get**
> UsageReportResponse get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get(org_id, report_id, session_token=session_token)

Get Usage Report Details

Get details of a specific usage report

### Example

* Bearer Authentication (HTTPBearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    report_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Usage Report Details
        api_response = api_instance.get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get(org_id, report_id, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_usage_report_api_v1_admin_organizations_org_id_usage_reports_report_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **report_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportResponse**](UsageReportResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_report_by_customer_api_v1_admin_usage_reports_post**
> UsageReportByCustomerResponse get_usage_report_by_customer_api_v1_admin_usage_reports_post(usage_report_by_customer_request, session_token=session_token)

Get usage report by customer

Get detailed usage report aggregated by customer and model

Supports date filtering, organization filtering, and grouping options.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.usage_report_by_customer_request import UsageReportByCustomerRequest
from llmhub_generated.models.usage_report_by_customer_response import UsageReportByCustomerResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    usage_report_by_customer_request = llmhub_generated.UsageReportByCustomerRequest() # UsageReportByCustomerRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get usage report by customer
        api_response = api_instance.get_usage_report_by_customer_api_v1_admin_usage_reports_post(usage_report_by_customer_request, session_token=session_token)
        print("The response of AdminOrganizationsApi->get_usage_report_by_customer_api_v1_admin_usage_reports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->get_usage_report_by_customer_api_v1_admin_usage_reports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_report_by_customer_request** | [**UsageReportByCustomerRequest**](UsageReportByCustomerRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportByCustomerResponse**](UsageReportByCustomerResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations_api_v1_admin_organizations_get**
> OrganizationListResponse list_organizations_api_v1_admin_organizations_get(skip=skip, limit=limit, is_active=is_active, search=search, session_token=session_token)

List all organizations

Get list of all organizations with optional filtering

Returns organizations with aggregated statistics:
- Total API clients
- Active API clients
- Last 30 days spending

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_list_response import OrganizationListResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    skip = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 100 # int | Maximum records to return (optional) (default to 100)
    is_active = True # bool | Filter by active status (optional)
    search = 'search_example' # str | Search by organization name (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List all organizations
        api_response = api_instance.list_organizations_api_v1_admin_organizations_get(skip=skip, limit=limit, is_active=is_active, search=search, session_token=session_token)
        print("The response of AdminOrganizationsApi->list_organizations_api_v1_admin_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->list_organizations_api_v1_admin_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Maximum records to return | [optional] [default to 100]
 **is_active** | **bool**| Filter by active status | [optional] 
 **search** | **str**| Search by organization name | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationListResponse**](OrganizationListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get**
> UsageReportListResponse list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get(org_id, page=page, page_size=page_size, year=year, session_token=session_token)

List Usage Reports

Get paginated list of usage reports for an organization

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.usage_report_list_response import UsageReportListResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    year = 56 # int | Filter by year (e.g., 2025) (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Usage Reports
        api_response = api_instance.list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get(org_id, page=page, page_size=page_size, year=year, session_token=session_token)
        print("The response of AdminOrganizationsApi->list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->list_usage_reports_api_v1_admin_organizations_org_id_usage_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **year** | **int**| Filter by year (e.g., 2025) | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**UsageReportListResponse**](UsageReportListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch**
> OrganizationResponse toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch(org_id, session_token=session_token)

Toggle organization active status

Toggle organization active/inactive status

This will also cascade the change to all associated API clients:
- When deactivating organization → deactivate all API clients
- When activating organization → activate all API clients

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_response import OrganizationResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Toggle organization active status
        api_response = api_instance.toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch(org_id, session_token=session_token)
        print("The response of AdminOrganizationsApi->toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->toggle_organization_active_api_v1_admin_organizations_org_id_toggle_active_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_pricing_api_v1_admin_pricing_pricing_id_patch**
> CustomerPricingResponse update_customer_pricing_api_v1_admin_pricing_pricing_id_patch(pricing_id, customer_pricing_update, session_token=session_token)

Update custom pricing

Update an existing custom pricing rule

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.customer_pricing_response import CustomerPricingResponse
from llmhub_generated.models.customer_pricing_update import CustomerPricingUpdate
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    pricing_id = 56 # int | 
    customer_pricing_update = llmhub_generated.CustomerPricingUpdate() # CustomerPricingUpdate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update custom pricing
        api_response = api_instance.update_customer_pricing_api_v1_admin_pricing_pricing_id_patch(pricing_id, customer_pricing_update, session_token=session_token)
        print("The response of AdminOrganizationsApi->update_customer_pricing_api_v1_admin_pricing_pricing_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->update_customer_pricing_api_v1_admin_pricing_pricing_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_id** | **int**|  | 
 **customer_pricing_update** | [**CustomerPricingUpdate**](CustomerPricingUpdate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CustomerPricingResponse**](CustomerPricingResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_api_v1_admin_organizations_org_id_patch**
> OrganizationResponse update_organization_api_v1_admin_organizations_org_id_patch(org_id, organization_update, session_token=session_token)

Update organization

Update an existing organization

Only provided fields will be updated.

**Requires super_admin role**

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.organization_response import OrganizationResponse
from llmhub_generated.models.organization_update import OrganizationUpdate
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = llmhub_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.AdminOrganizationsApi(api_client)
    org_id = 56 # int | 
    organization_update = llmhub_generated.OrganizationUpdate() # OrganizationUpdate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update organization
        api_response = api_instance.update_organization_api_v1_admin_organizations_org_id_patch(org_id, organization_update, session_token=session_token)
        print("The response of AdminOrganizationsApi->update_organization_api_v1_admin_organizations_org_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminOrganizationsApi->update_organization_api_v1_admin_organizations_org_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **organization_update** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

