# V2PerspectiveAnalyzeRequest

Analyze text for toxicity and harmful content using Google Perspective API  Attributes analyzed: - TOXICITY: Overall toxicity likelihood - SEVERE_TOXICITY: Very hateful, aggressive content - IDENTITY_ATTACK: Negative comments about identity/ethnicity - INSULT: Insulting or inflammatory language - PROFANITY: Swear words and obscene language - THREAT: Threats of violence or harm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** | Text to analyze for toxicity | 
**requested_attributes** | **List[str]** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**do_not_store** | **bool** | Don&#39;t store comment for future research (privacy mode) | [optional] [default to True]
**span_annotations** | **bool** | Return per-sentence toxicity scores | [optional] [default to False]

## Example

```python
from llmhub_generated.models.v2_perspective_analyze_request import V2PerspectiveAnalyzeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2PerspectiveAnalyzeRequest from a JSON string
v2_perspective_analyze_request_instance = V2PerspectiveAnalyzeRequest.from_json(json)
# print the JSON string representation of the object
print(V2PerspectiveAnalyzeRequest.to_json())

# convert the object into a dict
v2_perspective_analyze_request_dict = v2_perspective_analyze_request_instance.to_dict()
# create an instance of V2PerspectiveAnalyzeRequest from a dict
v2_perspective_analyze_request_from_dict = V2PerspectiveAnalyzeRequest.from_dict(v2_perspective_analyze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


