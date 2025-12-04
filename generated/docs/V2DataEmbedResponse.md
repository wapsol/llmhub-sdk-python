# V2DataEmbedResponse

Response for embedding generation

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
**embeddings** | **List[List[float]]** | List of embedding vectors (one per input text) | 
**dimensions** | **int** | Embedding vector dimensions | 
**num_embeddings** | **int** | Number of embeddings generated | 

## Example

```python
from llmhub_generated.models.v2_data_embed_response import V2DataEmbedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2DataEmbedResponse from a JSON string
v2_data_embed_response_instance = V2DataEmbedResponse.from_json(json)
# print the JSON string representation of the object
print(V2DataEmbedResponse.to_json())

# convert the object into a dict
v2_data_embed_response_dict = v2_data_embed_response_instance.to_dict()
# create an instance of V2DataEmbedResponse from a dict
v2_data_embed_response_from_dict = V2DataEmbedResponse.from_dict(v2_data_embed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


