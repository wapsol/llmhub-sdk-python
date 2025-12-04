# V2TextExpandRequest

Expand brief text into detailed content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**target_length** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_expand_request import V2TextExpandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextExpandRequest from a JSON string
v2_text_expand_request_instance = V2TextExpandRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextExpandRequest.to_json())

# convert the object into a dict
v2_text_expand_request_dict = v2_text_expand_request_instance.to_dict()
# create an instance of V2TextExpandRequest from a dict
v2_text_expand_request_from_dict = V2TextExpandRequest.from_dict(v2_text_expand_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


