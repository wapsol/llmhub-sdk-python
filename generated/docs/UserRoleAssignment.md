# UserRoleAssignment

Schema for assigning roles to users (user_id comes from URL path)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | [**RoleEnum**](RoleEnum.md) | Role to assign | 

## Example

```python
from llmhub_generated.models.user_role_assignment import UserRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleAssignment from a JSON string
user_role_assignment_instance = UserRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(UserRoleAssignment.to_json())

# convert the object into a dict
user_role_assignment_dict = user_role_assignment_instance.to_dict()
# create an instance of UserRoleAssignment from a dict
user_role_assignment_from_dict = UserRoleAssignment.from_dict(user_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


