# MerchantReturnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_no** | **str** | The unique order reference used by the Merchant (sku). | 
**merchant_return_no** | **str** | The unique return reference used by the Merchant (sku). | 
**lines** | [**List[MerchantReturnLineRequest]**](MerchantReturnLineRequest.md) |  | 
**id** | **int** | The unique return reference used by ChannelEngine. | [optional] 
**reason** | [**ReturnReason**](ReturnReason.md) |  | [optional] 
**customer_comment** | **str** | Optional. Comment of customer on the (reason of) the return. | [optional] 
**merchant_comment** | **str** | Optional. Comment of merchant on the return. | [optional] 
**refund_incl_vat** | **float** | Refund amount incl. VAT. | [optional] 
**refund_excl_vat** | **float** | Refund amount excl. VAT. | [optional] 
**return_date** | **datetime** | The date at which the return was originally created in the source system (if available). | [optional] 
**extra_data** | **Dict[str, Optional[str]]** | Extra data on the return. Each item must have an unqiue key | [optional] 

## Example

```python
from openapi_client.models.merchant_return_request import MerchantReturnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantReturnRequest from a JSON string
merchant_return_request_instance = MerchantReturnRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantReturnRequest.to_json())

# convert the object into a dict
merchant_return_request_dict = merchant_return_request_instance.to_dict()
# create an instance of MerchantReturnRequest from a dict
merchant_return_request_from_dict = MerchantReturnRequest.from_dict(merchant_return_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


