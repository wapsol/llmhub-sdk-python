# UsageReportByCustomerResponse

Response for usage report by customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**usage_data** | [**List[ModelUsageByCustomer]**](ModelUsageByCustomer.md) |  | 
**summary** | **Dict[str, object]** |  | 
**total_records** | **int** |  | 

## Example

```python
from llmhub_generated.models.usage_report_by_customer_response import UsageReportByCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportByCustomerResponse from a JSON string
usage_report_by_customer_response_instance = UsageReportByCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(UsageReportByCustomerResponse.to_json())

# convert the object into a dict
usage_report_by_customer_response_dict = usage_report_by_customer_response_instance.to_dict()
# create an instance of UsageReportByCustomerResponse from a dict
usage_report_by_customer_response_from_dict = UsageReportByCustomerResponse.from_dict(usage_report_by_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


