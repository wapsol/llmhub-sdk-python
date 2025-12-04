# DateRangeUsageRequest

Simple date range usage request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** | Start date (inclusive) | 
**to_date** | **datetime** | End date (inclusive) | 
**org_id** | **int** |  | [optional] 

## Example

```python
from llmhub_generated.models.date_range_usage_request import DateRangeUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeUsageRequest from a JSON string
date_range_usage_request_instance = DateRangeUsageRequest.from_json(json)
# print the JSON string representation of the object
print(DateRangeUsageRequest.to_json())

# convert the object into a dict
date_range_usage_request_dict = date_range_usage_request_instance.to_dict()
# create an instance of DateRangeUsageRequest from a dict
date_range_usage_request_from_dict = DateRangeUsageRequest.from_dict(date_range_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


