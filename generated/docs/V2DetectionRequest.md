# V2DetectionRequest

Detect specific content types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**content** | **str** | Content to analyze | 
**detection_types** | **List[str]** | PII, hate_speech, violence, etc. | 

## Example

```python
from llmhub_generated.models.v2_detection_request import V2DetectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DetectionRequest from a JSON string
v2_detection_request_instance = V2DetectionRequest.from_json(json)
# print the JSON string representation of the object
print(V2DetectionRequest.to_json())

# convert the object into a dict
v2_detection_request_dict = v2_detection_request_instance.to_dict()
# create an instance of V2DetectionRequest from a dict
v2_detection_request_from_dict = V2DetectionRequest.from_dict(v2_detection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


