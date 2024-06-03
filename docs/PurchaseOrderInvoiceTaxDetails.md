# PurchaseOrderInvoiceTaxDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | [**ModulesTaxType**](ModulesTaxType.md) |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**tax_amount_currency_code** | **str** |  | [optional] 
**taxable_amount** | **float** |  | [optional] 
**taxable_amount_currency_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_invoice_tax_details import PurchaseOrderInvoiceTaxDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderInvoiceTaxDetails from a JSON string
purchase_order_invoice_tax_details_instance = PurchaseOrderInvoiceTaxDetails.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderInvoiceTaxDetails.to_json())

# convert the object into a dict
purchase_order_invoice_tax_details_dict = purchase_order_invoice_tax_details_instance.to_dict()
# create an instance of PurchaseOrderInvoiceTaxDetails from a dict
purchase_order_invoice_tax_details_from_dict = PurchaseOrderInvoiceTaxDetails.from_dict(purchase_order_invoice_tax_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


