# V2VideoInterpolateRequest

Create smooth transitions between video frames

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**video_url** | **str** | URL of source video | 
**target_fps** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_video_interpolate_request import V2VideoInterpolateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VideoInterpolateRequest from a JSON string
v2_video_interpolate_request_instance = V2VideoInterpolateRequest.from_json(json)
# print the JSON string representation of the object
print(V2VideoInterpolateRequest.to_json())

# convert the object into a dict
v2_video_interpolate_request_dict = v2_video_interpolate_request_instance.to_dict()
# create an instance of V2VideoInterpolateRequest from a dict
v2_video_interpolate_request_from_dict = V2VideoInterpolateRequest.from_dict(v2_video_interpolate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


