# WebhookPayload

Webhook payload from OpusClip

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**status** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from llmhub_generated.models.webhook_payload import WebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPayload from a JSON string
webhook_payload_instance = WebhookPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookPayload.to_json())

# convert the object into a dict
webhook_payload_dict = webhook_payload_instance.to_dict()
# create an instance of WebhookPayload from a dict
webhook_payload_from_dict = WebhookPayload.from_dict(webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


