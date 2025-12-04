# SetCommissionRateRequest

Request to set commission rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_dev_user_id** | **str** |  | 
**org_id** | **int** |  | 
**commission_percentage** | **float** |  | 
**valid_from** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.set_commission_rate_request import SetCommissionRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommissionRateRequest from a JSON string
set_commission_rate_request_instance = SetCommissionRateRequest.from_json(json)
# print the JSON string representation of the object
print(SetCommissionRateRequest.to_json())

# convert the object into a dict
set_commission_rate_request_dict = set_commission_rate_request_instance.to_dict()
# create an instance of SetCommissionRateRequest from a dict
set_commission_rate_request_from_dict = SetCommissionRateRequest.from_dict(set_commission_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


