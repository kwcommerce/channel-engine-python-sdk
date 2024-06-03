# MerchantWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of a webhook. | 
**url** | **str** | The callback URL used by a webhook. E.g.: https://test-store.com/callback. | 
**is_active** | **bool** | Determines if a webhook is active, and callbacks should proceed. | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | The events supported by the webhook. | 

## Example

```python
from openapi_client.models.merchant_webhook_request import MerchantWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWebhookRequest from a JSON string
merchant_webhook_request_instance = MerchantWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantWebhookRequest.to_json())

# convert the object into a dict
merchant_webhook_request_dict = merchant_webhook_request_instance.to_dict()
# create an instance of MerchantWebhookRequest from a dict
merchant_webhook_request_from_dict = MerchantWebhookRequest.from_dict(merchant_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


