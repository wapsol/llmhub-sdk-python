# V2TextExtractRequest

Extract entities, keywords, or structured data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**extract_types** | **List[str]** | What to extract | [optional] [default to [entities, keywords]]

## Example

```python
from llmhub_generated.models.v2_text_extract_request import V2TextExtractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextExtractRequest from a JSON string
v2_text_extract_request_instance = V2TextExtractRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextExtractRequest.to_json())

# convert the object into a dict
v2_text_extract_request_dict = v2_text_extract_request_instance.to_dict()
# create an instance of V2TextExtractRequest from a dict
v2_text_extract_request_from_dict = V2TextExtractRequest.from_dict(v2_text_extract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


