# CustomerPricingResponse

Response schema for customer pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_id** | **int** |  | 
**org_id** | **int** |  | 
**org_name** | **str** |  | [optional] 
**model_id** | **str** |  | 
**model_name** | **str** |  | [optional] 
**custom_input_cost_per_1k** | **float** |  | 
**custom_output_cost_per_1k** | **float** |  | 
**custom_image_cost** | **float** |  | 
**discount_percentage** | **float** |  | 
**valid_from** | **datetime** |  | 
**valid_until** | **datetime** |  | 
**is_active** | **bool** |  | 
**notes** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.customer_pricing_response import CustomerPricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPricingResponse from a JSON string
customer_pricing_response_instance = CustomerPricingResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerPricingResponse.to_json())

# convert the object into a dict
customer_pricing_response_dict = customer_pricing_response_instance.to_dict()
# create an instance of CustomerPricingResponse from a dict
customer_pricing_response_from_dict = CustomerPricingResponse.from_dict(customer_pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


