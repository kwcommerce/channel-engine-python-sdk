# MerchantCancellationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique cancellation identifier used by ChannelEngine. | [optional] 
**merchant_cancellation_no** | **str** | The unique cancellation reference used by the Merchant (sku). | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | 
**channel_order_no** | **str** | The unique order reference used by the Channel. | [optional] 
**lines** | [**List[MerchantCancellationLineResponse]**](MerchantCancellationLineResponse.md) |  | 
**created_at** | **datetime** | The date at which the cancellation was created in ChannelEngine. | [optional] 
**reason** | **str** | Reason for cancellation (text). | [optional] 
**reason_code** | [**MancoReason**](MancoReason.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_cancellation_response import MerchantCancellationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCancellationResponse from a JSON string
merchant_cancellation_response_instance = MerchantCancellationResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantCancellationResponse.to_json())

# convert the object into a dict
merchant_cancellation_response_dict = merchant_cancellation_response_instance.to_dict()
# create an instance of MerchantCancellationResponse from a dict
merchant_cancellation_response_from_dict = MerchantCancellationResponse.from_dict(merchant_cancellation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


