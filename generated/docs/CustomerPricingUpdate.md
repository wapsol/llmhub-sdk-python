# CustomerPricingUpdate

Schema for updating custom pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from llmhub_generated.models.customer_pricing_update import CustomerPricingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPricingUpdate from a JSON string
customer_pricing_update_instance = CustomerPricingUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomerPricingUpdate.to_json())

# convert the object into a dict
customer_pricing_update_dict = customer_pricing_update_instance.to_dict()
# create an instance of CustomerPricingUpdate from a dict
customer_pricing_update_from_dict = CustomerPricingUpdate.from_dict(customer_pricing_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


