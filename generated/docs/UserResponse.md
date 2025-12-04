# UserResponse

Response schema for user data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**full_name** | **str** |  | [optional] 
**user_id** | **str** |  | 
**oauth_provider** | **str** |  | 
**avatar_url** | **str** |  | 
**org_id** | **int** |  | 
**org_name** | **str** |  | [optional] 
**roles** | **List[str]** | List of role names | [optional] 
**is_active** | **bool** |  | 
**is_email_verified** | **bool** |  | 
**last_login_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


