# V2AudioSynthesizeRequest

Generate speech from text (TTS)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**text** | **str** |  | 
**voice** | **str** |  | [optional] 
**voice_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**speed** | **float** |  | [optional] 
**output_format** | **str** |  | [optional] 
**stability** | **float** |  | [optional] 
**similarity_boost** | **float** |  | [optional] 
**style** | **float** |  | [optional] 
**use_speaker_boost** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_audio_synthesize_request import V2AudioSynthesizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AudioSynthesizeRequest from a JSON string
v2_audio_synthesize_request_instance = V2AudioSynthesizeRequest.from_json(json)
# print the JSON string representation of the object
print(V2AudioSynthesizeRequest.to_json())

# convert the object into a dict
v2_audio_synthesize_request_dict = v2_audio_synthesize_request_instance.to_dict()
# create an instance of V2AudioSynthesizeRequest from a dict
v2_audio_synthesize_request_from_dict = V2AudioSynthesizeRequest.from_dict(v2_audio_synthesize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


