# V2TextCompareRequest

Compare multiple texts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**texts** | **List[str]** | Texts to compare | 
**comparison_aspects** | **List[str]** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_compare_request import V2TextCompareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextCompareRequest from a JSON string
v2_text_compare_request_instance = V2TextCompareRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextCompareRequest.to_json())

# convert the object into a dict
v2_text_compare_request_dict = v2_text_compare_request_instance.to_dict()
# create an instance of V2TextCompareRequest from a dict
v2_text_compare_request_from_dict = V2TextCompareRequest.from_dict(v2_text_compare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


