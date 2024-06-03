# MerchantProductAttributeGroupWithProductExtraDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_attribute_group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**linked_product_extra_data** | [**List[MerchantProductExtraDataResponse]**](MerchantProductExtraDataResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_attribute_group_with_product_extra_data_response import MerchantProductAttributeGroupWithProductExtraDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductAttributeGroupWithProductExtraDataResponse from a JSON string
merchant_product_attribute_group_with_product_extra_data_response_instance = MerchantProductAttributeGroupWithProductExtraDataResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductAttributeGroupWithProductExtraDataResponse.to_json())

# convert the object into a dict
merchant_product_attribute_group_with_product_extra_data_response_dict = merchant_product_attribute_group_with_product_extra_data_response_instance.to_dict()
# create an instance of MerchantProductAttributeGroupWithProductExtraDataResponse from a dict
merchant_product_attribute_group_with_product_extra_data_response_from_dict = MerchantProductAttributeGroupWithProductExtraDataResponse.from_dict(merchant_product_attribute_group_with_product_extra_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


