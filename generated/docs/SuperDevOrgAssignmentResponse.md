# SuperDevOrgAssignmentResponse

Response schema for organization assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **int** |  | 
**super_dev_user_id** | **str** |  | 
**org_id** | **int** |  | 
**org_name** | **str** |  | [optional] 
**super_dev_name** | **str** |  | [optional] 
**super_dev_email** | **str** |  | [optional] 
**assigned_at** | **datetime** |  | 
**assigned_by** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**notes** | **str** |  | [optional] 
**commission_percentage** | **float** |  | [optional] 

## Example

```python
from llmhub_generated.models.super_dev_org_assignment_response import SuperDevOrgAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperDevOrgAssignmentResponse from a JSON string
super_dev_org_assignment_response_instance = SuperDevOrgAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(SuperDevOrgAssignmentResponse.to_json())

# convert the object into a dict
super_dev_org_assignment_response_dict = super_dev_org_assignment_response_instance.to_dict()
# create an instance of SuperDevOrgAssignmentResponse from a dict
super_dev_org_assignment_response_from_dict = SuperDevOrgAssignmentResponse.from_dict(super_dev_org_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


