# MerchantProductAttributeGroupChannelInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**global_channel_id** | **int** |  | [optional] 
**global_channel_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_attribute_group_channel_info_response import MerchantProductAttributeGroupChannelInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductAttributeGroupChannelInfoResponse from a JSON string
merchant_product_attribute_group_channel_info_response_instance = MerchantProductAttributeGroupChannelInfoResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductAttributeGroupChannelInfoResponse.to_json())

# convert the object into a dict
merchant_product_attribute_group_channel_info_response_dict = merchant_product_attribute_group_channel_info_response_instance.to_dict()
# create an instance of MerchantProductAttributeGroupChannelInfoResponse from a dict
merchant_product_attribute_group_channel_info_response_from_dict = MerchantProductAttributeGroupChannelInfoResponse.from_dict(merchant_product_attribute_group_channel_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


