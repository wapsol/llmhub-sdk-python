# V2VideoDescribeRequest

Generate description of video contents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**video_url** | **str** | URL of video to describe | 
**detail_level** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_video_describe_request import V2VideoDescribeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VideoDescribeRequest from a JSON string
v2_video_describe_request_instance = V2VideoDescribeRequest.from_json(json)
# print the JSON string representation of the object
print(V2VideoDescribeRequest.to_json())

# convert the object into a dict
v2_video_describe_request_dict = v2_video_describe_request_instance.to_dict()
# create an instance of V2VideoDescribeRequest from a dict
v2_video_describe_request_from_dict = V2VideoDescribeRequest.from_dict(v2_video_describe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


