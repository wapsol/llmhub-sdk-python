# ImageEditRequest

Request schema for image editing (DALL-E 2)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | URL of the image to edit | 
**mask_url** | **str** |  | [optional] 
**prompt** | **str** | Description of the desired edit | 
**size** | **str** | Output size (256x256, 512x512, 1024x1024) | [optional] [default to '1024x1024']

## Example

```python
from llmhub_generated.models.image_edit_request import ImageEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageEditRequest from a JSON string
image_edit_request_instance = ImageEditRequest.from_json(json)
# print the JSON string representation of the object
print(ImageEditRequest.to_json())

# convert the object into a dict
image_edit_request_dict = image_edit_request_instance.to_dict()
# create an instance of ImageEditRequest from a dict
image_edit_request_from_dict = ImageEditRequest.from_dict(image_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


