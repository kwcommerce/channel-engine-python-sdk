# UpdatePurchaseOrderShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_shipment_no** | **str** | The number the merchant uses to identify this PO shipment | [optional] 
**shipment_type** | [**ShipmentType**](ShipmentType.md) |  | [optional] 
**shipped_date** | **datetime** | When the shipment will be/was shipped | [optional] 
**estimated_delivery_date** | **datetime** | Estimated delivery time in the channel&#39;s warehouse | [optional] 
**selling_party_id** | **str** | The merchant&#39;s identifying &#39;selling party number&#39; at the channel | [optional] 
**ship_to_party_id** | **str** | The destination&#39;s &#39;ship to party&#39; number at the channel | [optional] 
**bill_of_lading_number** | **str** | Bill Of Lading (BOL) number is the unique number assigned by the vendor. The BOL present in the Shipment Confirmation message ideally matches the paper BOL provided with the shipment, but that is no must. Instead of BOL, an alternative reference number (like Delivery Note Number) for the shipment can also be sent in this field. | [optional] 
**shipment_weight_unit_of_measure** | [**WeightUnitOfMeasure**](WeightUnitOfMeasure.md) |  | [optional] 
**shipment_weight** | **float** | The shipment&#39;s weight | [optional] 
**shipment_volume_unit_of_measure** | [**VolumeUnitOfMeasure**](VolumeUnitOfMeasure.md) |  | [optional] 
**shipment_volume** | **float** | The shipment&#39;s volume | [optional] 
**lines** | [**List[ChangePurchaseOrderShipmentLine]**](ChangePurchaseOrderShipmentLine.md) | Shipment information for each shipped product | [optional] 

## Example

```python
from openapi_client.models.update_purchase_order_shipment import UpdatePurchaseOrderShipment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderShipment from a JSON string
update_purchase_order_shipment_instance = UpdatePurchaseOrderShipment.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderShipment.to_json())

# convert the object into a dict
update_purchase_order_shipment_dict = update_purchase_order_shipment_instance.to_dict()
# create an instance of UpdatePurchaseOrderShipment from a dict
update_purchase_order_shipment_from_dict = UpdatePurchaseOrderShipment.from_dict(update_purchase_order_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


