# V2DiscoverRequest

Discover companies using natural language queries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**query** | **str** | Natural language search query | 
**headquarters** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 10]

## Example

```python
from llmhub_generated.models.v2_discover_request import V2DiscoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DiscoverRequest from a JSON string
v2_discover_request_instance = V2DiscoverRequest.from_json(json)
# print the JSON string representation of the object
print(V2DiscoverRequest.to_json())

# convert the object into a dict
v2_discover_request_dict = v2_discover_request_instance.to_dict()
# create an instance of V2DiscoverRequest from a dict
v2_discover_request_from_dict = V2DiscoverRequest.from_dict(v2_discover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


