# ShareProjectRequest

Request to share a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | **str** | Visibility: &#39;public&#39; or &#39;private&#39; | [optional] [default to 'public']

## Example

```python
from llmhub_generated.models.share_project_request import ShareProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareProjectRequest from a JSON string
share_project_request_instance = ShareProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ShareProjectRequest.to_json())

# convert the object into a dict
share_project_request_dict = share_project_request_instance.to_dict()
# create an instance of ShareProjectRequest from a dict
share_project_request_from_dict = ShareProjectRequest.from_dict(share_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


