# ClipData

Individual clip data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clip_id** | **str** |  | 
**title** | **str** |  | 
**duration_seconds** | **int** |  | 
**thumbnail_url** | **str** |  | [optional] 
**video_url** | **str** |  | [optional] 
**virality_score** | **float** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 

## Example

```python
from llmhub_generated.models.clip_data import ClipData

# TODO update the JSON string below
json = "{}"
# create an instance of ClipData from a JSON string
clip_data_instance = ClipData.from_json(json)
# print the JSON string representation of the object
print(ClipData.to_json())

# convert the object into a dict
clip_data_dict = clip_data_instance.to_dict()
# create an instance of ClipData from a dict
clip_data_from_dict = ClipData.from_dict(clip_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


