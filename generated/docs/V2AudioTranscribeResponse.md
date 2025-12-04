# V2AudioTranscribeResponse

Response for audio transcription with audio intelligence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**content** | **object** |  | 
**provider_used** | **str** |  | 
**model_used** | **str** |  | 
**tokens_used** | **int** |  | 
**cost_usd** | **float** |  | 
**generation_time_ms** | **int** |  | 
**log_id** | **str** |  | 
**text** | **str** | Full transcript text | 
**audio_duration** | **float** | Audio duration in seconds | 
**confidence** | **float** |  | [optional] 
**language_code** | **str** |  | [optional] 
**utterances** | **List[Dict[str, object]]** |  | [optional] 
**chapters** | **List[Dict[str, object]]** |  | [optional] 
**entities** | **List[Dict[str, object]]** |  | [optional] 
**sentiment_analysis_results** | **List[Dict[str, object]]** |  | [optional] 
**iab_categories_result** | **Dict[str, object]** |  | [optional] 
**content_safety_labels** | **Dict[str, object]** |  | [optional] 
**summary** | **str** |  | [optional] 
**words** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_audio_transcribe_response import V2AudioTranscribeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2AudioTranscribeResponse from a JSON string
v2_audio_transcribe_response_instance = V2AudioTranscribeResponse.from_json(json)
# print the JSON string representation of the object
print(V2AudioTranscribeResponse.to_json())

# convert the object into a dict
v2_audio_transcribe_response_dict = v2_audio_transcribe_response_instance.to_dict()
# create an instance of V2AudioTranscribeResponse from a dict
v2_audio_transcribe_response_from_dict = V2AudioTranscribeResponse.from_dict(v2_audio_transcribe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


