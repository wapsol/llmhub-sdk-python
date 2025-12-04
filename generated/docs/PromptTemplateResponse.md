# PromptTemplateResponse

Response schema for prompt template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**template_name** | **str** |  | 
**template_type** | **str** |  | 
**description** | **str** |  | 
**variables** | **Dict[str, object]** |  | 
**usage_count** | **int** |  | 
**success_rate** | **float** |  | 
**is_public** | **bool** |  | 
**is_active** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from llmhub_generated.models.prompt_template_response import PromptTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplateResponse from a JSON string
prompt_template_response_instance = PromptTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PromptTemplateResponse.to_json())

# convert the object into a dict
prompt_template_response_dict = prompt_template_response_instance.to_dict()
# create an instance of PromptTemplateResponse from a dict
prompt_template_response_from_dict = PromptTemplateResponse.from_dict(prompt_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


