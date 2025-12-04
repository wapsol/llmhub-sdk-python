# V2VideoRemixRequest

Remix/edit existing video

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**video_url** | **str** | URL of source video | 
**instructions** | **str** | Editing instructions | 

## Example

```python
from llmhub_generated.models.v2_video_remix_request import V2VideoRemixRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VideoRemixRequest from a JSON string
v2_video_remix_request_instance = V2VideoRemixRequest.from_json(json)
# print the JSON string representation of the object
print(V2VideoRemixRequest.to_json())

# convert the object into a dict
v2_video_remix_request_dict = v2_video_remix_request_instance.to_dict()
# create an instance of V2VideoRemixRequest from a dict
v2_video_remix_request_from_dict = V2VideoRemixRequest.from_dict(v2_video_remix_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


