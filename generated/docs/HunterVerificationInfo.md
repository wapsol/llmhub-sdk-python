# HunterVerificationInfo

Email verification information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**result** | **str** |  | [optional] 
**score** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**regexp** | **bool** |  | [optional] 
**gibberish** | **bool** |  | [optional] 
**disposable** | **bool** |  | [optional] 
**webmail** | **bool** |  | [optional] 
**mx_records** | **bool** |  | [optional] 
**smtp_server** | **bool** |  | [optional] 
**smtp_check** | **bool** |  | [optional] 
**accept_all** | **bool** |  | [optional] 
**block** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.hunter_verification_info import HunterVerificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HunterVerificationInfo from a JSON string
hunter_verification_info_instance = HunterVerificationInfo.from_json(json)
# print the JSON string representation of the object
print(HunterVerificationInfo.to_json())

# convert the object into a dict
hunter_verification_info_dict = hunter_verification_info_instance.to_dict()
# create an instance of HunterVerificationInfo from a dict
hunter_verification_info_from_dict = HunterVerificationInfo.from_dict(hunter_verification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


