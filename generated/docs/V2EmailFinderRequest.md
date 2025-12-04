# V2EmailFinderRequest

Find professional email for specific person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**domain** | **str** | Company domain | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_email_finder_request import V2EmailFinderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2EmailFinderRequest from a JSON string
v2_email_finder_request_instance = V2EmailFinderRequest.from_json(json)
# print the JSON string representation of the object
print(V2EmailFinderRequest.to_json())

# convert the object into a dict
v2_email_finder_request_dict = v2_email_finder_request_instance.to_dict()
# create an instance of V2EmailFinderRequest from a dict
v2_email_finder_request_from_dict = V2EmailFinderRequest.from_dict(v2_email_finder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


