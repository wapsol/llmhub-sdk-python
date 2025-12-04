# llmhub_generated.V2EmbeddingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_embeddings_api_v2_embeddings_generate_post**](V2EmbeddingsApi.md#generate_embeddings_api_v2_embeddings_generate_post) | **POST** /api/v2/embeddings/generate | Generate Embeddings


# **generate_embeddings_api_v2_embeddings_generate_post**
> V2EmbeddingsResponse generate_embeddings_api_v2_embeddings_generate_post(x_api_key, v2_embeddings_request)

Generate Embeddings

Generate vector embeddings for RAG/semantic search

Supports:
- OpenAI: text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002
- Cohere: embed-english-v3.0, embed-multilingual-v3.0, embed-english-light-v3.0

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_embeddings_request import V2EmbeddingsRequest
from llmhub_generated.models.v2_embeddings_response import V2EmbeddingsResponse
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
    api_instance = llmhub_generated.V2EmbeddingsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_embeddings_request = llmhub_generated.V2EmbeddingsRequest() # V2EmbeddingsRequest | 

    try:
        # Generate Embeddings
        api_response = api_instance.generate_embeddings_api_v2_embeddings_generate_post(x_api_key, v2_embeddings_request)
        print("The response of V2EmbeddingsApi->generate_embeddings_api_v2_embeddings_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2EmbeddingsApi->generate_embeddings_api_v2_embeddings_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_embeddings_request** | [**V2EmbeddingsRequest**](V2EmbeddingsRequest.md)|  | 

### Return type

[**V2EmbeddingsResponse**](V2EmbeddingsResponse.md)

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

