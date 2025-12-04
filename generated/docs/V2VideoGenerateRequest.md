# V2VideoGenerateRequest

Generate video from text or images

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**prompt** | **str** | Video generation prompt | 
**prompt_image** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**aspect_ratio** | **str** |  | [optional] 
**include_audio** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_video_generate_request import V2VideoGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VideoGenerateRequest from a JSON string
v2_video_generate_request_instance = V2VideoGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(V2VideoGenerateRequest.to_json())

# convert the object into a dict
v2_video_generate_request_dict = v2_video_generate_request_instance.to_dict()
# create an instance of V2VideoGenerateRequest from a dict
v2_video_generate_request_from_dict = V2VideoGenerateRequest.from_dict(v2_video_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


