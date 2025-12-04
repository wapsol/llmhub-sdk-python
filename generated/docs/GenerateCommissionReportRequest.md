# GenerateCommissionReportRequest

Request to generate commission report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**usd_to_eur_rate** | **float** |  | [optional] 

## Example

```python
from llmhub_generated.models.generate_commission_report_request import GenerateCommissionReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCommissionReportRequest from a JSON string
generate_commission_report_request_instance = GenerateCommissionReportRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateCommissionReportRequest.to_json())

# convert the object into a dict
generate_commission_report_request_dict = generate_commission_report_request_instance.to_dict()
# create an instance of GenerateCommissionReportRequest from a dict
generate_commission_report_request_from_dict = GenerateCommissionReportRequest.from_dict(generate_commission_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


