# SuperDevListResponse

Response for list of Super Devs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**super_devs** | [**List[SuperDevListItem]**](SuperDevListItem.md) |  | 
**total** | **int** |  | 

## Example

```python
from llmhub_generated.models.super_dev_list_response import SuperDevListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperDevListResponse from a JSON string
super_dev_list_response_instance = SuperDevListResponse.from_json(json)
# print the JSON string representation of the object
print(SuperDevListResponse.to_json())

# convert the object into a dict
super_dev_list_response_dict = super_dev_list_response_instance.to_dict()
# create an instance of SuperDevListResponse from a dict
super_dev_list_response_from_dict = SuperDevListResponse.from_dict(super_dev_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


