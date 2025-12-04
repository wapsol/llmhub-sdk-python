# RegisterRequest

Request schema for user registration with organization creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**username** | **str** | Desired username | 
**full_name** | **str** | User&#39;s full name | 
**org_name** | **str** | Organization name | 
**org_legal_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.register_request import RegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterRequest from a JSON string
register_request_instance = RegisterRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterRequest.to_json())

# convert the object into a dict
register_request_dict = register_request_instance.to_dict()
# create an instance of RegisterRequest from a dict
register_request_from_dict = RegisterRequest.from_dict(register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


