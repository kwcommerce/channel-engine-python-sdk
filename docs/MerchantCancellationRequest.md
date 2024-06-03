# MerchantCancellationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_cancellation_no** | **str** | The unique cancellation reference used by the Merchant (sku). | 
**merchant_order_no** | **str** | The unique order reference used by the Merchant (sku). | 
**lines** | [**List[MerchantCancellationLineRequest]**](MerchantCancellationLineRequest.md) |  | 
**reason** | **str** | Reason for cancellation (text). | [optional] 
**reason_code** | [**MancoReason**](MancoReason.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_cancellation_request import MerchantCancellationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCancellationRequest from a JSON string
merchant_cancellation_request_instance = MerchantCancellationRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantCancellationRequest.to_json())

# convert the object into a dict
merchant_cancellation_request_dict = merchant_cancellation_request_instance.to_dict()
# create an instance of MerchantCancellationRequest from a dict
merchant_cancellation_request_from_dict = MerchantCancellationRequest.from_dict(merchant_cancellation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


