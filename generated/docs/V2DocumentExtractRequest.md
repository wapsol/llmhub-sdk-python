# V2DocumentExtractRequest

Extract specific data from documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**document** | **str** | Document content | 
**extract_fields** | **List[str]** | Fields to extract (e.g., invoice_number, date, total) | 

## Example

```python
from llmhub_generated.models.v2_document_extract_request import V2DocumentExtractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DocumentExtractRequest from a JSON string
v2_document_extract_request_instance = V2DocumentExtractRequest.from_json(json)
# print the JSON string representation of the object
print(V2DocumentExtractRequest.to_json())

# convert the object into a dict
v2_document_extract_request_dict = v2_document_extract_request_instance.to_dict()
# create an instance of V2DocumentExtractRequest from a dict
v2_document_extract_request_from_dict = V2DocumentExtractRequest.from_dict(v2_document_extract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


