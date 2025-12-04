# Texts

Single text or list of texts to embed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from llmhub_generated.models.texts import Texts

# TODO update the JSON string below
json = "{}"
# create an instance of Texts from a JSON string
texts_instance = Texts.from_json(json)
# print the JSON string representation of the object
print(Texts.to_json())

# convert the object into a dict
texts_dict = texts_instance.to_dict()
# create an instance of Texts from a dict
texts_from_dict = Texts.from_dict(texts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


