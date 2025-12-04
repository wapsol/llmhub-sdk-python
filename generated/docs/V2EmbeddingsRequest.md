# V2EmbeddingsRequest

Generate vector embeddings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**texts** | **List[str]** | Texts to embed | 
**embedding_model** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_embeddings_request import V2EmbeddingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2EmbeddingsRequest from a JSON string
v2_embeddings_request_instance = V2EmbeddingsRequest.from_json(json)
# print the JSON string representation of the object
print(V2EmbeddingsRequest.to_json())

# convert the object into a dict
v2_embeddings_request_dict = v2_embeddings_request_instance.to_dict()
# create an instance of V2EmbeddingsRequest from a dict
v2_embeddings_request_from_dict = V2EmbeddingsRequest.from_dict(v2_embeddings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


