# MerchantShipmentLineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant. | 
**merchant_bundle_product_no** | **str** | The unique bundle product reference used by the Merchant. | [optional] 
**channel_product_no** | **str** | The unique product reference used by the Channel. | [optional] 
**order_line** | [**MerchantOrderLineResponse**](MerchantOrderLineResponse.md) |  | [optional] 
**shipment_status** | [**ShipmentLineStatus**](ShipmentLineStatus.md) |  | [optional] 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the shipment line. Each item must have an unqiue key | [optional] 
**quantity** | **int** | Number of items of the product in the shipment. | 

## Example

```python
from openapi_client.models.merchant_shipment_line_response import MerchantShipmentLineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentLineResponse from a JSON string
merchant_shipment_line_response_instance = MerchantShipmentLineResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentLineResponse.to_json())

# convert the object into a dict
merchant_shipment_line_response_dict = merchant_shipment_line_response_instance.to_dict()
# create an instance of MerchantShipmentLineResponse from a dict
merchant_shipment_line_response_from_dict = MerchantShipmentLineResponse.from_dict(merchant_shipment_line_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


