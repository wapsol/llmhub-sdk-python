# TranslationContent

Content fields to translate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**meta_title** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**meta_keywords** | **str** |  | [optional] 

## Example

```python
from llmhub_generated.models.translation_content import TranslationContent

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationContent from a JSON string
translation_content_instance = TranslationContent.from_json(json)
# print the JSON string representation of the object
print(TranslationContent.to_json())

# convert the object into a dict
translation_content_dict = translation_content_instance.to_dict()
# create an instance of TranslationContent from a dict
translation_content_from_dict = TranslationContent.from_dict(translation_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


