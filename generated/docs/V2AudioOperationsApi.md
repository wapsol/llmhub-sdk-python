# llmhub_generated.V2AudioOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enhance_audio_api_v2_audio_enhance_post**](V2AudioOperationsApi.md#enhance_audio_api_v2_audio_enhance_post) | **POST** /api/v2/audio/enhance | Enhance Audio
[**separate_audio_api_v2_audio_separate_post**](V2AudioOperationsApi.md#separate_audio_api_v2_audio_separate_post) | **POST** /api/v2/audio/separate | Separate Audio
[**synthesize_audio_api_v2_audio_synthesize_post**](V2AudioOperationsApi.md#synthesize_audio_api_v2_audio_synthesize_post) | **POST** /api/v2/audio/synthesize | Synthesize Audio
[**transcribe_audio_api_v2_audio_transcribe_post**](V2AudioOperationsApi.md#transcribe_audio_api_v2_audio_transcribe_post) | **POST** /api/v2/audio/transcribe | Transcribe Audio


# **enhance_audio_api_v2_audio_enhance_post**
> V2BaseResponse enhance_audio_api_v2_audio_enhance_post(x_api_key)

Enhance Audio

Enhance audio quality (denoise, normalize, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2AudioOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Enhance Audio
        api_response = api_instance.enhance_audio_api_v2_audio_enhance_post(x_api_key)
        print("The response of V2AudioOperationsApi->enhance_audio_api_v2_audio_enhance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AudioOperationsApi->enhance_audio_api_v2_audio_enhance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **separate_audio_api_v2_audio_separate_post**
> V2BaseResponse separate_audio_api_v2_audio_separate_post(x_api_key)

Separate Audio

Separate audio tracks/sources (isolate vocals, etc.)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2AudioOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 

    try:
        # Separate Audio
        api_response = api_instance.separate_audio_api_v2_audio_separate_post(x_api_key)
        print("The response of V2AudioOperationsApi->separate_audio_api_v2_audio_separate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AudioOperationsApi->separate_audio_api_v2_audio_separate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synthesize_audio_api_v2_audio_synthesize_post**
> V2BaseResponse synthesize_audio_api_v2_audio_synthesize_post(x_api_key, v2_audio_synthesize_request)

Synthesize Audio

Generate speech from text (text-to-speech/TTS)

Supported providers:
- ElevenLabs: Premium quality with 6 models, voice cloning, 32 languages
- OpenAI TTS: Cost-effective option (future integration)
- Google Cloud TTS: High-quality multilingual (future integration)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_audio_synthesize_request import V2AudioSynthesizeRequest
from llmhub_generated.models.v2_base_response import V2BaseResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2AudioOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_audio_synthesize_request = llmhub_generated.V2AudioSynthesizeRequest() # V2AudioSynthesizeRequest | 

    try:
        # Synthesize Audio
        api_response = api_instance.synthesize_audio_api_v2_audio_synthesize_post(x_api_key, v2_audio_synthesize_request)
        print("The response of V2AudioOperationsApi->synthesize_audio_api_v2_audio_synthesize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AudioOperationsApi->synthesize_audio_api_v2_audio_synthesize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_audio_synthesize_request** | [**V2AudioSynthesizeRequest**](V2AudioSynthesizeRequest.md)|  | 

### Return type

[**V2BaseResponse**](V2BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcribe_audio_api_v2_audio_transcribe_post**
> V2AudioTranscribeResponse transcribe_audio_api_v2_audio_transcribe_post(x_api_key, v2_audio_transcribe_request)

Transcribe Audio

Transcribe audio to text with audio intelligence

Supported providers:
- Deepgram (default): Ultra-fast with sub-200ms latency
  - Nova-3: 54% lower WER, real-time code-switching (10 languages)
  - Smart formatting, speaker diarization (40x faster)
  - Summarization, topics, sentiment, intents
  - Keyword boosting, PII redaction
  - All features included in base price ($0.258/hour)
- AssemblyAI: State-of-the-art with Universal-2 (24% better proper nouns)
  - Speaker diarization, sentiment analysis
  - Entity detection, auto chapters & summarization
  - Topic classification (600+ IAB categories)
  - Content moderation
- OpenAI Whisper: Cost-effective option (future integration)

### Example


```python
import llmhub_generated
from llmhub_generated.models.v2_audio_transcribe_request import V2AudioTranscribeRequest
from llmhub_generated.models.v2_audio_transcribe_response import V2AudioTranscribeResponse
from llmhub_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = llmhub_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with llmhub_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = llmhub_generated.V2AudioOperationsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    v2_audio_transcribe_request = llmhub_generated.V2AudioTranscribeRequest() # V2AudioTranscribeRequest | 

    try:
        # Transcribe Audio
        api_response = api_instance.transcribe_audio_api_v2_audio_transcribe_post(x_api_key, v2_audio_transcribe_request)
        print("The response of V2AudioOperationsApi->transcribe_audio_api_v2_audio_transcribe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2AudioOperationsApi->transcribe_audio_api_v2_audio_transcribe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **v2_audio_transcribe_request** | [**V2AudioTranscribeRequest**](V2AudioTranscribeRequest.md)|  | 

### Return type

[**V2AudioTranscribeResponse**](V2AudioTranscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

