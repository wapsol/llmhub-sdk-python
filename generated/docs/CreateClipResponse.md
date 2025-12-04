# CreateClipResponse

Response after creating clip project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique project identifier | 
**status** | **str** | Current processing status | 
**video_url** | **str** | Original video URL | 
**estimated_duration_minutes** | **int** |  | [optional] 
**credits_required** | **int** |  | [optional] 
**message** | **str** | Human-readable status message | 

## Example

```python
from llmhub_generated.models.create_clip_response import CreateClipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClipResponse from a JSON string
create_clip_response_instance = CreateClipResponse.from_json(json)
# print the JSON string representation of the object
print(CreateClipResponse.to_json())

# convert the object into a dict
create_clip_response_dict = create_clip_response_instance.to_dict()
# create an instance of CreateClipResponse from a dict
create_clip_response_from_dict = CreateClipResponse.from_dict(create_clip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


