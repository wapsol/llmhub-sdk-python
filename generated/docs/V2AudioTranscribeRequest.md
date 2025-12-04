# V2AudioTranscribeRequest

Transcribe audio to text with audio intelligence features  Supports: - Multi-model transcription (best/nano tiers) - Speaker diarization (who said what) - Sentiment analysis per sentence - Entity detection (names, dates, organizations) - Auto-summarization with chapters - Topic classification (600+ IAB categories) - Content moderation - PII redaction for privacy - Custom vocabulary boosting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**audio_url** | **str** | Public URL to audio file (REQUIRED) | 
**language_code** | **str** |  | [optional] 
**speaker_labels** | **bool** |  | [optional] 
**speakers_expected** | **int** |  | [optional] 
**sentiment_analysis** | **bool** |  | [optional] 
**entity_detection** | **bool** |  | [optional] 
**auto_chapters** | **bool** |  | [optional] 
**summarization** | **bool** |  | [optional] 
**summarization_type** | **str** |  | [optional] 
**iab_categories** | **bool** |  | [optional] 
**content_safety** | **bool** |  | [optional] 
**filter_profanity** | **bool** |  | [optional] 
**redact_pii** | **bool** |  | [optional] 
**word_boost** | **List[str]** |  | [optional] 
**boost_param** | **str** |  | [optional] 
**detect_language** | **bool** |  | [optional] 
**smart_format** | **bool** |  | [optional] 
**punctuate** | **bool** |  | [optional] 
**paragraphs** | **bool** |  | [optional] 
**numerals** | **bool** |  | [optional] 
**filler_words** | **bool** |  | [optional] 
**utterances** | **bool** |  | [optional] 
**topics** | **bool** |  | [optional] 
**custom_topics** | **List[str]** |  | [optional] 
**intents** | **bool** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**keyword_boost** | **float** |  | [optional] 
**search** | **List[str]** |  | [optional] 
**replace** | **Dict[str, str]** |  | [optional] 
**multichannel** | **bool** |  | [optional] 

## Example

```python
from llmhub_generated.models.v2_audio_transcribe_request import V2AudioTranscribeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AudioTranscribeRequest from a JSON string
v2_audio_transcribe_request_instance = V2AudioTranscribeRequest.from_json(json)
# print the JSON string representation of the object
print(V2AudioTranscribeRequest.to_json())

# convert the object into a dict
v2_audio_transcribe_request_dict = v2_audio_transcribe_request_instance.to_dict()
# create an instance of V2AudioTranscribeRequest from a dict
v2_audio_transcribe_request_from_dict = V2AudioTranscribeRequest.from_dict(v2_audio_transcribe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


