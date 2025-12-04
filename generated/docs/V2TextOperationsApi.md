# llmhub_generated.V2TextOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_text_api_v2_text_analyze_post**](V2TextOperationsApi.md#analyze_text_api_v2_text_analyze_post) | **POST** /api/v2/text/analyze | Analyze Text
[**classify_text_api_v2_text_classify_post**](V2TextOperationsApi.md#classify_text_api_v2_text_classify_post) | **POST** /api/v2/text/classify | Classify Text
[**compare_texts_api_v2_text_compare_post**](V2TextOperationsApi.md#compare_texts_api_v2_text_compare_post) | **POST** /api/v2/text/compare | Compare Texts
[**condense_text_api_v2_text_condense_post**](V2TextOperationsApi.md#condense_text_api_v2_text_condense_post) | **POST** /api/v2/text/condense | Condense Text
[**expand_text_api_v2_text_expand_post**](V2TextOperationsApi.md#expand_text_api_v2_text_expand_post) | **POST** /api/v2/text/expand | Expand Text
[**extract_from_text_api_v2_text_extract_post**](V2TextOperationsApi.md#extract_from_text_api_v2_text_extract_post) | **POST** /api/v2/text/extract | Extract From Text
[**generate_text_api_v2_text_generate_post**](V2TextOperationsApi.md#generate_text_api_v2_text_generate_post) | **POST** /api/v2/text/generate | Generate Text
[**rewrite_text_api_v2_text_rewrite_post**](V2TextOperationsApi.md#rewrite_text_api_v2_text_rewrite_post) | **POST** /api/v2/text/rewrite | Rewrite Text
[**summarize_text_api_v2_text_summarize_post**](V2TextOperationsApi.md#summarize_text_api_v2_text_summarize_post) | **POST** /api/v2/text/summarize | Summarize Text
[**translate_text_api_v2_text_translate_post**](V2TextOperationsApi.md#translate_text_api_v2_text_translate_post) | **POST** /api/v2/text/translate | Translate Text


# **analyze_text_api_v2_text_analyze_post**
> V2BaseResponse analyze_text_api_v2_text_analyze_post(x_api_key, v2_text_analyze_request)

Analyze Text

Analyze text (sentiment, tone, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_analyze_request import V2TextAnalyzeRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_analyze_request = llmhub_generated.V2TextAnalyzeRequest() # V2TextAnalyzeRequest | 

    try:
        # Analyze Text
        api_response = api_instance.analyze_text_api_v2_text_analyze_post(x_api_key, v2_text_analyze_request)
        print("The response of V2TextOperationsApi->analyze_text_api_v2_text_analyze_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->analyze_text_api_v2_text_analyze_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_analyze_request** | [**V2TextAnalyzeRequest**](V2TextAnalyzeRequest.md)|  | 

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

# **classify_text_api_v2_text_classify_post**
> V2BaseResponse classify_text_api_v2_text_classify_post(x_api_key, v2_text_classify_request)

Classify Text

Classify text into categories

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_classify_request import V2TextClassifyRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_classify_request = llmhub_generated.V2TextClassifyRequest() # V2TextClassifyRequest | 

    try:
        # Classify Text
        api_response = api_instance.classify_text_api_v2_text_classify_post(x_api_key, v2_text_classify_request)
        print("The response of V2TextOperationsApi->classify_text_api_v2_text_classify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->classify_text_api_v2_text_classify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_classify_request** | [**V2TextClassifyRequest**](V2TextClassifyRequest.md)|  | 

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

# **compare_texts_api_v2_text_compare_post**
> V2BaseResponse compare_texts_api_v2_text_compare_post(x_api_key, v2_text_compare_request)

Compare Texts

Compare multiple texts

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_compare_request import V2TextCompareRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_compare_request = llmhub_generated.V2TextCompareRequest() # V2TextCompareRequest | 

    try:
        # Compare Texts
        api_response = api_instance.compare_texts_api_v2_text_compare_post(x_api_key, v2_text_compare_request)
        print("The response of V2TextOperationsApi->compare_texts_api_v2_text_compare_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->compare_texts_api_v2_text_compare_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_compare_request** | [**V2TextCompareRequest**](V2TextCompareRequest.md)|  | 

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

# **condense_text_api_v2_text_condense_post**
> V2BaseResponse condense_text_api_v2_text_condense_post(x_api_key, v2_text_condense_request)

Condense Text

Condense long text to key points

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_condense_request import V2TextCondenseRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_condense_request = llmhub_generated.V2TextCondenseRequest() # V2TextCondenseRequest | 

    try:
        # Condense Text
        api_response = api_instance.condense_text_api_v2_text_condense_post(x_api_key, v2_text_condense_request)
        print("The response of V2TextOperationsApi->condense_text_api_v2_text_condense_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->condense_text_api_v2_text_condense_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_condense_request** | [**V2TextCondenseRequest**](V2TextCondenseRequest.md)|  | 

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

# **expand_text_api_v2_text_expand_post**
> V2BaseResponse expand_text_api_v2_text_expand_post(x_api_key, v2_text_expand_request)

Expand Text

Expand brief text into detailed content

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_expand_request import V2TextExpandRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_expand_request = llmhub_generated.V2TextExpandRequest() # V2TextExpandRequest | 

    try:
        # Expand Text
        api_response = api_instance.expand_text_api_v2_text_expand_post(x_api_key, v2_text_expand_request)
        print("The response of V2TextOperationsApi->expand_text_api_v2_text_expand_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->expand_text_api_v2_text_expand_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_expand_request** | [**V2TextExpandRequest**](V2TextExpandRequest.md)|  | 

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

# **extract_from_text_api_v2_text_extract_post**
> V2BaseResponse extract_from_text_api_v2_text_extract_post(x_api_key, v2_text_extract_request)

Extract From Text

Extract entities, keywords, or structured data

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_extract_request import V2TextExtractRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_extract_request = llmhub_generated.V2TextExtractRequest() # V2TextExtractRequest | 

    try:
        # Extract From Text
        api_response = api_instance.extract_from_text_api_v2_text_extract_post(x_api_key, v2_text_extract_request)
        print("The response of V2TextOperationsApi->extract_from_text_api_v2_text_extract_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->extract_from_text_api_v2_text_extract_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_extract_request** | [**V2TextExtractRequest**](V2TextExtractRequest.md)|  | 

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

# **generate_text_api_v2_text_generate_post**
> V2BaseResponse generate_text_api_v2_text_generate_post(x_api_key, v2_text_generate_request)

Generate Text

Generate text content from prompt

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_generate_request import V2TextGenerateRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_generate_request = llmhub_generated.V2TextGenerateRequest() # V2TextGenerateRequest | 

    try:
        # Generate Text
        api_response = api_instance.generate_text_api_v2_text_generate_post(x_api_key, v2_text_generate_request)
        print("The response of V2TextOperationsApi->generate_text_api_v2_text_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->generate_text_api_v2_text_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_generate_request** | [**V2TextGenerateRequest**](V2TextGenerateRequest.md)|  | 

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

# **rewrite_text_api_v2_text_rewrite_post**
> V2BaseResponse rewrite_text_api_v2_text_rewrite_post(x_api_key, v2_text_rewrite_request)

Rewrite Text

Rewrite/paraphrase text

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_rewrite_request import V2TextRewriteRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_rewrite_request = llmhub_generated.V2TextRewriteRequest() # V2TextRewriteRequest | 

    try:
        # Rewrite Text
        api_response = api_instance.rewrite_text_api_v2_text_rewrite_post(x_api_key, v2_text_rewrite_request)
        print("The response of V2TextOperationsApi->rewrite_text_api_v2_text_rewrite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->rewrite_text_api_v2_text_rewrite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_rewrite_request** | [**V2TextRewriteRequest**](V2TextRewriteRequest.md)|  | 

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

# **summarize_text_api_v2_text_summarize_post**
> V2BaseResponse summarize_text_api_v2_text_summarize_post(x_api_key, v2_text_summarize_request)

Summarize Text

Summarize long text

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_summarize_request import V2TextSummarizeRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_summarize_request = llmhub_generated.V2TextSummarizeRequest() # V2TextSummarizeRequest | 

    try:
        # Summarize Text
        api_response = api_instance.summarize_text_api_v2_text_summarize_post(x_api_key, v2_text_summarize_request)
        print("The response of V2TextOperationsApi->summarize_text_api_v2_text_summarize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->summarize_text_api_v2_text_summarize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_summarize_request** | [**V2TextSummarizeRequest**](V2TextSummarizeRequest.md)|  | 

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

# **translate_text_api_v2_text_translate_post**
> V2BaseResponse translate_text_api_v2_text_translate_post(x_api_key, v2_text_translate_request)

Translate Text

Translate text between languages

Supports two modes:
1. Simple text translation: Single text to single language
2. Structured content translation: Multiple fields to multiple languages

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.models.v2_text_translate_request import V2TextTranslateRequest
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
    api_instance = llmhub_generated.V2TextOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_text_translate_request = llmhub_generated.V2TextTranslateRequest() # V2TextTranslateRequest | 

    try:
        # Translate Text
        api_response = api_instance.translate_text_api_v2_text_translate_post(x_api_key, v2_text_translate_request)
        print("The response of V2TextOperationsApi->translate_text_api_v2_text_translate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2TextOperationsApi->translate_text_api_v2_text_translate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_text_translate_request** | [**V2TextTranslateRequest**](V2TextTranslateRequest.md)|  | 

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

