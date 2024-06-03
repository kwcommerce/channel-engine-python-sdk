# MerchantAcknowledgePurchaseOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**merchant_order_no** | **str** |  | [optional] 
**lines** | [**List[MerchantAcknowledgePurchaseOrderLine]**](MerchantAcknowledgePurchaseOrderLine.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_acknowledge_purchase_order import MerchantAcknowledgePurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAcknowledgePurchaseOrder from a JSON string
merchant_acknowledge_purchase_order_instance = MerchantAcknowledgePurchaseOrder.from_json(json)
# print the JSON string representation of the object
print(MerchantAcknowledgePurchaseOrder.to_json())

# convert the object into a dict
merchant_acknowledge_purchase_order_dict = merchant_acknowledge_purchase_order_instance.to_dict()
# create an instance of MerchantAcknowledgePurchaseOrder from a dict
merchant_acknowledge_purchase_order_from_dict = MerchantAcknowledgePurchaseOrder.from_dict(merchant_acknowledge_purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


