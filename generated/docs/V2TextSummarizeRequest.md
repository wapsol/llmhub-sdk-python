# V2TextSummarizeRequest

Summarize long text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**summary_length** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_summarize_request import V2TextSummarizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextSummarizeRequest from a JSON string
v2_text_summarize_request_instance = V2TextSummarizeRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextSummarizeRequest.to_json())

# convert the object into a dict
v2_text_summarize_request_dict = v2_text_summarize_request_instance.to_dict()
# create an instance of V2TextSummarizeRequest from a dict
v2_text_summarize_request_from_dict = V2TextSummarizeRequest.from_dict(v2_text_summarize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


