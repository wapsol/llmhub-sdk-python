# V2TextClassifyRequest

Classify text into categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**categories** | **List[str]** | List of possible categories | 

## Example

```python
from llmhub_generated.models.v2_text_classify_request import V2TextClassifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextClassifyRequest from a JSON string
v2_text_classify_request_instance = V2TextClassifyRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextClassifyRequest.to_json())

# convert the object into a dict
v2_text_classify_request_dict = v2_text_classify_request_instance.to_dict()
# create an instance of V2TextClassifyRequest from a dict
v2_text_classify_request_from_dict = V2TextClassifyRequest.from_dict(v2_text_classify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


