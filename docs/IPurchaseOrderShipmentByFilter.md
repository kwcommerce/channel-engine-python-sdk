# IPurchaseOrderShipmentByFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ChannelEngine identifier of the shipment | [optional] 
**merchant_shipment_no** | **str** | The number the merchant uses to id this PO shipment | [optional] 
**channel_shipment_no** | **str** | The number the channel uses to id this PO shipment | [optional] 
**shipment_type** | [**ShipmentType**](ShipmentType.md) |  | [optional] 
**shipped_date** | **datetime** | When the shipment was shipped | [optional] 
**estimated_delivery_date** | **datetime** | Estimated delivery time in the channel&#39;s warehouse | [optional] 
**carrier_name** | **str** | Name of the carrier | [optional] 
**carrier_shipment_no** | **str** | The number the carrier uses to id this PO shipment | [optional] 
**bill_of_lading_number** | **str** | Bill of Lading number (not unique for a shipment) | [optional] 
**shipment_weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**shipment_weight** | **float** | The shipment&#39;s weight | [optional] 
**shipment_volume_unit_of_measure** | [**VolumeUnitOfMeasure**](VolumeUnitOfMeasure.md) |  | [optional] 
**shipment_volume** | **float** | The shipment&#39;s volume | [optional] 
**last_merchant_updated_at** | **datetime** | The last time the shipment was updated by the merchant | [optional] 
**last_exported_at** | **datetime** | The last time the shipment was exported to the channel | [optional] 
**last_export_status** | [**PurchaseOrderRelatedItemExportStatus**](PurchaseOrderRelatedItemExportStatus.md) |  | [optional] 
**lines** | [**List[IPurchaseOrderShipmentLineByFilter]**](IPurchaseOrderShipmentLineByFilter.md) | The products in this PO shipment | [optional] 

## Example

```python
from openapi_client.models.i_purchase_order_shipment_by_filter import IPurchaseOrderShipmentByFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IPurchaseOrderShipmentByFilter from a JSON string
i_purchase_order_shipment_by_filter_instance = IPurchaseOrderShipmentByFilter.from_json(json)
# print the JSON string representation of the object
print(IPurchaseOrderShipmentByFilter.to_json())

# convert the object into a dict
i_purchase_order_shipment_by_filter_dict = i_purchase_order_shipment_by_filter_instance.to_dict()
# create an instance of IPurchaseOrderShipmentByFilter from a dict
i_purchase_order_shipment_by_filter_from_dict = IPurchaseOrderShipmentByFilter.from_dict(i_purchase_order_shipment_by_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


