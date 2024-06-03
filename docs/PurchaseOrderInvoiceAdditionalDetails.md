# PurchaseOrderInvoiceAdditionalDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ModulesAdditionalDetailsType**](ModulesAdditionalDetailsType.md) |  | [optional] 
**detail** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_invoice_additional_details import PurchaseOrderInvoiceAdditionalDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderInvoiceAdditionalDetails from a JSON string
purchase_order_invoice_additional_details_instance = PurchaseOrderInvoiceAdditionalDetails.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderInvoiceAdditionalDetails.to_json())

# convert the object into a dict
purchase_order_invoice_additional_details_dict = purchase_order_invoice_additional_details_instance.to_dict()
# create an instance of PurchaseOrderInvoiceAdditionalDetails from a dict
purchase_order_invoice_additional_details_from_dict = PurchaseOrderInvoiceAdditionalDetails.from_dict(purchase_order_invoice_additional_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


