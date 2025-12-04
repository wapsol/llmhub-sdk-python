# ShareProjectResponse

Response after updating project visibility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**visibility** | **str** |  | 
**share_url** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from llmhub_generated.models.share_project_response import ShareProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProjectResponse from a JSON string
share_project_response_instance = ShareProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ShareProjectResponse.to_json())

# convert the object into a dict
share_project_response_dict = share_project_response_instance.to_dict()
# create an instance of ShareProjectResponse from a dict
share_project_response_from_dict = ShareProjectResponse.from_dict(share_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


