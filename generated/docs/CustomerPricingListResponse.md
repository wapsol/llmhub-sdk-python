# CustomerPricingListResponse

Response for list of customer pricing rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**pricing_rules** | [**List[CustomerPricingResponse]**](CustomerPricingResponse.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from llmhub_generated.models.customer_pricing_list_response import CustomerPricingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPricingListResponse from a JSON string
customer_pricing_list_response_instance = CustomerPricingListResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerPricingListResponse.to_json())

# convert the object into a dict
customer_pricing_list_response_dict = customer_pricing_list_response_instance.to_dict()
# create an instance of CustomerPricingListResponse from a dict
customer_pricing_list_response_from_dict = CustomerPricingListResponse.from_dict(customer_pricing_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


