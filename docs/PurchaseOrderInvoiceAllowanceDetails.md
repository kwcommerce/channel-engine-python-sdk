# PurchaseOrderInvoiceAllowanceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ModulesAllowanceDetailsType**](ModulesAllowanceDetailsType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**charge_amount** | **float** |  | [optional] 
**charge_amount_currency_code** | **str** |  | [optional] 
**tax_details** | [**PurchaseOrderInvoiceTaxDetails**](PurchaseOrderInvoiceTaxDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_invoice_allowance_details import PurchaseOrderInvoiceAllowanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderInvoiceAllowanceDetails from a JSON string
purchase_order_invoice_allowance_details_instance = PurchaseOrderInvoiceAllowanceDetails.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderInvoiceAllowanceDetails.to_json())

# convert the object into a dict
purchase_order_invoice_allowance_details_dict = purchase_order_invoice_allowance_details_instance.to_dict()
# create an instance of PurchaseOrderInvoiceAllowanceDetails from a dict
purchase_order_invoice_allowance_details_from_dict = PurchaseOrderInvoiceAllowanceDetails.from_dict(purchase_order_invoice_allowance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


