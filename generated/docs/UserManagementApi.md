# llmhub_generated.UserManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post**](UserManagementApi.md#admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post) | **POST** /api/v1/users/{user_id}/admin-generate-reset-link | Admin Generate Reset Link
[**admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0**](UserManagementApi.md#admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0) | **POST** /api/v1/users/{user_id}/admin-generate-reset-link | Admin Generate Reset Link
[**admin_set_password_api_v1_users_user_id_admin_set_password_post**](UserManagementApi.md#admin_set_password_api_v1_users_user_id_admin_set_password_post) | **POST** /api/v1/users/{user_id}/admin-set-password | Admin Set Password
[**admin_set_password_api_v1_users_user_id_admin_set_password_post_0**](UserManagementApi.md#admin_set_password_api_v1_users_user_id_admin_set_password_post_0) | **POST** /api/v1/users/{user_id}/admin-set-password | Admin Set Password
[**assign_role_to_user_api_v1_users_user_id_roles_post**](UserManagementApi.md#assign_role_to_user_api_v1_users_user_id_roles_post) | **POST** /api/v1/users/{user_id}/roles | Assign Role To User
[**assign_role_to_user_api_v1_users_user_id_roles_post_0**](UserManagementApi.md#assign_role_to_user_api_v1_users_user_id_roles_post_0) | **POST** /api/v1/users/{user_id}/roles | Assign Role To User
[**create_user_api_v1_users_post**](UserManagementApi.md#create_user_api_v1_users_post) | **POST** /api/v1/users | Create User
[**create_user_api_v1_users_post_0**](UserManagementApi.md#create_user_api_v1_users_post_0) | **POST** /api/v1/users | Create User
[**delete_user_api_v1_users_user_id_delete**](UserManagementApi.md#delete_user_api_v1_users_user_id_delete) | **DELETE** /api/v1/users/{user_id} | Delete User
[**delete_user_api_v1_users_user_id_delete_0**](UserManagementApi.md#delete_user_api_v1_users_user_id_delete_0) | **DELETE** /api/v1/users/{user_id} | Delete User
[**get_user_activity_api_v1_users_user_id_activity_get**](UserManagementApi.md#get_user_activity_api_v1_users_user_id_activity_get) | **GET** /api/v1/users/{user_id}/activity | Get User Activity
[**get_user_activity_api_v1_users_user_id_activity_get_0**](UserManagementApi.md#get_user_activity_api_v1_users_user_id_activity_get_0) | **GET** /api/v1/users/{user_id}/activity | Get User Activity
[**get_user_api_v1_users_user_id_get**](UserManagementApi.md#get_user_api_v1_users_user_id_get) | **GET** /api/v1/users/{user_id} | Get User
[**get_user_api_v1_users_user_id_get_0**](UserManagementApi.md#get_user_api_v1_users_user_id_get_0) | **GET** /api/v1/users/{user_id} | Get User
[**list_available_roles_api_v1_users_roles_available_get**](UserManagementApi.md#list_available_roles_api_v1_users_roles_available_get) | **GET** /api/v1/users/roles/available | List Available Roles
[**list_available_roles_api_v1_users_roles_available_get_0**](UserManagementApi.md#list_available_roles_api_v1_users_roles_available_get_0) | **GET** /api/v1/users/roles/available | List Available Roles
[**list_users_api_v1_users_get**](UserManagementApi.md#list_users_api_v1_users_get) | **GET** /api/v1/users | List Users
[**list_users_api_v1_users_get_0**](UserManagementApi.md#list_users_api_v1_users_get_0) | **GET** /api/v1/users | List Users
[**remove_role_from_user_api_v1_users_user_id_roles_role_name_delete**](UserManagementApi.md#remove_role_from_user_api_v1_users_user_id_roles_role_name_delete) | **DELETE** /api/v1/users/{user_id}/roles/{role_name} | Remove Role From User
[**remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0**](UserManagementApi.md#remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0) | **DELETE** /api/v1/users/{user_id}/roles/{role_name} | Remove Role From User
[**update_user_api_v1_users_user_id_patch**](UserManagementApi.md#update_user_api_v1_users_user_id_patch) | **PATCH** /api/v1/users/{user_id} | Update User
[**update_user_api_v1_users_user_id_patch_0**](UserManagementApi.md#update_user_api_v1_users_user_id_patch_0) | **PATCH** /api/v1/users/{user_id} | Update User


# **admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post**
> AdminGenerateResetLinkResponse admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post(user_id, admin_generate_reset_link_request, session_token=session_token)

Admin Generate Reset Link

Generate password reset link for a user (admin-initiated)

This endpoint allows administrators to generate a password reset link
and optionally send it via email. The link can be copied and shared manually
via email, chat, SMS, or other channels.

**Permissions:**
- **Super Admin:** Can generate reset link for any user
- **Organization Admin:** Can generate reset link for users in their organization

**Security:**
- Reset link valid for 1 hour
- Single-use token
- Action logged for audit trail
- Admin responsible for secure delivery

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.admin_generate_reset_link_request import AdminGenerateResetLinkRequest
from llmhub_generated.models.admin_generate_reset_link_response import AdminGenerateResetLinkResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    admin_generate_reset_link_request = llmhub_generated.AdminGenerateResetLinkRequest() # AdminGenerateResetLinkRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Admin Generate Reset Link
        api_response = api_instance.admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post(user_id, admin_generate_reset_link_request, session_token=session_token)
        print("The response of UserManagementApi->admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_generate_reset_link_request** | [**AdminGenerateResetLinkRequest**](AdminGenerateResetLinkRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**AdminGenerateResetLinkResponse**](AdminGenerateResetLinkResponse.md)

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

# **admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0**
> AdminGenerateResetLinkResponse admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0(user_id, admin_generate_reset_link_request, session_token=session_token)

Admin Generate Reset Link

Generate password reset link for a user (admin-initiated)

This endpoint allows administrators to generate a password reset link
and optionally send it via email. The link can be copied and shared manually
via email, chat, SMS, or other channels.

**Permissions:**
- **Super Admin:** Can generate reset link for any user
- **Organization Admin:** Can generate reset link for users in their organization

**Security:**
- Reset link valid for 1 hour
- Single-use token
- Action logged for audit trail
- Admin responsible for secure delivery

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.admin_generate_reset_link_request import AdminGenerateResetLinkRequest
from llmhub_generated.models.admin_generate_reset_link_response import AdminGenerateResetLinkResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    admin_generate_reset_link_request = llmhub_generated.AdminGenerateResetLinkRequest() # AdminGenerateResetLinkRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Admin Generate Reset Link
        api_response = api_instance.admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0(user_id, admin_generate_reset_link_request, session_token=session_token)
        print("The response of UserManagementApi->admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->admin_generate_reset_link_api_v1_users_user_id_admin_generate_reset_link_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_generate_reset_link_request** | [**AdminGenerateResetLinkRequest**](AdminGenerateResetLinkRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**AdminGenerateResetLinkResponse**](AdminGenerateResetLinkResponse.md)

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

# **admin_set_password_api_v1_users_user_id_admin_set_password_post**
> AdminSetPasswordResponse admin_set_password_api_v1_users_user_id_admin_set_password_post(user_id, admin_set_password_request, session_token=session_token)

Admin Set Password

Set a new password for a user (admin-initiated)

This endpoint allows administrators to set a new password for a user.
All existing sessions for the user will be invalidated for security.
Optionally sends an email notification to the user with the new password.

**Permissions:**
- **Super Admin:** Can change password for any user
- **Organization Admin:** Can change password for users in their organization

**Security:**
- Password must be at least 8 characters
- All user sessions are invalidated
- Email notification sent (if enabled)
- Action is logged for audit trail

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.admin_set_password_request import AdminSetPasswordRequest
from llmhub_generated.models.admin_set_password_response import AdminSetPasswordResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    admin_set_password_request = llmhub_generated.AdminSetPasswordRequest() # AdminSetPasswordRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Admin Set Password
        api_response = api_instance.admin_set_password_api_v1_users_user_id_admin_set_password_post(user_id, admin_set_password_request, session_token=session_token)
        print("The response of UserManagementApi->admin_set_password_api_v1_users_user_id_admin_set_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->admin_set_password_api_v1_users_user_id_admin_set_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_set_password_request** | [**AdminSetPasswordRequest**](AdminSetPasswordRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**AdminSetPasswordResponse**](AdminSetPasswordResponse.md)

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

# **admin_set_password_api_v1_users_user_id_admin_set_password_post_0**
> AdminSetPasswordResponse admin_set_password_api_v1_users_user_id_admin_set_password_post_0(user_id, admin_set_password_request, session_token=session_token)

Admin Set Password

Set a new password for a user (admin-initiated)

This endpoint allows administrators to set a new password for a user.
All existing sessions for the user will be invalidated for security.
Optionally sends an email notification to the user with the new password.

**Permissions:**
- **Super Admin:** Can change password for any user
- **Organization Admin:** Can change password for users in their organization

**Security:**
- Password must be at least 8 characters
- All user sessions are invalidated
- Email notification sent (if enabled)
- Action is logged for audit trail

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.admin_set_password_request import AdminSetPasswordRequest
from llmhub_generated.models.admin_set_password_response import AdminSetPasswordResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    admin_set_password_request = llmhub_generated.AdminSetPasswordRequest() # AdminSetPasswordRequest | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Admin Set Password
        api_response = api_instance.admin_set_password_api_v1_users_user_id_admin_set_password_post_0(user_id, admin_set_password_request, session_token=session_token)
        print("The response of UserManagementApi->admin_set_password_api_v1_users_user_id_admin_set_password_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->admin_set_password_api_v1_users_user_id_admin_set_password_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **admin_set_password_request** | [**AdminSetPasswordRequest**](AdminSetPasswordRequest.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**AdminSetPasswordResponse**](AdminSetPasswordResponse.md)

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

# **assign_role_to_user_api_v1_users_user_id_roles_post**
> UserResponse assign_role_to_user_api_v1_users_user_id_roles_post(user_id, user_role_assignment, session_token=session_token)

Assign Role To User

Assign a role to a user

**Permissions:**
- **Super Admin:** Can assign any role to any user
- **Super Dev:** Can assign org_admin or user roles to users in assigned organizations
- **Organization Admin:** Can assign org_admin or user roles to users in their organization

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
from llmhub_generated.models.user_role_assignment import UserRoleAssignment
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    user_role_assignment = llmhub_generated.UserRoleAssignment() # UserRoleAssignment | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Assign Role To User
        api_response = api_instance.assign_role_to_user_api_v1_users_user_id_roles_post(user_id, user_role_assignment, session_token=session_token)
        print("The response of UserManagementApi->assign_role_to_user_api_v1_users_user_id_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->assign_role_to_user_api_v1_users_user_id_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_role_assignment** | [**UserRoleAssignment**](UserRoleAssignment.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **assign_role_to_user_api_v1_users_user_id_roles_post_0**
> UserResponse assign_role_to_user_api_v1_users_user_id_roles_post_0(user_id, user_role_assignment, session_token=session_token)

Assign Role To User

Assign a role to a user

**Permissions:**
- **Super Admin:** Can assign any role to any user
- **Super Dev:** Can assign org_admin or user roles to users in assigned organizations
- **Organization Admin:** Can assign org_admin or user roles to users in their organization

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
from llmhub_generated.models.user_role_assignment import UserRoleAssignment
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    user_role_assignment = llmhub_generated.UserRoleAssignment() # UserRoleAssignment | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Assign Role To User
        api_response = api_instance.assign_role_to_user_api_v1_users_user_id_roles_post_0(user_id, user_role_assignment, session_token=session_token)
        print("The response of UserManagementApi->assign_role_to_user_api_v1_users_user_id_roles_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->assign_role_to_user_api_v1_users_user_id_roles_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_role_assignment** | [**UserRoleAssignment**](UserRoleAssignment.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **create_user_api_v1_users_post**
> UserResponse create_user_api_v1_users_post(user_create, session_token=session_token)

Create User

Create a new user in an organization

**Permissions:**
- **Super Admin:** Can create users in any organization
- **Super Dev:** Can create users in assigned organizations
- **Organization Admin:** Can create users in their organization only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_create import UserCreate
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_create = llmhub_generated.UserCreate() # UserCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create User
        api_response = api_instance.create_user_api_v1_users_post(user_create, session_token=session_token)
        print("The response of UserManagementApi->create_user_api_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->create_user_api_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **create_user_api_v1_users_post_0**
> UserResponse create_user_api_v1_users_post_0(user_create, session_token=session_token)

Create User

Create a new user in an organization

**Permissions:**
- **Super Admin:** Can create users in any organization
- **Super Dev:** Can create users in assigned organizations
- **Organization Admin:** Can create users in their organization only

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_create import UserCreate
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_create = llmhub_generated.UserCreate() # UserCreate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Create User
        api_response = api_instance.create_user_api_v1_users_post_0(user_create, session_token=session_token)
        print("The response of UserManagementApi->create_user_api_v1_users_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->create_user_api_v1_users_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **delete_user_api_v1_users_user_id_delete**
> delete_user_api_v1_users_user_id_delete(user_id, session_token=session_token)

Delete User

Deactivate a user (soft delete)

**Note:** This doesn't delete the user from the database, it just sets is_active=False.

**Permissions:**
- **Super Admin:** Can deactivate any user
- **Organization Admin:** Can deactivate users in their organization

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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Delete User
        api_instance.delete_user_api_v1_users_user_id_delete(user_id, session_token=session_token)
    except Exception as e:
        print("Exception when calling UserManagementApi->delete_user_api_v1_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **delete_user_api_v1_users_user_id_delete_0**
> delete_user_api_v1_users_user_id_delete_0(user_id, session_token=session_token)

Delete User

Deactivate a user (soft delete)

**Note:** This doesn't delete the user from the database, it just sets is_active=False.

**Permissions:**
- **Super Admin:** Can deactivate any user
- **Organization Admin:** Can deactivate users in their organization

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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Delete User
        api_instance.delete_user_api_v1_users_user_id_delete_0(user_id, session_token=session_token)
    except Exception as e:
        print("Exception when calling UserManagementApi->delete_user_api_v1_users_user_id_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_user_activity_api_v1_users_user_id_activity_get**
> UserActivityResponse get_user_activity_api_v1_users_user_id_activity_get(user_id, page=page, page_size=page_size, event_type=event_type, session_token=session_token)

Get User Activity

Get activity timeline for a specific user

Returns a timeline of user activities including:
- Login events
- Role assignments/removals
- Profile updates
- Account creation

**Permissions:**
- **Super Admin:** Can view activity for any user
- **Organization Admin:** Can view activity for users in their organization
- **User:** Can view their own activity

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_activity_response import UserActivityResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    event_type = 'event_type_example' # str | Filter by event type (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Activity
        api_response = api_instance.get_user_activity_api_v1_users_user_id_activity_get(user_id, page=page, page_size=page_size, event_type=event_type, session_token=session_token)
        print("The response of UserManagementApi->get_user_activity_api_v1_users_user_id_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_activity_api_v1_users_user_id_activity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **event_type** | **str**| Filter by event type | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserActivityResponse**](UserActivityResponse.md)

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

# **get_user_activity_api_v1_users_user_id_activity_get_0**
> UserActivityResponse get_user_activity_api_v1_users_user_id_activity_get_0(user_id, page=page, page_size=page_size, event_type=event_type, session_token=session_token)

Get User Activity

Get activity timeline for a specific user

Returns a timeline of user activities including:
- Login events
- Role assignments/removals
- Profile updates
- Account creation

**Permissions:**
- **Super Admin:** Can view activity for any user
- **Organization Admin:** Can view activity for users in their organization
- **User:** Can view their own activity

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_activity_response import UserActivityResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    event_type = 'event_type_example' # str | Filter by event type (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User Activity
        api_response = api_instance.get_user_activity_api_v1_users_user_id_activity_get_0(user_id, page=page, page_size=page_size, event_type=event_type, session_token=session_token)
        print("The response of UserManagementApi->get_user_activity_api_v1_users_user_id_activity_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_activity_api_v1_users_user_id_activity_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **event_type** | **str**| Filter by event type | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserActivityResponse**](UserActivityResponse.md)

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

# **get_user_api_v1_users_user_id_get**
> UserResponse get_user_api_v1_users_user_id_get(user_id, session_token=session_token)

Get User

Get detailed information about a specific user

**Permissions:**
- **Super Admin:** Can view any user
- **Super Dev:** Can view users in assigned organizations
- **Organization Admin:** Can view users in their organization
- **User:** Can only view their own profile

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User
        api_response = api_instance.get_user_api_v1_users_user_id_get(user_id, session_token=session_token)
        print("The response of UserManagementApi->get_user_api_v1_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_api_v1_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_api_v1_users_user_id_get_0**
> UserResponse get_user_api_v1_users_user_id_get_0(user_id, session_token=session_token)

Get User

Get detailed information about a specific user

**Permissions:**
- **Super Admin:** Can view any user
- **Super Dev:** Can view users in assigned organizations
- **Organization Admin:** Can view users in their organization
- **User:** Can only view their own profile

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Get User
        api_response = api_instance.get_user_api_v1_users_user_id_get_0(user_id, session_token=session_token)
        print("The response of UserManagementApi->get_user_api_v1_users_user_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_api_v1_users_user_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **list_available_roles_api_v1_users_roles_available_get**
> List[RoleResponse] list_available_roles_api_v1_users_roles_available_get(session_token=session_token)

List Available Roles

List available roles

**Permissions:**
- **Super Admin:** Can see all roles
- **Organization Admin:** Can see org_admin and user roles (cannot assign super_admin)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.role_response import RoleResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Available Roles
        api_response = api_instance.list_available_roles_api_v1_users_roles_available_get(session_token=session_token)
        print("The response of UserManagementApi->list_available_roles_api_v1_users_roles_available_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_available_roles_api_v1_users_roles_available_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**List[RoleResponse]**](RoleResponse.md)

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

# **list_available_roles_api_v1_users_roles_available_get_0**
> List[RoleResponse] list_available_roles_api_v1_users_roles_available_get_0(session_token=session_token)

List Available Roles

List available roles

**Permissions:**
- **Super Admin:** Can see all roles
- **Organization Admin:** Can see org_admin and user roles (cannot assign super_admin)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.role_response import RoleResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Available Roles
        api_response = api_instance.list_available_roles_api_v1_users_roles_available_get_0(session_token=session_token)
        print("The response of UserManagementApi->list_available_roles_api_v1_users_roles_available_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_available_roles_api_v1_users_roles_available_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_token** | **str**|  | [optional] 

### Return type

[**List[RoleResponse]**](RoleResponse.md)

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

# **list_users_api_v1_users_get**
> UserListResponse list_users_api_v1_users_get(page=page, page_size=page_size, org_id=org_id, is_active=is_active, search=search, role_filter=role_filter, session_token=session_token)

List Users

List users with pagination and filtering

**Permissions:**
- **Super Admin:** Can see all users across all organizations
- **Super Dev:** Can see users from assigned organizations only
- **Organization Admin:** Can only see users in their organization
- **User:** Not authorized (403)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_list_response import UserListResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    org_id = 56 # int | Filter by organization ID (optional)
    is_active = True # bool | Filter by active status (optional)
    search = 'search_example' # str | Search by email or name (optional)
    role_filter = 'role_filter_example' # str | Filter by roles (comma-separated: super_admin,super_dev,org_admin,user) (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Users
        api_response = api_instance.list_users_api_v1_users_get(page=page, page_size=page_size, org_id=org_id, is_active=is_active, search=search, role_filter=role_filter, session_token=session_token)
        print("The response of UserManagementApi->list_users_api_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_users_api_v1_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **org_id** | **int**| Filter by organization ID | [optional] 
 **is_active** | **bool**| Filter by active status | [optional] 
 **search** | **str**| Search by email or name | [optional] 
 **role_filter** | **str**| Filter by roles (comma-separated: super_admin,super_dev,org_admin,user) | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **list_users_api_v1_users_get_0**
> UserListResponse list_users_api_v1_users_get_0(page=page, page_size=page_size, org_id=org_id, is_active=is_active, search=search, role_filter=role_filter, session_token=session_token)

List Users

List users with pagination and filtering

**Permissions:**
- **Super Admin:** Can see all users across all organizations
- **Super Dev:** Can see users from assigned organizations only
- **Organization Admin:** Can only see users in their organization
- **User:** Not authorized (403)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_list_response import UserListResponse
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    org_id = 56 # int | Filter by organization ID (optional)
    is_active = True # bool | Filter by active status (optional)
    search = 'search_example' # str | Search by email or name (optional)
    role_filter = 'role_filter_example' # str | Filter by roles (comma-separated: super_admin,super_dev,org_admin,user) (optional)
    session_token = 'session_token_example' # str |  (optional)

    try:
        # List Users
        api_response = api_instance.list_users_api_v1_users_get_0(page=page, page_size=page_size, org_id=org_id, is_active=is_active, search=search, role_filter=role_filter, session_token=session_token)
        print("The response of UserManagementApi->list_users_api_v1_users_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_users_api_v1_users_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **org_id** | **int**| Filter by organization ID | [optional] 
 **is_active** | **bool**| Filter by active status | [optional] 
 **search** | **str**| Search by email or name | [optional] 
 **role_filter** | **str**| Filter by roles (comma-separated: super_admin,super_dev,org_admin,user) | [optional] 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **remove_role_from_user_api_v1_users_user_id_roles_role_name_delete**
> remove_role_from_user_api_v1_users_user_id_roles_role_name_delete(user_id, role_name, session_token=session_token)

Remove Role From User

Remove a role from a user

**Permissions:**
- **Super Admin:** Can remove any role from any user
- **Organization Admin:** Can remove org_admin or user roles from users in their organization

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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    role_name = 'role_name_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Remove Role From User
        api_instance.remove_role_from_user_api_v1_users_user_id_roles_role_name_delete(user_id, role_name, session_token=session_token)
    except Exception as e:
        print("Exception when calling UserManagementApi->remove_role_from_user_api_v1_users_user_id_roles_role_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_name** | **str**|  | 
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

# **remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0**
> remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0(user_id, role_name, session_token=session_token)

Remove Role From User

Remove a role from a user

**Permissions:**
- **Super Admin:** Can remove any role from any user
- **Organization Admin:** Can remove org_admin or user roles from users in their organization

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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    role_name = 'role_name_example' # str | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Remove Role From User
        api_instance.remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0(user_id, role_name, session_token=session_token)
    except Exception as e:
        print("Exception when calling UserManagementApi->remove_role_from_user_api_v1_users_user_id_roles_role_name_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_name** | **str**|  | 
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

# **update_user_api_v1_users_user_id_patch**
> UserResponse update_user_api_v1_users_user_id_patch(user_id, user_update, session_token=session_token)

Update User

Update user information

**Permissions:**
- **Super Admin:** Can update any user
- **Super Dev:** Can update users in assigned organizations
- **Organization Admin:** Can update users in their organization
- **User:** Can update their own profile (limited fields)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
from llmhub_generated.models.user_update import UserUpdate
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update = llmhub_generated.UserUpdate() # UserUpdate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update User
        api_response = api_instance.update_user_api_v1_users_user_id_patch(user_id, user_update, session_token=session_token)
        print("The response of UserManagementApi->update_user_api_v1_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->update_user_api_v1_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **update_user_api_v1_users_user_id_patch_0**
> UserResponse update_user_api_v1_users_user_id_patch_0(user_id, user_update, session_token=session_token)

Update User

Update user information

**Permissions:**
- **Super Admin:** Can update any user
- **Super Dev:** Can update users in assigned organizations
- **Organization Admin:** Can update users in their organization
- **User:** Can update their own profile (limited fields)

### Example

* Bearer Authentication (HTTPBearer):

```python
import llmhub_generated
from llmhub_generated.models.user_response import UserResponse
from llmhub_generated.models.user_update import UserUpdate
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
    api_instance = llmhub_generated.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update = llmhub_generated.UserUpdate() # UserUpdate | 
    session_token = 'session_token_example' # str |  (optional)

    try:
        # Update User
        api_response = api_instance.update_user_api_v1_users_user_id_patch_0(user_id, user_update, session_token=session_token)
        print("The response of UserManagementApi->update_user_api_v1_users_user_id_patch_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->update_user_api_v1_users_user_id_patch_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 
 **session_token** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

