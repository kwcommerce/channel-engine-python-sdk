# MerchantSingleOrderReturnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_no** | **str** | The unique order reference used by the Merchant. | [optional] 
**lines** | [**List[MerchantSingleOrderReturnLineResponse]**](MerchantSingleOrderReturnLineResponse.md) |  | [optional] 
**created_at** | **datetime** | The date at which the return was created in ChannelEngine. | [optional] 
**updated_at** | **datetime** | The date at which the return was last modified in ChannelEngine. | [optional] 
**merchant_return_no** | **str** | The unique return reference used by the Merchant, will be empty in case of a channel or unacknowledged return. | [optional] 
**channel_return_no** | **str** | The unique return reference used by the Channel, will be empty in case of a merchant return. | [optional] 
**channel_id** | **int** | The id of the channel. | [optional] 
**global_channel_id** | **int** | The id of the Global Channel. | [optional] 
**global_channel_name** | **str** | The name of the Global Channel. | [optional] 
**status** | [**ReturnStatus**](ReturnStatus.md) |  | [optional] 
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
from openapi_client.models.merchant_single_order_return_response import MerchantSingleOrderReturnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSingleOrderReturnResponse from a JSON string
merchant_single_order_return_response_instance = MerchantSingleOrderReturnResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantSingleOrderReturnResponse.to_json())

# convert the object into a dict
merchant_single_order_return_response_dict = merchant_single_order_return_response_instance.to_dict()
# create an instance of MerchantSingleOrderReturnResponse from a dict
merchant_single_order_return_response_from_dict = MerchantSingleOrderReturnResponse.from_dict(merchant_single_order_return_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


