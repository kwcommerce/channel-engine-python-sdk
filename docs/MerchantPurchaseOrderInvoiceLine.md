# MerchantPurchaseOrderInvoiceLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_purchase_order_no** | **str** |  | [optional] 
**merchant_purchase_order_no** | **str** |  | [optional] 
**channel_product_no** | **str** |  | [optional] 
**merchant_product_no** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**net_cost_currency_code** | **str** |  | [optional] 
**net_cost_amount** | **float** |  | [optional] 
**hsn_code** | **str** |  | [optional] 
**cn_reference_invoice_number** | **str** |  | [optional] 
**cn_debit_note_number** | **str** |  | [optional] 
**cn_returns_reference_number** | **str** |  | [optional] 
**cn_rma_id** | **str** |  | [optional] 
**cn_goods_return_date** | **datetime** |  | [optional] 
**cn_coop_reference_number** | **str** |  | [optional] 
**cn_consignors_reference_number** | **str** |  | [optional] 
**allowance_details** | [**List[PurchaseOrderInvoiceAllowanceDetails]**](PurchaseOrderInvoiceAllowanceDetails.md) |  | [optional] 
**tax_details** | [**List[PurchaseOrderInvoiceTaxDetails]**](PurchaseOrderInvoiceTaxDetails.md) |  | [optional] 
**charge_details** | [**List[PurchaseOrderInvoiceChargeDetails]**](PurchaseOrderInvoiceChargeDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_purchase_order_invoice_line import MerchantPurchaseOrderInvoiceLine

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPurchaseOrderInvoiceLine from a JSON string
merchant_purchase_order_invoice_line_instance = MerchantPurchaseOrderInvoiceLine.from_json(json)
# print the JSON string representation of the object
print(MerchantPurchaseOrderInvoiceLine.to_json())

# convert the object into a dict
merchant_purchase_order_invoice_line_dict = merchant_purchase_order_invoice_line_instance.to_dict()
# create an instance of MerchantPurchaseOrderInvoiceLine from a dict
merchant_purchase_order_invoice_line_from_dict = MerchantPurchaseOrderInvoiceLine.from_dict(merchant_purchase_order_invoice_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


