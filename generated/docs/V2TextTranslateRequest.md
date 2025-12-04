# V2TextTranslateRequest

Translate text between languages  Supports two modes: 1. Simple text translation: Provide 'text', 'source_language', 'target_language' 2. Structured content translation: Provide 'content', 'source_language', 'target_languages'  Either 'text' or 'content' must be provided (not both). Either 'target_language' or 'target_languages' must be provided (not both).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | [optional] 
**content** | [**TranslationContent**](TranslationContent.md) |  | [optional] 
**source_language** | **str** | Source language code (e.g., &#39;en&#39;, &#39;de&#39;, &#39;fr&#39;) | 
**target_language** | **str** |  | [optional] 
**target_languages** | **List[str]** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_text_translate_request import V2TextTranslateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TextTranslateRequest from a JSON string
v2_text_translate_request_instance = V2TextTranslateRequest.from_json(json)
# print the JSON string representation of the object
print(V2TextTranslateRequest.to_json())

# convert the object into a dict
v2_text_translate_request_dict = v2_text_translate_request_instance.to_dict()
# create an instance of V2TextTranslateRequest from a dict
v2_text_translate_request_from_dict = V2TextTranslateRequest.from_dict(v2_text_translate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


