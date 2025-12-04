# AdminSetPasswordRequest

Schema for admin-initiated password change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** | New password for the user | 
**send_email** | **bool** | Whether to send email notification to user | [optional] [default to True]

## Example

```python
from llmhub_generated.models.admin_set_password_request import AdminSetPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetPasswordRequest from a JSON string
admin_set_password_request_instance = AdminSetPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(AdminSetPasswordRequest.to_json())

# convert the object into a dict
admin_set_password_request_dict = admin_set_password_request_instance.to_dict()
# create an instance of AdminSetPasswordRequest from a dict
admin_set_password_request_from_dict = AdminSetPasswordRequest.from_dict(admin_set_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


