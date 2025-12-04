# UsageReportByCustomerRequest

Request schema for usage report by customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**org_id** | **int** |  | [optional] 
**model_id** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**group_by** | **str** | Group by: day, week, month | [optional] [default to 'day']

## Example

```python
from llmhub_generated.models.usage_report_by_customer_request import UsageReportByCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportByCustomerRequest from a JSON string
usage_report_by_customer_request_instance = UsageReportByCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(UsageReportByCustomerRequest.to_json())

# convert the object into a dict
usage_report_by_customer_request_dict = usage_report_by_customer_request_instance.to_dict()
# create an instance of UsageReportByCustomerRequest from a dict
usage_report_by_customer_request_from_dict = UsageReportByCustomerRequest.from_dict(usage_report_by_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


