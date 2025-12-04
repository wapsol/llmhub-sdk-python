# V2EmbeddingsResponse

Response for embeddings generation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**content** | **object** |  | 
**provider_used** | **str** |  | 
**model_used** | **str** |  | 
**tokens_used** | **int** |  | 
**cost_usd** | **float** |  | 
**generation_time_ms** | **int** |  | 
**log_id** | **str** |  | 
**embeddings** | **List[List[float]]** | Generated embedding vectors | 
**dimensions** | **int** | Embedding dimensions | 

## Example

```python
from llmhub_generated.models.v2_embeddings_response import V2EmbeddingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2EmbeddingsResponse from a JSON string
v2_embeddings_response_instance = V2EmbeddingsResponse.from_json(json)
# print the JSON string representation of the object
print(V2EmbeddingsResponse.to_json())

# convert the object into a dict
v2_embeddings_response_dict = v2_embeddings_response_instance.to_dict()
# create an instance of V2EmbeddingsResponse from a dict
v2_embeddings_response_from_dict = V2EmbeddingsResponse.from_dict(v2_embeddings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


