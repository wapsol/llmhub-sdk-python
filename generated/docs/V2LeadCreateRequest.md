# V2LeadCreateRequest

Create new lead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**email** | **str** | Lead email address | 
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
from llmhub_generated.models.v2_lead_create_request import V2LeadCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2LeadCreateRequest from a JSON string
v2_lead_create_request_instance = V2LeadCreateRequest.from_json(json)
# print the JSON string representation of the object
print(V2LeadCreateRequest.to_json())

# convert the object into a dict
v2_lead_create_request_dict = v2_lead_create_request_instance.to_dict()
# create an instance of V2LeadCreateRequest from a dict
v2_lead_create_request_from_dict = V2LeadCreateRequest.from_dict(v2_lead_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


