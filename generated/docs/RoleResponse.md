# RoleResponse

Response schema for role data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Unique role name | 
**display_name** | **str** | Human-readable role name | 
**description** | **str** |  | [optional] 
**role_id** | **int** |  | 
**permissions** | **List[str]** |  | 
**is_system_role** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print(RoleResponse.to_json())

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_from_dict = RoleResponse.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


