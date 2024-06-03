# MerchantStockLocationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_default** | **bool** |  | [optional] 
**fall_back_to_default** | **bool** | If false: only use fulfillment by channel, else (also) use merchant fulfillment. | [optional] 
**address** | [**MerchantStockLocationAddressRequest**](MerchantStockLocationAddressRequest.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_stock_location_create_request import MerchantStockLocationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantStockLocationCreateRequest from a JSON string
merchant_stock_location_create_request_instance = MerchantStockLocationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantStockLocationCreateRequest.to_json())

# convert the object into a dict
merchant_stock_location_create_request_dict = merchant_stock_location_create_request_instance.to_dict()
# create an instance of MerchantStockLocationCreateRequest from a dict
merchant_stock_location_create_request_from_dict = MerchantStockLocationCreateRequest.from_dict(merchant_stock_location_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


