# MerchantReturnLineUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**accepted_quantity** | **int** | The amount of items that have been accepted. | 
**rejected_quantity** | **int** | The amount of items that have been rejected. | 

## Example

```python
from openapi_client.models.merchant_return_line_update_request import MerchantReturnLineUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReturnLineUpdateRequest from a JSON string
merchant_return_line_update_request_instance = MerchantReturnLineUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantReturnLineUpdateRequest.to_json())

# convert the object into a dict
merchant_return_line_update_request_dict = merchant_return_line_update_request_instance.to_dict()
# create an instance of MerchantReturnLineUpdateRequest from a dict
merchant_return_line_update_request_from_dict = MerchantReturnLineUpdateRequest.from_dict(merchant_return_line_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


