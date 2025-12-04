# V2DocumentStructureRequest

Convert unstructured documents to structured format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**document** | **str** | Unstructured document content | 
**target_format** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_document_structure_request import V2DocumentStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DocumentStructureRequest from a JSON string
v2_document_structure_request_instance = V2DocumentStructureRequest.from_json(json)
# print the JSON string representation of the object
print(V2DocumentStructureRequest.to_json())

# convert the object into a dict
v2_document_structure_request_dict = v2_document_structure_request_instance.to_dict()
# create an instance of V2DocumentStructureRequest from a dict
v2_document_structure_request_from_dict = V2DocumentStructureRequest.from_dict(v2_document_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


