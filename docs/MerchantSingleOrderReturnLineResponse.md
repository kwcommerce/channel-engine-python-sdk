# MerchantSingleOrderReturnLineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | [optional] 
**accepted_quantity** | **int** | The accepted quantity of returned products in this orderline. | [optional] 
**rejected_quantity** | **int** | The rejected quantity of returned products in this orderline. | [optional] 
**order_line** | [**MerchantOrderLineResponse**](MerchantOrderLineResponse.md) |  | [optional] 
**shipment_status** | [**ShipmentLineStatus**](ShipmentLineStatus.md) |  | [optional] 
**quantity** | **int** | Number of items of the product in this return. | 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the returnline. Each item must have an unqiue key | [optional] 

## Example

```python
from openapi_client.models.merchant_single_order_return_line_response import MerchantSingleOrderReturnLineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSingleOrderReturnLineResponse from a JSON string
merchant_single_order_return_line_response_instance = MerchantSingleOrderReturnLineResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantSingleOrderReturnLineResponse.to_json())

# convert the object into a dict
merchant_single_order_return_line_response_dict = merchant_single_order_return_line_response_instance.to_dict()
# create an instance of MerchantSingleOrderReturnLineResponse from a dict
merchant_single_order_return_line_response_from_dict = MerchantSingleOrderReturnLineResponse.from_dict(merchant_single_order_return_line_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


