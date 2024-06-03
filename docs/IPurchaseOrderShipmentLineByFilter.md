# IPurchaseOrderShipmentLineByFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ChannelEngine identifier of the shipment line | [optional] 
**channel_order_no** | **str** | The number the channel uses to identify the purchase order,  which this line (partially) ships. | [optional] 
**item_sequence_number** | **str** | Item sequence number for the item. The first item will be 001, the second 002, and so on.  This number is used as a reference to refer to this item from the carton or pallet level. | [optional] 
**channel_product_no** | **str** | The number the channel uses to identify the product | [optional] 
**merchant_product_no** | **str** | The number the merchant uses to identify the product | [optional] 
**quantity_unit_of_measure** | [**PurchaseOrderLineUnitOfMeasure**](PurchaseOrderLineUnitOfMeasure.md) |  | [optional] 
**quantity** | **int** | The quantity | [optional] 
**quantity_unit_size** | **int** | The case size, in the event that we ordered using cases. Otherwise, it is 1. | [optional] 
**expiry_date** | **datetime** | The date that determines the limit of consumption or use of a product.  For perishable products. | [optional] 

## Example

```python
from openapi_client.models.i_purchase_order_shipment_line_by_filter import IPurchaseOrderShipmentLineByFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IPurchaseOrderShipmentLineByFilter from a JSON string
i_purchase_order_shipment_line_by_filter_instance = IPurchaseOrderShipmentLineByFilter.from_json(json)
# print the JSON string representation of the object
print(IPurchaseOrderShipmentLineByFilter.to_json())

# convert the object into a dict
i_purchase_order_shipment_line_by_filter_dict = i_purchase_order_shipment_line_by_filter_instance.to_dict()
# create an instance of IPurchaseOrderShipmentLineByFilter from a dict
i_purchase_order_shipment_line_by_filter_from_dict = IPurchaseOrderShipmentLineByFilter.from_dict(i_purchase_order_shipment_line_by_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


