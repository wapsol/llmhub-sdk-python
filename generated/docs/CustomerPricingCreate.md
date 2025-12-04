# CustomerPricingCreate

Schema for creating custom pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Organization ID | 
**model_id** | **str** | Model UUID | 
**custom_input_cost_per_1k** | **float** |  | [optional] 
**custom_output_cost_per_1k** | **float** |  | [optional] 
**custom_image_cost** | **float** |  | [optional] 
**discount_percentage** | **float** |  | [optional] 
**valid_from** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.customer_pricing_create import CustomerPricingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPricingCreate from a JSON string
customer_pricing_create_instance = CustomerPricingCreate.from_json(json)
# print the JSON string representation of the object
print(CustomerPricingCreate.to_json())

# convert the object into a dict
customer_pricing_create_dict = customer_pricing_create_instance.to_dict()
# create an instance of CustomerPricingCreate from a dict
customer_pricing_create_from_dict = CustomerPricingCreate.from_dict(customer_pricing_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


