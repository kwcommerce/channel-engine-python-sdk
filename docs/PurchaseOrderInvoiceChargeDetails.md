# PurchaseOrderInvoiceChargeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ModulesChargeDetailsType**](ModulesChargeDetailsType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**charge_amount** | **float** |  | [optional] 
**charge_amount_currency_code** | **str** |  | [optional] 
**tax_details** | [**PurchaseOrderInvoiceTaxDetails**](PurchaseOrderInvoiceTaxDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_invoice_charge_details import PurchaseOrderInvoiceChargeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderInvoiceChargeDetails from a JSON string
purchase_order_invoice_charge_details_instance = PurchaseOrderInvoiceChargeDetails.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderInvoiceChargeDetails.to_json())

# convert the object into a dict
purchase_order_invoice_charge_details_dict = purchase_order_invoice_charge_details_instance.to_dict()
# create an instance of PurchaseOrderInvoiceChargeDetails from a dict
purchase_order_invoice_charge_details_from_dict = PurchaseOrderInvoiceChargeDetails.from_dict(purchase_order_invoice_charge_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


