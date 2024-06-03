# IPurchaseOrderLineByFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**channel_order_line_no** | **str** |  | [optional] 
**channel_product_no** | **str** |  | [optional] 
**merchant_product_no** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**is_back_order_allowed** | **bool** |  | [optional] 
**unit_of_measure** | [**PurchaseOrderLineUnitOfMeasure**](PurchaseOrderLineUnitOfMeasure.md) |  | [optional] 
**unit_size** | **int** |  | [optional] 
**net_cost_amount** | **float** |  | [optional] 
**net_cost_currency** | **str** |  | [optional] 
**list_price_amount** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**acknowledged_date** | **datetime** |  | [optional] 
**line_total** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.i_purchase_order_line_by_filter import IPurchaseOrderLineByFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IPurchaseOrderLineByFilter from a JSON string
i_purchase_order_line_by_filter_instance = IPurchaseOrderLineByFilter.from_json(json)
# print the JSON string representation of the object
print(IPurchaseOrderLineByFilter.to_json())

# convert the object into a dict
i_purchase_order_line_by_filter_dict = i_purchase_order_line_by_filter_instance.to_dict()
# create an instance of IPurchaseOrderLineByFilter from a dict
i_purchase_order_line_by_filter_from_dict = IPurchaseOrderLineByFilter.from_dict(i_purchase_order_line_by_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


