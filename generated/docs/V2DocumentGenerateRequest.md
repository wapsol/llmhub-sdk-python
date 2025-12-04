# V2DocumentGenerateRequest

Generate complete documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**document_type** | **str** | Type of document (report, contract, whitepaper, etc.) | 
**specifications** | **Dict[str, object]** | Document specifications and requirements | 

## Example

```python
from llmhub_generated.models.v2_document_generate_request import V2DocumentGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DocumentGenerateRequest from a JSON string
v2_document_generate_request_instance = V2DocumentGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(V2DocumentGenerateRequest.to_json())

# convert the object into a dict
v2_document_generate_request_dict = v2_document_generate_request_instance.to_dict()
# create an instance of V2DocumentGenerateRequest from a dict
v2_document_generate_request_from_dict = V2DocumentGenerateRequest.from_dict(v2_document_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


