# AdminSetPasswordResponse

Response schema for admin password change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**user_id** | **str** |  | 
**sessions_invalidated** | **int** | Number of sessions invalidated | 

## Example

```python
from llmhub_generated.models.admin_set_password_response import AdminSetPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetPasswordResponse from a JSON string
admin_set_password_response_instance = AdminSetPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(AdminSetPasswordResponse.to_json())

# convert the object into a dict
admin_set_password_response_dict = admin_set_password_response_instance.to_dict()
# create an instance of AdminSetPasswordResponse from a dict
admin_set_password_response_from_dict = AdminSetPasswordResponse.from_dict(admin_set_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


