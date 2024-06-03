# ChangePurchaseOrderShipmentLine

For Create or Update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_order_no** | **str** | Channel&#39;s identifier of the purchase order | 
**merchant_product_no** | **str** | Merchant&#39;s identifier of the product.  The combination of ChannelOrderNo + MerchantProductNo identifies the order line this shipment line  ships. | 
**quantity_unit_of_measure** | [**PurchaseOrderLineUnitOfMeasure**](PurchaseOrderLineUnitOfMeasure.md) |  | [optional] 
**quantity** | **int** | The quantity | [optional] 
**quantity_unit_size** | **int** | The case size, when QuantityUnitOfMeasure is &#39;CASES&#39;. Otherwise, it is 1. | [optional] 
**expiry_date** | **datetime** | The date that determines the limit of consumption or use of a product.  For perishable products. | [optional] 

## Example

```python
from openapi_client.models.change_purchase_order_shipment_line import ChangePurchaseOrderShipmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePurchaseOrderShipmentLine from a JSON string
change_purchase_order_shipment_line_instance = ChangePurchaseOrderShipmentLine.from_json(json)
# print the JSON string representation of the object
print(ChangePurchaseOrderShipmentLine.to_json())

# convert the object into a dict
change_purchase_order_shipment_line_dict = change_purchase_order_shipment_line_instance.to_dict()
# create an instance of ChangePurchaseOrderShipmentLine from a dict
change_purchase_order_shipment_line_from_dict = ChangePurchaseOrderShipmentLine.from_dict(change_purchase_order_shipment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


