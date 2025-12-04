# llmhub_generated.V2DocumentOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify_document_api_v2_document_classify_post**](V2DocumentOperationsApi.md#classify_document_api_v2_document_classify_post) | **POST** /api/v2/document/classify | Classify Document
[**compare_documents_api_v2_document_compare_post**](V2DocumentOperationsApi.md#compare_documents_api_v2_document_compare_post) | **POST** /api/v2/document/compare | Compare Documents
[**extract_from_document_api_v2_document_extract_post**](V2DocumentOperationsApi.md#extract_from_document_api_v2_document_extract_post) | **POST** /api/v2/document/extract | Extract From Document
[**generate_document_api_v2_document_generate_post**](V2DocumentOperationsApi.md#generate_document_api_v2_document_generate_post) | **POST** /api/v2/document/generate | Generate Document
[**parse_document_api_v2_document_parse_post**](V2DocumentOperationsApi.md#parse_document_api_v2_document_parse_post) | **POST** /api/v2/document/parse | Parse Document
[**structure_document_api_v2_document_structure_post**](V2DocumentOperationsApi.md#structure_document_api_v2_document_structure_post) | **POST** /api/v2/document/structure | Structure Document


# **classify_document_api_v2_document_classify_post**
> V2BaseResponse classify_document_api_v2_document_classify_post(x_api_key, v2_document_classify_request)

Classify Document

Classify document type/category

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_classify_request import V2DocumentClassifyRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_classify_request = llmhub_generated.V2DocumentClassifyRequest() # V2DocumentClassifyRequest | 

    try:
        # Classify Document
        api_response = api_instance.classify_document_api_v2_document_classify_post(x_api_key, v2_document_classify_request)
        print("The response of V2DocumentOperationsApi->classify_document_api_v2_document_classify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->classify_document_api_v2_document_classify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_classify_request** | [**V2DocumentClassifyRequest**](V2DocumentClassifyRequest.md)|  | 

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

# **compare_documents_api_v2_document_compare_post**
> V2BaseResponse compare_documents_api_v2_document_compare_post(x_api_key, v2_document_compare_request)

Compare Documents

Compare multiple documents

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_compare_request import V2DocumentCompareRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_compare_request = llmhub_generated.V2DocumentCompareRequest() # V2DocumentCompareRequest | 

    try:
        # Compare Documents
        api_response = api_instance.compare_documents_api_v2_document_compare_post(x_api_key, v2_document_compare_request)
        print("The response of V2DocumentOperationsApi->compare_documents_api_v2_document_compare_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->compare_documents_api_v2_document_compare_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_compare_request** | [**V2DocumentCompareRequest**](V2DocumentCompareRequest.md)|  | 

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

# **extract_from_document_api_v2_document_extract_post**
> V2BaseResponse extract_from_document_api_v2_document_extract_post(x_api_key, v2_document_extract_request)

Extract From Document

Extract specific data from documents (invoices, contracts, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_extract_request import V2DocumentExtractRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_extract_request = llmhub_generated.V2DocumentExtractRequest() # V2DocumentExtractRequest | 

    try:
        # Extract From Document
        api_response = api_instance.extract_from_document_api_v2_document_extract_post(x_api_key, v2_document_extract_request)
        print("The response of V2DocumentOperationsApi->extract_from_document_api_v2_document_extract_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->extract_from_document_api_v2_document_extract_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_extract_request** | [**V2DocumentExtractRequest**](V2DocumentExtractRequest.md)|  | 

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

# **generate_document_api_v2_document_generate_post**
> V2BaseResponse generate_document_api_v2_document_generate_post(x_api_key, v2_document_generate_request)

Generate Document

Generate complete documents (reports, contracts, whitepapers, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_generate_request import V2DocumentGenerateRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_generate_request = llmhub_generated.V2DocumentGenerateRequest() # V2DocumentGenerateRequest | 

    try:
        # Generate Document
        api_response = api_instance.generate_document_api_v2_document_generate_post(x_api_key, v2_document_generate_request)
        print("The response of V2DocumentOperationsApi->generate_document_api_v2_document_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->generate_document_api_v2_document_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_generate_request** | [**V2DocumentGenerateRequest**](V2DocumentGenerateRequest.md)|  | 

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

# **parse_document_api_v2_document_parse_post**
> V2BaseResponse parse_document_api_v2_document_parse_post(x_api_key, v2_document_parse_request)

Parse Document

Parse document structure (headings, sections, tables)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_parse_request import V2DocumentParseRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_parse_request = llmhub_generated.V2DocumentParseRequest() # V2DocumentParseRequest | 

    try:
        # Parse Document
        api_response = api_instance.parse_document_api_v2_document_parse_post(x_api_key, v2_document_parse_request)
        print("The response of V2DocumentOperationsApi->parse_document_api_v2_document_parse_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->parse_document_api_v2_document_parse_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_parse_request** | [**V2DocumentParseRequest**](V2DocumentParseRequest.md)|  | 

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

# **structure_document_api_v2_document_structure_post**
> V2BaseResponse structure_document_api_v2_document_structure_post(x_api_key, v2_document_structure_request)

Structure Document

Convert unstructured documents to structured format

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_document_structure_request import V2DocumentStructureRequest
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
    api_instance = llmhub_generated.V2DocumentOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_document_structure_request = llmhub_generated.V2DocumentStructureRequest() # V2DocumentStructureRequest | 

    try:
        # Structure Document
        api_response = api_instance.structure_document_api_v2_document_structure_post(x_api_key, v2_document_structure_request)
        print("The response of V2DocumentOperationsApi->structure_document_api_v2_document_structure_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DocumentOperationsApi->structure_document_api_v2_document_structure_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_document_structure_request** | [**V2DocumentStructureRequest**](V2DocumentStructureRequest.md)|  | 

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

