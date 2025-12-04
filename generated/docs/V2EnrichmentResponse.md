# V2EnrichmentResponse

Base response for enrichment endpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**content** | **object** |  | 
**provider_used** | **str** |  | 
**model_used** | **str** |  | 
**tokens_used** | **int** |  | 
**cost_usd** | **float** |  | [optional] 
**generation_time_ms** | **int** |  | 
**log_id** | **int** |  | [optional] 
**data** | **Dict[str, object]** |  | [optional] 
**person** | [**HunterPersonInfo**](HunterPersonInfo.md) |  | [optional] 
**company** | [**HunterCompanyInfo**](HunterCompanyInfo.md) |  | [optional] 
**verification** | [**HunterVerificationInfo**](HunterVerificationInfo.md) |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_enrichment_response import V2EnrichmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2EnrichmentResponse from a JSON string
v2_enrichment_response_instance = V2EnrichmentResponse.from_json(json)
# print the JSON string representation of the object
print(V2EnrichmentResponse.to_json())

# convert the object into a dict
v2_enrichment_response_dict = v2_enrichment_response_instance.to_dict()
# create an instance of V2EnrichmentResponse from a dict
v2_enrichment_response_from_dict = V2EnrichmentResponse.from_dict(v2_enrichment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


