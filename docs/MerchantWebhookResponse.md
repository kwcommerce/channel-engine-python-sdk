# MerchantWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_webhook_response import MerchantWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWebhookResponse from a JSON string
merchant_webhook_response_instance = MerchantWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantWebhookResponse.to_json())

# convert the object into a dict
merchant_webhook_response_dict = merchant_webhook_response_instance.to_dict()
# create an instance of MerchantWebhookResponse from a dict
merchant_webhook_response_from_dict = MerchantWebhookResponse.from_dict(merchant_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


