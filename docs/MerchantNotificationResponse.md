# MerchantNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier used by ChannelEngine. | [optional] 
**read** | **bool** | Indicating whether the notification is already read using the backoffice. | [optional] 
**created_at** | **datetime** | Get the created date time. | [optional] 
**message** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**type** | [**NotificationType**](NotificationType.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_notification_response import MerchantNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantNotificationResponse from a JSON string
merchant_notification_response_instance = MerchantNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantNotificationResponse.to_json())

# convert the object into a dict
merchant_notification_response_dict = merchant_notification_response_instance.to_dict()
# create an instance of MerchantNotificationResponse from a dict
merchant_notification_response_from_dict = MerchantNotificationResponse.from_dict(merchant_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


