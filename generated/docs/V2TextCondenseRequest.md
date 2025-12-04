# V2TextCondenseRequest

Condense long text to key points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**num_points** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_condense_request import V2TextCondenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextCondenseRequest from a JSON string
v2_text_condense_request_instance = V2TextCondenseRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextCondenseRequest.to_json())

# convert the object into a dict
v2_text_condense_request_dict = v2_text_condense_request_instance.to_dict()
# create an instance of V2TextCondenseRequest from a dict
v2_text_condense_request_from_dict = V2TextCondenseRequest.from_dict(v2_text_condense_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


