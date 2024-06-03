# MerchantReturnLineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**quantity** | **int** | Number of items of the product in this return. | 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the returnline. Each item must have an unqiue key | [optional] 

## Example

```python
from openapi_client.models.merchant_return_line_request import MerchantReturnLineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReturnLineRequest from a JSON string
merchant_return_line_request_instance = MerchantReturnLineRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantReturnLineRequest.to_json())

# convert the object into a dict
merchant_return_line_request_dict = merchant_return_line_request_instance.to_dict()
# create an instance of MerchantReturnLineRequest from a dict
merchant_return_line_request_from_dict = MerchantReturnLineRequest.from_dict(merchant_return_line_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


