# UnassignOrganizationRequest

Request to unassign organization from Super Dev

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_dev_user_id** | **str** |  | 
**org_id** | **int** |  | 

## Example

```python
from llmhub_generated.models.unassign_organization_request import UnassignOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignOrganizationRequest from a JSON string
unassign_organization_request_instance = UnassignOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(UnassignOrganizationRequest.to_json())

# convert the object into a dict
unassign_organization_request_dict = unassign_organization_request_instance.to_dict()
# create an instance of UnassignOrganizationRequest from a dict
unassign_organization_request_from_dict = UnassignOrganizationRequest.from_dict(unassign_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


