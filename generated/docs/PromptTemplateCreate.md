# PromptTemplateCreate

Schema for creating a new prompt template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | 
**template_type** | [**ContentType**](ContentType.md) |  | 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | 
**user_prompt_template** | **str** |  | 
**variables** | **Dict[str, object]** |  | [optional] 
**output_config** | **Dict[str, object]** |  | [optional] 
**is_public** | **bool** |  | [optional] [default to False]

## Example

```python
from llmhub_generated.models.prompt_template_create import PromptTemplateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplateCreate from a JSON string
prompt_template_create_instance = PromptTemplateCreate.from_json(json)
# print the JSON string representation of the object
print(PromptTemplateCreate.to_json())

# convert the object into a dict
prompt_template_create_dict = prompt_template_create_instance.to_dict()
# create an instance of PromptTemplateCreate from a dict
prompt_template_create_from_dict = PromptTemplateCreate.from_dict(prompt_template_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


