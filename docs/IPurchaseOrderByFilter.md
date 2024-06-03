# IPurchaseOrderByFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**global_channel_name** | **str** |  | [optional] 
**global_channel_id** | **int** |  | [optional] 
**channel_purchase_order_no** | **str** |  | [optional] 
**merchant_purchase_order_no** | **str** |  | [optional] 
**status** | [**ModulesPurchaseOrderStatus**](ModulesPurchaseOrderStatus.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**type** | [**ModulesPurchaseOrderType**](ModulesPurchaseOrderType.md) |  | [optional] 
**from_ship_date** | **datetime** |  | [optional] 
**to_ship_date** | **datetime** |  | [optional] 
**from_delivery_date** | **datetime** |  | [optional] 
**to_delivery_date** | **datetime** |  | [optional] 
**import_information** | [**IImportInformation**](IImportInformation.md) |  | [optional] 
**selling_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**ship_to_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**buying_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**billing_party** | [**IVendorParty**](IVendorParty.md) |  | [optional] 
**lines** | [**List[IPurchaseOrderLineByFilter]**](IPurchaseOrderLineByFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.i_purchase_order_by_filter import IPurchaseOrderByFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IPurchaseOrderByFilter from a JSON string
i_purchase_order_by_filter_instance = IPurchaseOrderByFilter.from_json(json)
# print the JSON string representation of the object
print(IPurchaseOrderByFilter.to_json())

# convert the object into a dict
i_purchase_order_by_filter_dict = i_purchase_order_by_filter_instance.to_dict()
# create an instance of IPurchaseOrderByFilter from a dict
i_purchase_order_by_filter_from_dict = IPurchaseOrderByFilter.from_dict(i_purchase_order_by_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


