# MerchantCancellationLineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique cancellation line identifier used by ChannelEngine. | [optional] 
**merchant_product_no** | **str** | The unique product reference used by the Merchant. | [optional] 
**channel_product_no** | **str** | The unique product reference used by the Channel. | [optional] 
**quantity** | **int** | Quantity of the product to cancel. | 

## Example

```python
from openapi_client.models.merchant_cancellation_line_response import MerchantCancellationLineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCancellationLineResponse from a JSON string
merchant_cancellation_line_response_instance = MerchantCancellationLineResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantCancellationLineResponse.to_json())

# convert the object into a dict
merchant_cancellation_line_response_dict = merchant_cancellation_line_response_instance.to_dict()
# create an instance of MerchantCancellationLineResponse from a dict
merchant_cancellation_line_response_from_dict = MerchantCancellationLineResponse.from_dict(merchant_cancellation_line_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


