# ImageGenerationRequest

Request schema for image generation (DALL-E 3)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | Image generation prompt | 
**size** | **str** | Image size (1024x1024, 1792x1024, 1024x1792) | [optional] [default to '1024x1024']
**quality** | **str** | Image quality (standard, hd) | [optional] [default to 'standard']
**style** | **str** | Image style (vivid, natural) | [optional] [default to 'vivid']
**upload_to_minio** | **bool** | Upload to MinIO storage | [optional] [default to True]

## Example

```python
from llmhub_generated.models.image_generation_request import ImageGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGenerationRequest from a JSON string
image_generation_request_instance = ImageGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(ImageGenerationRequest.to_json())

# convert the object into a dict
image_generation_request_dict = image_generation_request_instance.to_dict()
# create an instance of ImageGenerationRequest from a dict
image_generation_request_from_dict = ImageGenerationRequest.from_dict(image_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


