# DetailedHealthCheckResponse

Detailed health check with dependency status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**timestamp** | **datetime** |  | 
**checks** | **Dict[str, str]** |  | 

## Example

```python
from llmhub_generated.models.detailed_health_check_response import DetailedHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedHealthCheckResponse from a JSON string
detailed_health_check_response_instance = DetailedHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(DetailedHealthCheckResponse.to_json())

# convert the object into a dict
detailed_health_check_response_dict = detailed_health_check_response_instance.to_dict()
# create an instance of DetailedHealthCheckResponse from a dict
detailed_health_check_response_from_dict = DetailedHealthCheckResponse.from_dict(detailed_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


