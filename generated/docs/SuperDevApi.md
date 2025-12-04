# llmhub_generated.SuperDevApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post**](SuperDevApi.md#assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post) | **POST** /api/v1/super-dev/admin/assign-organization | Assign Organization To Super Dev
[**assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0**](SuperDevApi.md#assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0) | **POST** /api/v1/super-dev/admin/assign-organization | Assign Organization To Super Dev
[**create_organization_api_v1_super_dev_organizations_post**](SuperDevApi.md#create_organization_api_v1_super_dev_organizations_post) | **POST** /api/v1/super-dev/organizations | Create Organization
[**create_organization_api_v1_super_dev_organizations_post_0**](SuperDevApi.md#create_organization_api_v1_super_dev_organizations_post_0) | **POST** /api/v1/super-dev/organizations | Create Organization
[**generate_commission_report_api_v1_super_dev_commission_reports_generate_post**](SuperDevApi.md#generate_commission_report_api_v1_super_dev_commission_reports_generate_post) | **POST** /api/v1/super-dev/commission-reports/generate | Generate Commission Report
[**generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0**](SuperDevApi.md#generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0) | **POST** /api/v1/super-dev/commission-reports/generate | Generate Commission Report
[**get_commission_summary_api_v1_super_dev_commission_summary_get**](SuperDevApi.md#get_commission_summary_api_v1_super_dev_commission_summary_get) | **GET** /api/v1/super-dev/commission-summary | Get Commission Summary
[**get_commission_summary_api_v1_super_dev_commission_summary_get_0**](SuperDevApi.md#get_commission_summary_api_v1_super_dev_commission_summary_get_0) | **GET** /api/v1/super-dev/commission-summary | Get Commission Summary
[**get_super_dev_dashboard_api_v1_super_dev_dashboard_get**](SuperDevApi.md#get_super_dev_dashboard_api_v1_super_dev_dashboard_get) | **GET** /api/v1/super-dev/dashboard | Get Super Dev Dashboard
[**get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0**](SuperDevApi.md#get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0) | **GET** /api/v1/super-dev/dashboard | Get Super Dev Dashboard
[**list_commission_reports_api_v1_super_dev_commission_reports_get**](SuperDevApi.md#list_commission_reports_api_v1_super_dev_commission_reports_get) | **GET** /api/v1/super-dev/commission-reports | List Commission Reports
[**list_commission_reports_api_v1_super_dev_commission_reports_get_0**](SuperDevApi.md#list_commission_reports_api_v1_super_dev_commission_reports_get_0) | **GET** /api/v1/super-dev/commission-reports | List Commission Reports
[**list_my_organizations_api_v1_super_dev_organizations_get**](SuperDevApi.md#list_my_organizations_api_v1_super_dev_organizations_get) | **GET** /api/v1/super-dev/organizations | List My Organizations
[**list_my_organizations_api_v1_super_dev_organizations_get_0**](SuperDevApi.md#list_my_organizations_api_v1_super_dev_organizations_get_0) | **GET** /api/v1/super-dev/organizations | List My Organizations
[**list_super_devs_api_v1_super_dev_admin_list_get**](SuperDevApi.md#list_super_devs_api_v1_super_dev_admin_list_get) | **GET** /api/v1/super-dev/admin/list | List Super Devs
[**list_super_devs_api_v1_super_dev_admin_list_get_0**](SuperDevApi.md#list_super_devs_api_v1_super_dev_admin_list_get_0) | **GET** /api/v1/super-dev/admin/list | List Super Devs
[**set_commission_rate_api_v1_super_dev_admin_commission_rate_put**](SuperDevApi.md#set_commission_rate_api_v1_super_dev_admin_commission_rate_put) | **PUT** /api/v1/super-dev/admin/commission-rate | Set Commission Rate
[**set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0**](SuperDevApi.md#set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0) | **PUT** /api/v1/super-dev/admin/commission-rate | Set Commission Rate
[**unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post**](SuperDevApi.md#unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post) | **POST** /api/v1/super-dev/admin/unassign-organization | Unassign Organization From Super Dev
[**unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0**](SuperDevApi.md#unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0) | **POST** /api/v1/super-dev/admin/unassign-organization | Unassign Organization From Super Dev


# **assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post**
> SuperDevOrgAssignmentResponse assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post(assign_organization_request, session_token=session_token)

Assign Organization To Super Dev

Assign an organization to a Super Dev with initial commission rate

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.assign_organization_request import AssignOrganizationRequest
from llmhub_generated.models.super_dev_org_assignment_response import SuperDevOrgAssignmentResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    assign_organization_request = llmhub_generated.AssignOrganizationRequest() # AssignOrganizationRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Assign Organization To Super Dev
        api_response = api_instance.assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post(assign_organization_request, session_token=session_token)
        print("The response of SuperDevApi->assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_organization_request** | [**AssignOrganizationRequest**](AssignOrganizationRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevOrgAssignmentResponse**](SuperDevOrgAssignmentResponse.md)

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

# **assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0**
> SuperDevOrgAssignmentResponse assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0(assign_organization_request, session_token=session_token)

Assign Organization To Super Dev

Assign an organization to a Super Dev with initial commission rate

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.assign_organization_request import AssignOrganizationRequest
from llmhub_generated.models.super_dev_org_assignment_response import SuperDevOrgAssignmentResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    assign_organization_request = llmhub_generated.AssignOrganizationRequest() # AssignOrganizationRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Assign Organization To Super Dev
        api_response = api_instance.assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0(assign_organization_request, session_token=session_token)
        print("The response of SuperDevApi->assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->assign_organization_to_super_dev_api_v1_super_dev_admin_assign_organization_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_organization_request** | [**AssignOrganizationRequest**](AssignOrganizationRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevOrgAssignmentResponse**](SuperDevOrgAssignmentResponse.md)

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

# **create_organization_api_v1_super_dev_organizations_post**
> OrganizationResponse create_organization_api_v1_super_dev_organizations_post(organization_create, session_token=session_token)

Create Organization

Create a new organization (Super Devs are auto-assigned to orgs they create)

**Requires:** super_dev role

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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    organization_create = llmhub_generated.OrganizationCreate() # OrganizationCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create Organization
        api_response = api_instance.create_organization_api_v1_super_dev_organizations_post(organization_create, session_token=session_token)
        print("The response of SuperDevApi->create_organization_api_v1_super_dev_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->create_organization_api_v1_super_dev_organizations_post: %s\n" % e)
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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_api_v1_super_dev_organizations_post_0**
> OrganizationResponse create_organization_api_v1_super_dev_organizations_post_0(organization_create, session_token=session_token)

Create Organization

Create a new organization (Super Devs are auto-assigned to orgs they create)

**Requires:** super_dev role

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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    organization_create = llmhub_generated.OrganizationCreate() # OrganizationCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create Organization
        api_response = api_instance.create_organization_api_v1_super_dev_organizations_post_0(organization_create, session_token=session_token)
        print("The response of SuperDevApi->create_organization_api_v1_super_dev_organizations_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->create_organization_api_v1_super_dev_organizations_post_0: %s\n" % e)
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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_commission_report_api_v1_super_dev_commission_reports_generate_post**
> CommissionReportResponse generate_commission_report_api_v1_super_dev_commission_reports_generate_post(org_id, generate_commission_report_request, session_token=session_token)

Generate Commission Report

Generate commission report for a specific organization

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_report_response import CommissionReportResponse
from llmhub_generated.models.generate_commission_report_request import GenerateCommissionReportRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    org_id = 56 # int | 
    generate_commission_report_request = llmhub_generated.GenerateCommissionReportRequest() # GenerateCommissionReportRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Generate Commission Report
        api_response = api_instance.generate_commission_report_api_v1_super_dev_commission_reports_generate_post(org_id, generate_commission_report_request, session_token=session_token)
        print("The response of SuperDevApi->generate_commission_report_api_v1_super_dev_commission_reports_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->generate_commission_report_api_v1_super_dev_commission_reports_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **generate_commission_report_request** | [**GenerateCommissionReportRequest**](GenerateCommissionReportRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionReportResponse**](CommissionReportResponse.md)

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

# **generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0**
> CommissionReportResponse generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0(org_id, generate_commission_report_request, session_token=session_token)

Generate Commission Report

Generate commission report for a specific organization

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_report_response import CommissionReportResponse
from llmhub_generated.models.generate_commission_report_request import GenerateCommissionReportRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    org_id = 56 # int | 
    generate_commission_report_request = llmhub_generated.GenerateCommissionReportRequest() # GenerateCommissionReportRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Generate Commission Report
        api_response = api_instance.generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0(org_id, generate_commission_report_request, session_token=session_token)
        print("The response of SuperDevApi->generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->generate_commission_report_api_v1_super_dev_commission_reports_generate_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **generate_commission_report_request** | [**GenerateCommissionReportRequest**](GenerateCommissionReportRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionReportResponse**](CommissionReportResponse.md)

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

# **get_commission_summary_api_v1_super_dev_commission_summary_get**
> CommissionSummaryResponse get_commission_summary_api_v1_super_dev_commission_summary_get(period_start, period_end, session_token=session_token)

Get Commission Summary

Get commission summary across all organizations for a period

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_summary_response import CommissionSummaryResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | 
    period_end = '2013-10-20T19:20:30+01:00' # datetime | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Commission Summary
        api_response = api_instance.get_commission_summary_api_v1_super_dev_commission_summary_get(period_start, period_end, session_token=session_token)
        print("The response of SuperDevApi->get_commission_summary_api_v1_super_dev_commission_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->get_commission_summary_api_v1_super_dev_commission_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_start** | **datetime**|  | 
 **period_end** | **datetime**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionSummaryResponse**](CommissionSummaryResponse.md)

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

# **get_commission_summary_api_v1_super_dev_commission_summary_get_0**
> CommissionSummaryResponse get_commission_summary_api_v1_super_dev_commission_summary_get_0(period_start, period_end, session_token=session_token)

Get Commission Summary

Get commission summary across all organizations for a period

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_summary_response import CommissionSummaryResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | 
    period_end = '2013-10-20T19:20:30+01:00' # datetime | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Commission Summary
        api_response = api_instance.get_commission_summary_api_v1_super_dev_commission_summary_get_0(period_start, period_end, session_token=session_token)
        print("The response of SuperDevApi->get_commission_summary_api_v1_super_dev_commission_summary_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->get_commission_summary_api_v1_super_dev_commission_summary_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_start** | **datetime**|  | 
 **period_end** | **datetime**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionSummaryResponse**](CommissionSummaryResponse.md)

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

# **get_super_dev_dashboard_api_v1_super_dev_dashboard_get**
> SuperDevDashboardStats get_super_dev_dashboard_api_v1_super_dev_dashboard_get(session_token=session_token)

Get Super Dev Dashboard

Get dashboard statistics for current Super Dev

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.super_dev_dashboard_stats import SuperDevDashboardStats
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Super Dev Dashboard
        api_response = api_instance.get_super_dev_dashboard_api_v1_super_dev_dashboard_get(session_token=session_token)
        print("The response of SuperDevApi->get_super_dev_dashboard_api_v1_super_dev_dashboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->get_super_dev_dashboard_api_v1_super_dev_dashboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevDashboardStats**](SuperDevDashboardStats.md)

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

# **get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0**
> SuperDevDashboardStats get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0(session_token=session_token)

Get Super Dev Dashboard

Get dashboard statistics for current Super Dev

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.super_dev_dashboard_stats import SuperDevDashboardStats
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get Super Dev Dashboard
        api_response = api_instance.get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0(session_token=session_token)
        print("The response of SuperDevApi->get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->get_super_dev_dashboard_api_v1_super_dev_dashboard_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevDashboardStats**](SuperDevDashboardStats.md)

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

# **list_commission_reports_api_v1_super_dev_commission_reports_get**
> List[CommissionReportResponse] list_commission_reports_api_v1_super_dev_commission_reports_get(report_status=report_status, session_token=session_token)

List Commission Reports

List commission reports for current Super Dev

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_report_response import CommissionReportResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    report_status = 'report_status_example' # str |  (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Commission Reports
        api_response = api_instance.list_commission_reports_api_v1_super_dev_commission_reports_get(report_status=report_status, session_token=session_token)
        print("The response of SuperDevApi->list_commission_reports_api_v1_super_dev_commission_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_commission_reports_api_v1_super_dev_commission_reports_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_status** | **str**|  | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**List[CommissionReportResponse]**](CommissionReportResponse.md)

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

# **list_commission_reports_api_v1_super_dev_commission_reports_get_0**
> List[CommissionReportResponse] list_commission_reports_api_v1_super_dev_commission_reports_get_0(report_status=report_status, session_token=session_token)

List Commission Reports

List commission reports for current Super Dev

**Requires:** super_dev role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_report_response import CommissionReportResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    report_status = 'report_status_example' # str |  (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Commission Reports
        api_response = api_instance.list_commission_reports_api_v1_super_dev_commission_reports_get_0(report_status=report_status, session_token=session_token)
        print("The response of SuperDevApi->list_commission_reports_api_v1_super_dev_commission_reports_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_commission_reports_api_v1_super_dev_commission_reports_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_status** | **str**|  | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**List[CommissionReportResponse]**](CommissionReportResponse.md)

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

# **list_my_organizations_api_v1_super_dev_organizations_get**
> object list_my_organizations_api_v1_super_dev_organizations_get(session_token=session_token)

List My Organizations

List organizations assigned to current Super Dev

**Requires:** super_dev role

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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List My Organizations
        api_response = api_instance.list_my_organizations_api_v1_super_dev_organizations_get(session_token=session_token)
        print("The response of SuperDevApi->list_my_organizations_api_v1_super_dev_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_my_organizations_api_v1_super_dev_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

**object**

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

# **list_my_organizations_api_v1_super_dev_organizations_get_0**
> object list_my_organizations_api_v1_super_dev_organizations_get_0(session_token=session_token)

List My Organizations

List organizations assigned to current Super Dev

**Requires:** super_dev role

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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List My Organizations
        api_response = api_instance.list_my_organizations_api_v1_super_dev_organizations_get_0(session_token=session_token)
        print("The response of SuperDevApi->list_my_organizations_api_v1_super_dev_organizations_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_my_organizations_api_v1_super_dev_organizations_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

**object**

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

# **list_super_devs_api_v1_super_dev_admin_list_get**
> SuperDevListResponse list_super_devs_api_v1_super_dev_admin_list_get(session_token=session_token)

List Super Devs

List all Super Devs with their statistics

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.super_dev_list_response import SuperDevListResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Super Devs
        api_response = api_instance.list_super_devs_api_v1_super_dev_admin_list_get(session_token=session_token)
        print("The response of SuperDevApi->list_super_devs_api_v1_super_dev_admin_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_super_devs_api_v1_super_dev_admin_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevListResponse**](SuperDevListResponse.md)

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

# **list_super_devs_api_v1_super_dev_admin_list_get_0**
> SuperDevListResponse list_super_devs_api_v1_super_dev_admin_list_get_0(session_token=session_token)

List Super Devs

List all Super Devs with their statistics

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.super_dev_list_response import SuperDevListResponse
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Super Devs
        api_response = api_instance.list_super_devs_api_v1_super_dev_admin_list_get_0(session_token=session_token)
        print("The response of SuperDevApi->list_super_devs_api_v1_super_dev_admin_list_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->list_super_devs_api_v1_super_dev_admin_list_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**SuperDevListResponse**](SuperDevListResponse.md)

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

# **set_commission_rate_api_v1_super_dev_admin_commission_rate_put**
> CommissionRateResponse set_commission_rate_api_v1_super_dev_admin_commission_rate_put(set_commission_rate_request, session_token=session_token)

Set Commission Rate

Set or update commission rate for a Super Dev and organization

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_rate_response import CommissionRateResponse
from llmhub_generated.models.set_commission_rate_request import SetCommissionRateRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    set_commission_rate_request = llmhub_generated.SetCommissionRateRequest() # SetCommissionRateRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Set Commission Rate
        api_response = api_instance.set_commission_rate_api_v1_super_dev_admin_commission_rate_put(set_commission_rate_request, session_token=session_token)
        print("The response of SuperDevApi->set_commission_rate_api_v1_super_dev_admin_commission_rate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->set_commission_rate_api_v1_super_dev_admin_commission_rate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_commission_rate_request** | [**SetCommissionRateRequest**](SetCommissionRateRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionRateResponse**](CommissionRateResponse.md)

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

# **set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0**
> CommissionRateResponse set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0(set_commission_rate_request, session_token=session_token)

Set Commission Rate

Set or update commission rate for a Super Dev and organization

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.commission_rate_response import CommissionRateResponse
from llmhub_generated.models.set_commission_rate_request import SetCommissionRateRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    set_commission_rate_request = llmhub_generated.SetCommissionRateRequest() # SetCommissionRateRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Set Commission Rate
        api_response = api_instance.set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0(set_commission_rate_request, session_token=session_token)
        print("The response of SuperDevApi->set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->set_commission_rate_api_v1_super_dev_admin_commission_rate_put_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_commission_rate_request** | [**SetCommissionRateRequest**](SetCommissionRateRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**CommissionRateResponse**](CommissionRateResponse.md)

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

# **unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post**
> object unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post(unassign_organization_request, session_token=session_token)

Unassign Organization From Super Dev

Unassign an organization from a Super Dev

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.unassign_organization_request import UnassignOrganizationRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    unassign_organization_request = llmhub_generated.UnassignOrganizationRequest() # UnassignOrganizationRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Unassign Organization From Super Dev
        api_response = api_instance.unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post(unassign_organization_request, session_token=session_token)
        print("The response of SuperDevApi->unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unassign_organization_request** | [**UnassignOrganizationRequest**](UnassignOrganizationRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**object**

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

# **unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0**
> object unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0(unassign_organization_request, session_token=session_token)

Unassign Organization From Super Dev

Unassign an organization from a Super Dev

**Requires:** super_admin role

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.unassign_organization_request import UnassignOrganizationRequest
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
    api_instance = llmhub_generated.SuperDevApi(api_client)
    unassign_organization_request = llmhub_generated.UnassignOrganizationRequest() # UnassignOrganizationRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Unassign Organization From Super Dev
        api_response = api_instance.unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0(unassign_organization_request, session_token=session_token)
        print("The response of SuperDevApi->unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperDevApi->unassign_organization_from_super_dev_api_v1_super_dev_admin_unassign_organization_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unassign_organization_request** | [**UnassignOrganizationRequest**](UnassignOrganizationRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

**object**

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

