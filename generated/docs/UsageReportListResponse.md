# UsageReportListResponse

Schema for paginated list of usage reports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**reports** | [**List[UsageReportResponse]**](UsageReportResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from llmhub_generated.models.usage_report_list_response import UsageReportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportListResponse from a JSON string
usage_report_list_response_instance = UsageReportListResponse.from_json(json)
# print the JSON string representation of the object
print(UsageReportListResponse.to_json())

# convert the object into a dict
usage_report_list_response_dict = usage_report_list_response_instance.to_dict()
# create an instance of UsageReportListResponse from a dict
usage_report_list_response_from_dict = UsageReportListResponse.from_dict(usage_report_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


