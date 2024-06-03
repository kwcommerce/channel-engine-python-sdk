# CollectionOfMerchantNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[MerchantNotificationResponse]**](MerchantNotificationResponse.md) |  | [optional] 
**count** | **int** | The number of items in the current response. | [optional] 
**total_count** | **int** | The total number of items. | [optional] 
**items_per_page** | **int** | The number of items per page. | [optional] 
**status_code** | **int** |  | [optional] 
**request_id** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**exception_type** | **str** |  | [optional] 
**validation_errors** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.collection_of_merchant_notification_response import CollectionOfMerchantNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionOfMerchantNotificationResponse from a JSON string
collection_of_merchant_notification_response_instance = CollectionOfMerchantNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(CollectionOfMerchantNotificationResponse.to_json())

# convert the object into a dict
collection_of_merchant_notification_response_dict = collection_of_merchant_notification_response_instance.to_dict()
# create an instance of CollectionOfMerchantNotificationResponse from a dict
collection_of_merchant_notification_response_from_dict = CollectionOfMerchantNotificationResponse.from_dict(collection_of_merchant_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


