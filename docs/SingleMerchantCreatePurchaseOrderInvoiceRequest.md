# SingleMerchantCreatePurchaseOrderInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**MerchantPurchaseOrderInvoice**](MerchantPurchaseOrderInvoice.md) |  | [optional] 
**model** | [**List[MerchantPurchaseOrderInvoice]**](MerchantPurchaseOrderInvoice.md) |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.single_merchant_create_purchase_order_invoice_request import SingleMerchantCreatePurchaseOrderInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SingleMerchantCreatePurchaseOrderInvoiceRequest from a JSON string
single_merchant_create_purchase_order_invoice_request_instance = SingleMerchantCreatePurchaseOrderInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(SingleMerchantCreatePurchaseOrderInvoiceRequest.to_json())

# convert the object into a dict
single_merchant_create_purchase_order_invoice_request_dict = single_merchant_create_purchase_order_invoice_request_instance.to_dict()
# create an instance of SingleMerchantCreatePurchaseOrderInvoiceRequest from a dict
single_merchant_create_purchase_order_invoice_request_from_dict = SingleMerchantCreatePurchaseOrderInvoiceRequest.from_dict(single_merchant_create_purchase_order_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


