# MerchantProductBundlePartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_bundle_part_response import MerchantProductBundlePartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductBundlePartResponse from a JSON string
merchant_product_bundle_part_response_instance = MerchantProductBundlePartResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductBundlePartResponse.to_json())

# convert the object into a dict
merchant_product_bundle_part_response_dict = merchant_product_bundle_part_response_instance.to_dict()
# create an instance of MerchantProductBundlePartResponse from a dict
merchant_product_bundle_part_response_from_dict = MerchantProductBundlePartResponse.from_dict(merchant_product_bundle_part_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


