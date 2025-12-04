# AdminGenerateResetLinkRequest

Schema for admin generating password reset link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_email** | **bool** | Whether to also send reset email to user | [optional] [default to False]

## Example

```python
from llmhub_generated.models.admin_generate_reset_link_request import AdminGenerateResetLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGenerateResetLinkRequest from a JSON string
admin_generate_reset_link_request_instance = AdminGenerateResetLinkRequest.from_json(json)
# print the JSON string representation of the object
print(AdminGenerateResetLinkRequest.to_json())

# convert the object into a dict
admin_generate_reset_link_request_dict = admin_generate_reset_link_request_instance.to_dict()
# create an instance of AdminGenerateResetLinkRequest from a dict
admin_generate_reset_link_request_from_dict = AdminGenerateResetLinkRequest.from_dict(admin_generate_reset_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


