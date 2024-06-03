# SingleMerchantAcknowledgePurchaseOrderLinesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**line_identifier_type** | [**PurchaseOrderLineIdentifierType**](PurchaseOrderLineIdentifierType.md) |  | [optional] 
**identifier_type** | [**PurchaseOrderIdentifierType**](PurchaseOrderIdentifierType.md) |  | [optional] 
**model** | [**MerchantAcknowledgePurchaseOrder**](MerchantAcknowledgePurchaseOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.single_merchant_acknowledge_purchase_order_lines_request import SingleMerchantAcknowledgePurchaseOrderLinesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SingleMerchantAcknowledgePurchaseOrderLinesRequest from a JSON string
single_merchant_acknowledge_purchase_order_lines_request_instance = SingleMerchantAcknowledgePurchaseOrderLinesRequest.from_json(json)
# print the JSON string representation of the object
print(SingleMerchantAcknowledgePurchaseOrderLinesRequest.to_json())

# convert the object into a dict
single_merchant_acknowledge_purchase_order_lines_request_dict = single_merchant_acknowledge_purchase_order_lines_request_instance.to_dict()
# create an instance of SingleMerchantAcknowledgePurchaseOrderLinesRequest from a dict
single_merchant_acknowledge_purchase_order_lines_request_from_dict = SingleMerchantAcknowledgePurchaseOrderLinesRequest.from_dict(single_merchant_acknowledge_purchase_order_lines_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


