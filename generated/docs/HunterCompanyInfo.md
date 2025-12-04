# HunterCompanyInfo

Company information from enrichment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**sector** | **str** |  | [optional] 
**founded** | **int** |  | [optional] 
**employee_count** | **int** |  | [optional] 
**headquarters** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**facebook** | **str** |  | [optional] 
**technologies** | **List[str]** |  | [optional] 
**traffic_rank** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.hunter_company_info import HunterCompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HunterCompanyInfo from a JSON string
hunter_company_info_instance = HunterCompanyInfo.from_json(json)
# print the JSON string representation of the object
print(HunterCompanyInfo.to_json())

# convert the object into a dict
hunter_company_info_dict = hunter_company_info_instance.to_dict()
# create an instance of HunterCompanyInfo from a dict
hunter_company_info_from_dict = HunterCompanyInfo.from_dict(hunter_company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


