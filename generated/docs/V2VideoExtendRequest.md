# V2VideoExtendRequest

Extend video duration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**video_url** | **str** | URL of source video | 
**extend_duration** | **int** | Additional seconds to add | 

## Example

```python
from llmhub_generated.models.v2_video_extend_request import V2VideoExtendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VideoExtendRequest from a JSON string
v2_video_extend_request_instance = V2VideoExtendRequest.from_json(json)
# print the JSON string representation of the object
print(V2VideoExtendRequest.to_json())

# convert the object into a dict
v2_video_extend_request_dict = v2_video_extend_request_instance.to_dict()
# create an instance of V2VideoExtendRequest from a dict
v2_video_extend_request_from_dict = V2VideoExtendRequest.from_dict(v2_video_extend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


