# AdminGenerateResetLinkResponse

Response schema for admin reset link generation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**reset_link** | **str** | Full password reset URL with token | 
**token** | **str** | Reset token (for reference) | 
**expires_at** | **datetime** | Token expiration time | 
**user_id** | **str** |  | 
**email_sent** | **bool** | Whether email was sent to user | 

## Example

```python
from llmhub_generated.models.admin_generate_reset_link_response import AdminGenerateResetLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGenerateResetLinkResponse from a JSON string
admin_generate_reset_link_response_instance = AdminGenerateResetLinkResponse.from_json(json)
# print the JSON string representation of the object
print(AdminGenerateResetLinkResponse.to_json())

# convert the object into a dict
admin_generate_reset_link_response_dict = admin_generate_reset_link_response_instance.to_dict()
# create an instance of AdminGenerateResetLinkResponse from a dict
admin_generate_reset_link_response_from_dict = AdminGenerateResetLinkResponse.from_dict(admin_generate_reset_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


