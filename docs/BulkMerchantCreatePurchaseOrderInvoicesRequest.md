# BulkMerchantCreatePurchaseOrderInvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**List[MerchantPurchaseOrderInvoice]**](MerchantPurchaseOrderInvoice.md) |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.bulk_merchant_create_purchase_order_invoices_request import BulkMerchantCreatePurchaseOrderInvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMerchantCreatePurchaseOrderInvoicesRequest from a JSON string
bulk_merchant_create_purchase_order_invoices_request_instance = BulkMerchantCreatePurchaseOrderInvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkMerchantCreatePurchaseOrderInvoicesRequest.to_json())

# convert the object into a dict
bulk_merchant_create_purchase_order_invoices_request_dict = bulk_merchant_create_purchase_order_invoices_request_instance.to_dict()
# create an instance of BulkMerchantCreatePurchaseOrderInvoicesRequest from a dict
bulk_merchant_create_purchase_order_invoices_request_from_dict = BulkMerchantCreatePurchaseOrderInvoicesRequest.from_dict(bulk_merchant_create_purchase_order_invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


