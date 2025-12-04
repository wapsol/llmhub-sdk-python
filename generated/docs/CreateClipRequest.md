# CreateClipRequest

Request to create video clips

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_url** | **str** | YouTube URL or direct video URL (MP4, MOV, WEBM) | 
**brand_template_id** | **str** |  | [optional] 
**model** | **str** | Processing model: clip-basic or clip-anything | [optional] [default to 'clip-basic']
**clip_durations** | **List[str]** |  | [optional] 
**genre** | **str** |  | [optional] 
**topic_keywords** | **List[str]** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.create_clip_request import CreateClipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClipRequest from a JSON string
create_clip_request_instance = CreateClipRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClipRequest.to_json())

# convert the object into a dict
create_clip_request_dict = create_clip_request_instance.to_dict()
# create an instance of CreateClipRequest from a dict
create_clip_request_from_dict = CreateClipRequest.from_dict(create_clip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


