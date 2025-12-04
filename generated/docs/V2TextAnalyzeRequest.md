# V2TextAnalyzeRequest

Analyze text (sentiment, tone, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**analysis_types** | **List[str]** | Types of analysis to perform | [optional] [default to [sentiment, tone]]

## Example

```python
from llmhub_generated.models.v2_text_analyze_request import V2TextAnalyzeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextAnalyzeRequest from a JSON string
v2_text_analyze_request_instance = V2TextAnalyzeRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextAnalyzeRequest.to_json())

# convert the object into a dict
v2_text_analyze_request_dict = v2_text_analyze_request_instance.to_dict()
# create an instance of V2TextAnalyzeRequest from a dict
v2_text_analyze_request_from_dict = V2TextAnalyzeRequest.from_dict(v2_text_analyze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


