# V2DomainSearchRequest

Find all email addresses for a company domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**domain** | **str** | Company domain | 
**company** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 10]

## Example

```python
from llmhub_generated.models.v2_domain_search_request import V2DomainSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DomainSearchRequest from a JSON string
v2_domain_search_request_instance = V2DomainSearchRequest.from_json(json)
# print the JSON string representation of the object
print(V2DomainSearchRequest.to_json())

# convert the object into a dict
v2_domain_search_request_dict = v2_domain_search_request_instance.to_dict()
# create an instance of V2DomainSearchRequest from a dict
v2_domain_search_request_from_dict = V2DomainSearchRequest.from_dict(v2_domain_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


