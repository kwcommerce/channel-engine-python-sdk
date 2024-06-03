# MerchantPurchaseOrderInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_no** | **str** |  | [optional] 
**invoice_type** | [**ModulesPurchaseOrderInvoiceType**](ModulesPurchaseOrderInvoiceType.md) |  | [optional] 
**invoice_total_amount** | **float** |  | [optional] 
**invoice_total_currency_code** | **str** |  | [optional] 
**remit_to_party** | [**MerchantVendorParty**](MerchantVendorParty.md) |  | [optional] 
**ship_to_party_id** | **int** |  | [optional] 
**bill_to_party_id** | **int** |  | [optional] 
**additional_details** | [**List[PurchaseOrderInvoiceAdditionalDetails]**](PurchaseOrderInvoiceAdditionalDetails.md) |  | [optional] 
**lines** | [**List[MerchantPurchaseOrderInvoiceLine]**](MerchantPurchaseOrderInvoiceLine.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_purchase_order_invoice import MerchantPurchaseOrderInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPurchaseOrderInvoice from a JSON string
merchant_purchase_order_invoice_instance = MerchantPurchaseOrderInvoice.from_json(json)
# print the JSON string representation of the object
print(MerchantPurchaseOrderInvoice.to_json())

# convert the object into a dict
merchant_purchase_order_invoice_dict = merchant_purchase_order_invoice_instance.to_dict()
# create an instance of MerchantPurchaseOrderInvoice from a dict
merchant_purchase_order_invoice_from_dict = MerchantPurchaseOrderInvoice.from_dict(merchant_purchase_order_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


