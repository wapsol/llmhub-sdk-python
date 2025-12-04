# CommissionRateResponse

Response schema for commission rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **int** |  | 
**super_dev_user_id** | **str** |  | 
**org_id** | **int** |  | 
**org_name** | **str** |  | [optional] 
**super_dev_name** | **str** |  | [optional] 
**commission_percentage** | **float** |  | 
**valid_from** | **datetime** |  | 
**valid_until** | **datetime** |  | [optional] 
**is_active** | **bool** |  | 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.commission_rate_response import CommissionRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionRateResponse from a JSON string
commission_rate_response_instance = CommissionRateResponse.from_json(json)
# print the JSON string representation of the object
print(CommissionRateResponse.to_json())

# convert the object into a dict
commission_rate_response_dict = commission_rate_response_instance.to_dict()
# create an instance of CommissionRateResponse from a dict
commission_rate_response_from_dict = CommissionRateResponse.from_dict(commission_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


