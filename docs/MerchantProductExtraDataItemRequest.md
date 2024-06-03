# MerchantProductExtraDataItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Name of the extra data field. | 
**value** | **str** | Value of the extra data field. | [optional] 
**type** | [**ExtraDataType**](ExtraDataType.md) |  | [optional] 
**is_public** | **bool** | Add this field to the export of the product feed to the channel. | [optional] 
**language_iso_code** | **str** | The 2-letter ISO code of the extra data | [optional] 

## Example

```python
from openapi_client.models.merchant_product_extra_data_item_request import MerchantProductExtraDataItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductExtraDataItemRequest from a JSON string
merchant_product_extra_data_item_request_instance = MerchantProductExtraDataItemRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantProductExtraDataItemRequest.to_json())

# convert the object into a dict
merchant_product_extra_data_item_request_dict = merchant_product_extra_data_item_request_instance.to_dict()
# create an instance of MerchantProductExtraDataItemRequest from a dict
merchant_product_extra_data_item_request_from_dict = MerchantProductExtraDataItemRequest.from_dict(merchant_product_extra_data_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


