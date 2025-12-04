# V2CompanyEnrichmentRequest

Enrich company profile with firmographic and technographic data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**domain** | **str** | Company domain | 

## Example

```python
from llmhub_generated.models.v2_company_enrichment_request import V2CompanyEnrichmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2CompanyEnrichmentRequest from a JSON string
v2_company_enrichment_request_instance = V2CompanyEnrichmentRequest.from_json(json)
# print the JSON string representation of the object
print(V2CompanyEnrichmentRequest.to_json())

# convert the object into a dict
v2_company_enrichment_request_dict = v2_company_enrichment_request_instance.to_dict()
# create an instance of V2CompanyEnrichmentRequest from a dict
v2_company_enrichment_request_from_dict = V2CompanyEnrichmentRequest.from_dict(v2_company_enrichment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


