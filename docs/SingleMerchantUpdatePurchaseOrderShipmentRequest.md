# SingleMerchantUpdatePurchaseOrderShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** | The identifier of the channel | [optional] 
**model** | [**UpdatePurchaseOrderShipment**](UpdatePurchaseOrderShipment.md) |  | [optional] 

## Example

```python
from openapi_client.models.single_merchant_update_purchase_order_shipment_request import SingleMerchantUpdatePurchaseOrderShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SingleMerchantUpdatePurchaseOrderShipmentRequest from a JSON string
single_merchant_update_purchase_order_shipment_request_instance = SingleMerchantUpdatePurchaseOrderShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(SingleMerchantUpdatePurchaseOrderShipmentRequest.to_json())

# convert the object into a dict
single_merchant_update_purchase_order_shipment_request_dict = single_merchant_update_purchase_order_shipment_request_instance.to_dict()
# create an instance of SingleMerchantUpdatePurchaseOrderShipmentRequest from a dict
single_merchant_update_purchase_order_shipment_request_from_dict = SingleMerchantUpdatePurchaseOrderShipmentRequest.from_dict(single_merchant_update_purchase_order_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


