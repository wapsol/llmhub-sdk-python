# OrganizationActivityItem

Single activity event in organization timeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**event_type** | **str** |  | 
**timestamp** | **datetime** |  | 
**actor** | **str** |  | 
**actor_type** | **str** |  | 
**action** | **str** |  | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**details** | **Dict[str, object]** |  | 
**status** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 

## Example

```python
from llmhub_generated.models.organization_activity_item import OrganizationActivityItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationActivityItem from a JSON string
organization_activity_item_instance = OrganizationActivityItem.from_json(json)
# print the JSON string representation of the object
print(OrganizationActivityItem.to_json())

# convert the object into a dict
organization_activity_item_dict = organization_activity_item_instance.to_dict()
# create an instance of OrganizationActivityItem from a dict
organization_activity_item_from_dict = OrganizationActivityItem.from_dict(organization_activity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


