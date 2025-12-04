# V2DocumentClassifyRequest

Classify document type/category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**document** | **str** | Document content | 
**possible_types** | **List[str]** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_document_classify_request import V2DocumentClassifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DocumentClassifyRequest from a JSON string
v2_document_classify_request_instance = V2DocumentClassifyRequest.from_json(json)
# print the JSON string representation of the object
print(V2DocumentClassifyRequest.to_json())

# convert the object into a dict
v2_document_classify_request_dict = v2_document_classify_request_instance.to_dict()
# create an instance of V2DocumentClassifyRequest from a dict
v2_document_classify_request_from_dict = V2DocumentClassifyRequest.from_dict(v2_document_classify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


