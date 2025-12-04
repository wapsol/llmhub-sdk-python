# SuperDevListItem

Summary item for Super Dev in list view

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**full_name** | **str** |  | 
**email** | **str** |  | 
**total_organizations** | **int** |  | 
**total_commission_ytd_eur** | **float** |  | 
**is_active** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.super_dev_list_item import SuperDevListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SuperDevListItem from a JSON string
super_dev_list_item_instance = SuperDevListItem.from_json(json)
# print the JSON string representation of the object
print(SuperDevListItem.to_json())

# convert the object into a dict
super_dev_list_item_dict = super_dev_list_item_instance.to_dict()
# create an instance of SuperDevListItem from a dict
super_dev_list_item_from_dict = SuperDevListItem.from_dict(super_dev_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


