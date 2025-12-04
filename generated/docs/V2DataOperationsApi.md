# llmhub_generated.V2DataOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_embeddings_api_v2_data_embed_post**](V2DataOperationsApi.md#generate_embeddings_api_v2_data_embed_post) | **POST** /api/v2/data/embed | Generate Embeddings
[**rerank_documents_api_v2_data_rerank_post**](V2DataOperationsApi.md#rerank_documents_api_v2_data_rerank_post) | **POST** /api/v2/data/rerank | Rerank Documents


# **generate_embeddings_api_v2_data_embed_post**
> V2DataEmbedResponse generate_embeddings_api_v2_data_embed_post(x_api_key, v2_data_embed_request)

Generate Embeddings

Generate semantic embeddings for text(s)

Embeddings convert text into high-dimensional vectors for:
- Semantic search: Find similar documents
- RAG: Retrieve relevant context for LLMs
- Clustering: Group similar content
- Recommendation: Find related items

Supported providers:
- VoyageAI: Premium quality with 6 models (general + domain-specific)
- OpenAI: Cost-effective option (future integration)
- Cohere: Multilingual support (future integration)

Key features:
- Asymmetric embeddings: Optimize for document vs query
- Matryoshka embeddings: Flexible dimensions (256-2048)
- Batch processing: Up to 1000 texts per request
- Domain specialization: Code, finance, law models

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_data_embed_request import V2DataEmbedRequest
from llmhub_generated.models.v2_data_embed_response import V2DataEmbedResponse
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
    api_instance = llmhub_generated.V2DataOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_data_embed_request = llmhub_generated.V2DataEmbedRequest() # V2DataEmbedRequest | 

    try:
        # Generate Embeddings
        api_response = api_instance.generate_embeddings_api_v2_data_embed_post(x_api_key, v2_data_embed_request)
        print("The response of V2DataOperationsApi->generate_embeddings_api_v2_data_embed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DataOperationsApi->generate_embeddings_api_v2_data_embed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_data_embed_request** | [**V2DataEmbedRequest**](V2DataEmbedRequest.md)|  | 

### Return type

[**V2DataEmbedResponse**](V2DataEmbedResponse.md)

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

# **rerank_documents_api_v2_data_rerank_post**
> V2DataRerankResponse rerank_documents_api_v2_data_rerank_post(x_api_key, v2_data_rerank_request)

Rerank Documents

Rerank documents by relevance to a query

Reranking is a second-stage refinement for search results:
1. **First stage**: Embedding-based search (fast, ~1000 docs → top 100)
2. **Second stage**: Reranker (accurate, top 100 → best 10)

Why rerank?
- Embeddings provide fast approximate search
- Rerankers jointly process query+document for precise scoring
- Typical improvement: 15-30% accuracy boost

Workflow:
1. Use embeddings to retrieve ~100 candidates
2. Use reranker to refine to top 10-20 most relevant
3. Present refined results to user or LLM

Supported providers:
- VoyageAI: 2 models (rerank-2.5, rerank-2.5-lite)
- Cohere: English and multilingual (future integration)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_data_rerank_request import V2DataRerankRequest
from llmhub_generated.models.v2_data_rerank_response import V2DataRerankResponse
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
    api_instance = llmhub_generated.V2DataOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_data_rerank_request = llmhub_generated.V2DataRerankRequest() # V2DataRerankRequest | 

    try:
        # Rerank Documents
        api_response = api_instance.rerank_documents_api_v2_data_rerank_post(x_api_key, v2_data_rerank_request)
        print("The response of V2DataOperationsApi->rerank_documents_api_v2_data_rerank_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2DataOperationsApi->rerank_documents_api_v2_data_rerank_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_data_rerank_request** | [**V2DataRerankRequest**](V2DataRerankRequest.md)|  | 

### Return type

[**V2DataRerankResponse**](V2DataRerankResponse.md)

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

