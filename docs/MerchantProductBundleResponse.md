# MerchantProductBundleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_product_no** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**parts** | [**List[MerchantProductBundlePartResponse]**](MerchantProductBundlePartResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_product_bundle_response import MerchantProductBundleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantProductBundleResponse from a JSON string
merchant_product_bundle_response_instance = MerchantProductBundleResponse.from_json(json)
# print the JSON string representation of the object
print(MerchantProductBundleResponse.to_json())

# convert the object into a dict
merchant_product_bundle_response_dict = merchant_product_bundle_response_instance.to_dict()
# create an instance of MerchantProductBundleResponse from a dict
merchant_product_bundle_response_from_dict = MerchantProductBundleResponse.from_dict(merchant_product_bundle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


