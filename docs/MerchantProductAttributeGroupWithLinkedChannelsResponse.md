# MerchantProductAttributeGroupWithLinkedChannelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_attribute_group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**linked_channels** | [**List[MerchantProductAttributeGroupChannelInfoResponse]**](MerchantProductAttributeGroupChannelInfoResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_attribute_group_with_linked_channels_response import MerchantProductAttributeGroupWithLinkedChannelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductAttributeGroupWithLinkedChannelsResponse from a JSON string
merchant_product_attribute_group_with_linked_channels_response_instance = MerchantProductAttributeGroupWithLinkedChannelsResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductAttributeGroupWithLinkedChannelsResponse.to_json())

# convert the object into a dict
merchant_product_attribute_group_with_linked_channels_response_dict = merchant_product_attribute_group_with_linked_channels_response_instance.to_dict()
# create an instance of MerchantProductAttributeGroupWithLinkedChannelsResponse from a dict
merchant_product_attribute_group_with_linked_channels_response_from_dict = MerchantProductAttributeGroupWithLinkedChannelsResponse.from_dict(merchant_product_attribute_group_with_linked_channels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


