# MerchantAcknowledgePurchaseOrderLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_line_identifier** | **str** |  | [optional] 
**acknowledgement_code** | [**PurchaseOrderAcknowledgementCode**](PurchaseOrderAcknowledgementCode.md) |  | [optional] 
**acknowledged_quantity** | **int** |  | [optional] 
**rejection_reason** | [**PurchaseOrderRejectionReason**](PurchaseOrderRejectionReason.md) |  | [optional] 
**scheduled_ship_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_acknowledge_purchase_order_line import MerchantAcknowledgePurchaseOrderLine

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAcknowledgePurchaseOrderLine from a JSON string
merchant_acknowledge_purchase_order_line_instance = MerchantAcknowledgePurchaseOrderLine.from_json(json)
# print the JSON string representation of the object
print(MerchantAcknowledgePurchaseOrderLine.to_json())

# convert the object into a dict
merchant_acknowledge_purchase_order_line_dict = merchant_acknowledge_purchase_order_line_instance.to_dict()
# create an instance of MerchantAcknowledgePurchaseOrderLine from a dict
merchant_acknowledge_purchase_order_line_from_dict = MerchantAcknowledgePurchaseOrderLine.from_dict(merchant_acknowledge_purchase_order_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


