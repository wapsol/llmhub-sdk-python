# PromptTemplateUpdate

Schema for updating a prompt template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**user_prompt_template** | **str** |  | [optional] 
**variables** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.prompt_template_update import PromptTemplateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PromptTemplateUpdate from a JSON string
prompt_template_update_instance = PromptTemplateUpdate.from_json(json)
# print the JSON string representation of the object
print(PromptTemplateUpdate.to_json())

# convert the object into a dict
prompt_template_update_dict = prompt_template_update_instance.to_dict()
# create an instance of PromptTemplateUpdate from a dict
prompt_template_update_from_dict = PromptTemplateUpdate.from_dict(prompt_template_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


