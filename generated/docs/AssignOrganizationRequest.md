# AssignOrganizationRequest

Request to assign organization to Super Dev

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_dev_user_id** | **str** |  | 
**org_id** | **int** |  | 
**commission_percentage** | **float** |  | 
**valid_from** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.assign_organization_request import AssignOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrganizationRequest from a JSON string
assign_organization_request_instance = AssignOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(AssignOrganizationRequest.to_json())

# convert the object into a dict
assign_organization_request_dict = assign_organization_request_instance.to_dict()
# create an instance of AssignOrganizationRequest from a dict
assign_organization_request_from_dict = AssignOrganizationRequest.from_dict(assign_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


