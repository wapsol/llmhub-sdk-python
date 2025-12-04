# V2CombinedEnrichmentRequest

Combined person + company enrichment in single call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**email** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_combined_enrichment_request import V2CombinedEnrichmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2CombinedEnrichmentRequest from a JSON string
v2_combined_enrichment_request_instance = V2CombinedEnrichmentRequest.from_json(json)
# print the JSON string representation of the object
print(V2CombinedEnrichmentRequest.to_json())

# convert the object into a dict
v2_combined_enrichment_request_dict = v2_combined_enrichment_request_instance.to_dict()
# create an instance of V2CombinedEnrichmentRequest from a dict
v2_combined_enrichment_request_from_dict = V2CombinedEnrichmentRequest.from_dict(v2_combined_enrichment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


