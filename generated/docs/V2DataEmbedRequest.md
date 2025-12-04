# V2DataEmbedRequest

Generate semantic embeddings for text(s)  Embeddings convert text into numerical vectors for semantic search, RAG, clustering, and similarity calculations.  Supports: - Single text or batch processing (up to 1000 texts) - Asymmetric embeddings (document vs query optimization) - Matryoshka embeddings (flexible dimensions) - Domain-specific models (code, finance, law)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**texts** | [**Texts**](Texts.md) |  | 
**input_type** | **str** |  | [optional] 
**output_dimension** | **int** |  | [optional] 
**truncation** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_data_embed_request import V2DataEmbedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DataEmbedRequest from a JSON string
v2_data_embed_request_instance = V2DataEmbedRequest.from_json(json)
# print the JSON string representation of the object
print(V2DataEmbedRequest.to_json())

# convert the object into a dict
v2_data_embed_request_dict = v2_data_embed_request_instance.to_dict()
# create an instance of V2DataEmbedRequest from a dict
v2_data_embed_request_from_dict = V2DataEmbedRequest.from_dict(v2_data_embed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


