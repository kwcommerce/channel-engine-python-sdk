# MerchantShipmentLineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** | The unique product reference used by the Merchant (sku). | 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the order. Each item must have an unqiue key | [optional] 
**quantity** | **int** | Number of items of the product in the shipment. | 

## Example

```python
from openapi_client.models.merchant_shipment_line_request import MerchantShipmentLineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantShipmentLineRequest from a JSON string
merchant_shipment_line_request_instance = MerchantShipmentLineRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantShipmentLineRequest.to_json())

# convert the object into a dict
merchant_shipment_line_request_dict = merchant_shipment_line_request_instance.to_dict()
# create an instance of MerchantShipmentLineRequest from a dict
merchant_shipment_line_request_from_dict = MerchantShipmentLineRequest.from_dict(merchant_shipment_line_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


