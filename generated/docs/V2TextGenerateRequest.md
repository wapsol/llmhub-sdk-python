# V2TextGenerateRequest

Generate text content from prompt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**prompt** | **str** | Text generation prompt | 
**system_prompt** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_generate_request import V2TextGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextGenerateRequest from a JSON string
v2_text_generate_request_instance = V2TextGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextGenerateRequest.to_json())

# convert the object into a dict
v2_text_generate_request_dict = v2_text_generate_request_instance.to_dict()
# create an instance of V2TextGenerateRequest from a dict
v2_text_generate_request_from_dict = V2TextGenerateRequest.from_dict(v2_text_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


