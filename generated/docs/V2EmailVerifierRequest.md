# V2EmailVerifierRequest

Verify email address validity and deliverability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**email** | **str** | Email address to verify | 

## Example

```python
from llmhub_generated.models.v2_email_verifier_request import V2EmailVerifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2EmailVerifierRequest from a JSON string
v2_email_verifier_request_instance = V2EmailVerifierRequest.from_json(json)
# print the JSON string representation of the object
print(V2EmailVerifierRequest.to_json())

# convert the object into a dict
v2_email_verifier_request_dict = v2_email_verifier_request_instance.to_dict()
# create an instance of V2EmailVerifierRequest from a dict
v2_email_verifier_request_from_dict = V2EmailVerifierRequest.from_dict(v2_email_verifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


