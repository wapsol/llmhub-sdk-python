# V2DataRerankRequest

Rerank documents by relevance to a query  Reranking is a second-stage refinement for search results: 1. First stage: Fast embedding-based search (retrieve ~100 candidates) 2. Second stage: Reranker scores each candidate (refine to top 10)  Provides more accurate relevance scores than embeddings alone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**query** | **str** | Search query | 
**documents** | **List[str]** | List of documents to rank by relevance | 
**top_k** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_data_rerank_request import V2DataRerankRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DataRerankRequest from a JSON string
v2_data_rerank_request_instance = V2DataRerankRequest.from_json(json)
# print the JSON string representation of the object
print(V2DataRerankRequest.to_json())

# convert the object into a dict
v2_data_rerank_request_dict = v2_data_rerank_request_instance.to_dict()
# create an instance of V2DataRerankRequest from a dict
v2_data_rerank_request_from_dict = V2DataRerankRequest.from_dict(v2_data_rerank_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


