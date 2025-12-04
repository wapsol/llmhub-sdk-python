# V2LeadUpdateRequest

Update existing lead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**linkedin_url** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_lead_update_request import V2LeadUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2LeadUpdateRequest from a JSON string
v2_lead_update_request_instance = V2LeadUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(V2LeadUpdateRequest.to_json())

# convert the object into a dict
v2_lead_update_request_dict = v2_lead_update_request_instance.to_dict()
# create an instance of V2LeadUpdateRequest from a dict
v2_lead_update_request_from_dict = V2LeadUpdateRequest.from_dict(v2_lead_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


