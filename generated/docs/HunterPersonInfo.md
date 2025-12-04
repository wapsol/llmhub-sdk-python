# HunterPersonInfo

Person information from enrichment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**facebook** | **str** |  | [optional] 
**github** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.hunter_person_info import HunterPersonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HunterPersonInfo from a JSON string
hunter_person_info_instance = HunterPersonInfo.from_json(json)
# print the JSON string representation of the object
print(HunterPersonInfo.to_json())

# convert the object into a dict
hunter_person_info_dict = hunter_person_info_instance.to_dict()
# create an instance of HunterPersonInfo from a dict
hunter_person_info_from_dict = HunterPersonInfo.from_dict(hunter_person_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


