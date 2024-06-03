# MerchantCancellationLineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**quantity** | **int** | Quantity of the product to cancel. | 

## Example

```python
from openapi_client.models.merchant_cancellation_line_request import MerchantCancellationLineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCancellationLineRequest from a JSON string
merchant_cancellation_line_request_instance = MerchantCancellationLineRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantCancellationLineRequest.to_json())

# convert the object into a dict
merchant_cancellation_line_request_dict = merchant_cancellation_line_request_instance.to_dict()
# create an instance of MerchantCancellationLineRequest from a dict
merchant_cancellation_line_request_from_dict = MerchantCancellationLineRequest.from_dict(merchant_cancellation_line_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


