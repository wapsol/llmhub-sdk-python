# OrganizationActivityResponse

Response for organization activity timeline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**activities** | [**List[OrganizationActivityItem]**](OrganizationActivityItem.md) |  | 
**total_count** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from llmhub_generated.models.organization_activity_response import OrganizationActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationActivityResponse from a JSON string
organization_activity_response_instance = OrganizationActivityResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationActivityResponse.to_json())

# convert the object into a dict
organization_activity_response_dict = organization_activity_response_instance.to_dict()
# create an instance of OrganizationActivityResponse from a dict
organization_activity_response_from_dict = OrganizationActivityResponse.from_dict(organization_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


