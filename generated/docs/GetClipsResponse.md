# GetClipsResponse

Response with project clips

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**status** | **str** |  | 
**clips** | [**List[ClipData]**](ClipData.md) |  | 
**total_clips** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from llmhub_generated.models.get_clips_response import GetClipsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClipsResponse from a JSON string
get_clips_response_instance = GetClipsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClipsResponse.to_json())

# convert the object into a dict
get_clips_response_dict = get_clips_response_instance.to_dict()
# create an instance of GetClipsResponse from a dict
get_clips_response_from_dict = GetClipsResponse.from_dict(get_clips_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


