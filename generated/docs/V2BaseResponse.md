# V2BaseResponse

Base response schema for all v2 endpoints

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

## Example

```python
from llmhub_generated.models.v2_base_response import V2BaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2BaseResponse from a JSON string
v2_base_response_instance = V2BaseResponse.from_json(json)
# print the JSON string representation of the object
print(V2BaseResponse.to_json())

# convert the object into a dict
v2_base_response_dict = v2_base_response_instance.to_dict()
# create an instance of V2BaseResponse from a dict
v2_base_response_from_dict = V2BaseResponse.from_dict(v2_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


